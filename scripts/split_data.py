#!/usr/bin/env python3
"""
Unified data splitting for LogAD benchmark.
Protocol: 80% train / 10% val / 10% test

HDFS_v1: stratified split by Block ID (prevents data leakage)
BGL:     chronological split (preserves temporal ordering)

Usage:
    python scripts/split_data.py
"""
import os
import csv
import random

SEED = 42
random.seed(SEED)

OUTPUT_DIR = "data/splits"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ── HDFS_v1 ──────────────────────────────────────────────────────────────────

def split_hdfs(label_csv, output_dir):
    print("HDFS: loading labels...")
    labels = {}
    with open(label_csv, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            block_id = row['BlockId'].strip()
            label = 0 if row['Label'].strip() == 'Normal' else 1
            labels[block_id] = label

    normal_blocks  = [b for b, l in labels.items() if l == 0]
    anomaly_blocks = [b for b, l in labels.items() if l == 1]

    random.shuffle(normal_blocks)
    random.shuffle(anomaly_blocks)

    def stratified_split(blocks, train_r=0.8, val_r=0.1):
        n = len(blocks)
        t = int(n * train_r)
        v = int(n * (train_r + val_r))
        return blocks[:t], blocks[t:v], blocks[v:]

    n_tr, n_val, n_te = stratified_split(normal_blocks)
    a_tr, a_val, a_te = stratified_split(anomaly_blocks)

    splits = {
        "train": n_tr + a_tr,
        "val":   n_val + a_val,
        "test":  n_te  + a_te,
    }

    for split, blocks in splits.items():
        random.shuffle(blocks)
        rows = [{"block_id": b, "label": labels[b]} for b in blocks]
        out_path = os.path.join(output_dir, f"hdfs_{split}.csv")
        with open(out_path, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["block_id", "label"])
            writer.writeheader()
            writer.writerows(rows)

        n_anom = sum(r["label"] for r in rows)
        print(f"  HDFS {split:5s}: {len(rows):>7,} blocks | "
              f"anomaly rate: {n_anom/len(rows):.4f} ({n_anom:,})")

    tr_set  = set(splits["train"])
    val_set = set(splits["val"])
    te_set  = set(splits["test"])
    assert len(tr_set & val_set) == 0, "train/val overlap!"
    assert len(tr_set & te_set)  == 0, "train/test overlap!"
    assert len(val_set & te_set) == 0, "val/test overlap!"
    print("  OK: no block ID overlap between splits\n")


# ── BGL ──────────────────────────────────────────────────────────────────────

def split_bgl(bgl_log, output_dir, window_size=20, step_size=20):
    print("BGL: reading log and creating windows...")
    windows = []
    buffer = []

    with open(bgl_log, "rb") as f:
        for raw_line in f:
            try:
                line = raw_line.decode("utf-8").strip()
            except UnicodeDecodeError:
                continue
            parts = line.split(" ")
            if len(parts) < 2:
                continue
            label = 0 if parts[0] == "-" else 1
            buffer.append(label)

            if len(buffer) == window_size:
                windows.append(int(any(buffer)))
                buffer = buffer[step_size:]

    if buffer:
        windows.append(int(any(buffer)))

    n = len(windows)
    train_end = int(0.8 * n)
    val_end   = int(0.9 * n)

    splits = {
        "train": windows[:train_end],
        "val":   windows[train_end:val_end],
        "test":  windows[val_end:],
    }

    for split, wins in splits.items():
        out_path = os.path.join(output_dir, f"bgl_{split}.csv")
        with open(out_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["window_idx", "window_label"])
            for idx, lbl in enumerate(wins):
                writer.writerow([idx, lbl])

        n_anom = sum(wins)
        print(f"  BGL  {split:5s}: {len(wins):>7,} windows | "
              f"anomaly rate: {n_anom/len(wins):.4f} ({n_anom:,})")

    print("  OK: chronological order preserved\n")


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  LogAD Benchmark - Data Splitting (seed=42)")
    print("=" * 55 + "\n")

    hdfs_label = "data/raw/hdfs_v1/preprocessed/anomaly_label.csv"
    if os.path.exists(hdfs_label):
        split_hdfs(hdfs_label, OUTPUT_DIR)
    else:
        print(f"WARNING: HDFS label file not found: {hdfs_label}\n")

    bgl_log = "data/raw/bgl/BGL.log"
    if os.path.exists(bgl_log):
        split_bgl(bgl_log, OUTPUT_DIR)
    else:
        print(f"WARNING: BGL log not found: {bgl_log}\n")

    print("Done. Files in:", OUTPUT_DIR)
