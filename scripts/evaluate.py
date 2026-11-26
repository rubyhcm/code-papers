#!/usr/bin/env python3
"""
Unified evaluation script for LogAD benchmark.
Computes: Precision, Recall, F1, FPR, PR-AUC

Usage:
    # From CSV files:
    python scripts/evaluate.py --pred results/preds.csv --labels data/splits/hdfs_test.csv

    # From arrays (import as module):
    from scripts.evaluate import compute_metrics
    metrics = compute_metrics(y_true, y_pred, y_scores)
"""
import argparse
import csv
import json
import sys


def compute_metrics(y_true, y_pred, y_scores=None):
    """
    Compute all evaluation metrics for binary anomaly detection.

    Args:
        y_true   : list/array of ground truth labels (0=normal, 1=anomaly)
        y_pred   : list/array of predicted labels (0/1)
        y_scores : list/array of anomaly scores (optional, for PR-AUC)

    Returns:
        dict with keys: precision, recall, f1, fpr, pr_auc
    """
    y_true = list(y_true)
    y_pred = list(y_pred)

    if len(y_true) != len(y_pred):
        raise ValueError(f"Length mismatch: y_true={len(y_true)}, y_pred={len(y_pred)}")

    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1        = (2 * precision * recall / (precision + recall)
                 if (precision + recall) > 0 else 0.0)
    fpr       = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    pr_auc = None
    if y_scores is not None:
        try:
            from sklearn.metrics import average_precision_score
            pr_auc = float(average_precision_score(y_true, list(y_scores)))
        except ImportError:
            pr_auc = None

    return {
        "precision": round(precision, 6),
        "recall":    round(recall, 6),
        "f1":        round(f1, 6),
        "fpr":       round(fpr, 6),
        "pr_auc":    round(pr_auc, 6) if pr_auc is not None else None,
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "support_positive": tp + fn,
        "support_negative": fp + tn,
    }


def evaluate_from_files(pred_file, label_file,
                        pred_col="pred", label_col="label", score_col="score"):
    """Load predictions and labels from CSV files and compute metrics."""
    preds, labels, scores = [], [], []
    has_scores = False

    with open(pred_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            preds.append(int(row[pred_col]))
            if score_col in row:
                scores.append(float(row[score_col]))
                has_scores = True

    with open(label_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            labels.append(int(row[label_col]))

    return compute_metrics(labels, preds, scores if has_scores else None)


def print_metrics(metrics, title="Evaluation Results"):
    print(f"\n{'='*45}")
    print(f"  {title}")
    print(f"{'='*45}")
    print(f"  Precision : {metrics['precision']:.4f}")
    print(f"  Recall    : {metrics['recall']:.4f}")
    print(f"  F1        : {metrics['f1']:.4f}")
    print(f"  FPR       : {metrics['fpr']:.4f}")
    if metrics['pr_auc'] is not None:
        print(f"  PR-AUC    : {metrics['pr_auc']:.4f}")
    print(f"{'='*45}")
    print(f"  TP={metrics['tp']:,}  FP={metrics['fp']:,}  "
          f"FN={metrics['fn']:,}  TN={metrics['tn']:,}")
    print(f"  Positives={metrics['support_positive']:,}  "
          f"Negatives={metrics['support_negative']:,}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LogAD Unified Evaluator")
    parser.add_argument("--pred",   required=True, help="CSV file with predictions (col: pred, optionally score)")
    parser.add_argument("--labels", required=True, help="CSV file with ground truth (col: label)")
    parser.add_argument("--pred-col",   default="pred",  help="Prediction column name")
    parser.add_argument("--label-col",  default="label", help="Label column name")
    parser.add_argument("--score-col",  default="score", help="Score column name (optional)")
    parser.add_argument("--output", default=None, help="Save metrics to JSON file")
    args = parser.parse_args()

    metrics = evaluate_from_files(
        args.pred, args.labels,
        pred_col=args.pred_col,
        label_col=args.label_col,
        score_col=args.score_col,
    )

    print_metrics(metrics)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(metrics, f, indent=2)
        print(f"\nSaved to: {args.output}")
