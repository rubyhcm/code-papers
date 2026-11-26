# Task 3.1: LightAD Reproduction Report

**Date:** 2026-11-26  
**Hardware:** macOS Apple Silicon (CPU only)  
**Status:** ✅ COMPLETED

---

## Summary

LightAD (ICSE 2024) successfully reproduced on both HDFS_v1 and BGL datasets. All 4 configurations ran without errors after minor fixes.

---

## Issues Fixed

| Issue | Fix |
|---|---|
| Hardcoded path `/mnt/ssd1/yjy/...` in `main_hdfs.py` | Replaced with `os.path.dirname(__file__)` relative path |
| `np.savez` fails on inhomogeneous BGL sequences (numpy 2.x) | Added `dtype=object` to `np.array()` before saving |

---

## Results

### HDFS_v1 (5-fold average)

| Model | Precision | Recall | F1 | Specificity | Balanced Acc | Train (s) | Infer (s) |
|---|---|---|---|---|---|---|---|
| KNN | 0.9978 | 0.9974 | **0.9976** | 0.9999 | 0.9987 | 0.073 | 0.238 |
| DT | 0.9977 | 0.9985 | **0.9981** | 0.9999 | 0.9992 | 0.893 | 0.111 |
| SLFN | 0.9961 | 0.9967 | **0.9964** | 0.9999 | 0.9983 | 5.249 | 0.111 |

**Best HDFS:** DT (F1 = 0.9981)

### BGL (KNN only, per paper protocol)

| Model | Precision | Recall | F1 | Specificity | Balanced Acc |
|---|---|---|---|---|---|
| KNN | 0.9947 | 0.9850 | **0.9898** | 0.9997 | 0.9923 |

---

## Comparison with Paper

LightAD paper (Table 2, HDFS full dataset) reports:
- KNN: F1 ≈ 0.997, DT: F1 ≈ 0.998, SLFN: F1 ≈ 0.996

Our results are within **±0.001 of paper values** ✅ (acceptance criterion: ±5%)

---

## Runtime

| Step | Time |
|---|---|
| HDFS preprocessing | ~26s |
| BGL preprocessing | ~6s |
| HDFS KNN (5 folds) | ~1.2s total |
| HDFS DT (5 folds) | ~5s total |
| HDFS SLFN (5 folds) | ~27s total |
| BGL KNN | ~18 min (949K test sequences) |

---

## Notes

- BGL uses semantic matching (Jaccard distance on token sets), not vectorized features.
  DT/SLFN are not applicable to BGL in the original paper.
- Results saved to: `results/lightad_baseline.json`
