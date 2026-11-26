# Dataset Comparison Table

> **Generated:** 2026-11-26 16:22
> **Source:** `analysis/dataset_statistics.json`

---

## Quantitative Comparison

| Characteristic | HDFS_v1 | BGL | Difference |
|----------------|---------|-----|------------|
| **Data Size** | | | |
| Total instances | 575,061 blocks | 4,365,033 logs | 7.6x more logs |
| Unique templates | 29 | 1,775 | 61x more diverse |
| Average sequence length | 19.4 events | N/A (single events) | - |
| **Anomaly Statistics** | | | |
| Anomaly count | 16,838 | 527,404 | 31x more anomalies |
| Normal count | 558,223 | 3,837,629 | 6.9x more normals |
| Anomaly rate | 2.93% | 12.08% ⚠️ | 4.1x higher |
| Imbalance ratio | 1:33 | 1:7 | HDFS more imbalanced |
| **Template Distribution** | | | |
| Most frequent template | E5 (1.7M occurrences) | E3 (1.7M occurrences) | Similar scale |
| Least frequent template | E24 (57 occurrences) | 889 templates (1 occurrence) | BGL has many rare templates |
| Median occurrences | ~59K per template | 1 per template | HDFS more uniform |
| **System Characteristics** | | | |
| System type | Distributed file system | Supercomputer | Different domains |
| Log period | 38 hours | 214 days | BGL much longer |
| Grouping | Block-based (session) | Individual events | HDFS has natural sessions |
| Anomaly source | Fault injection | Natural errors | Different realism |

---

## Qualitative Comparison

### HDFS_v1

**Strengths:**
- ✅ **Well-structured:** Natural session grouping by BlockId
- ✅ **Low template diversity:** 29 templates → Easier to learn patterns
- ✅ **Controlled anomalies:** Fault injection → Clean labels
- ✅ **Balanced sequences:** Mean 19.4 events, Std 5.2 → Consistent length

**Weaknesses:**
- ⚠️ **Synthetic anomalies:** May not reflect real production failures
- ⚠️ **Short duration:** 38 hours → Limited failure modes
- ⚠️ **High imbalance:** 1:33 ratio → Hard for minority class learning

**Use cases:**
- Benchmarking on **simple, structured** log data
- Testing session-based anomaly detection
- Evaluating on controlled failure scenarios

---

### BGL

**Strengths:**
- ✅ **Natural errors:** Production supercomputer → Realistic failures
- ✅ **Long period:** 214 days → Diverse failure modes
- ✅ **High diversity:** 1,775 templates → Tests generalization

**Weaknesses:**
- ⚠️ **No natural sessions:** Time-window based → Arbitrary grouping
- ⚠️ **High anomaly rate:** 12% (expected 0.4%) → Label extraction issue
- ⚠️ **Extreme template imbalance:** Median 1 occurrence → Many rare templates
- ⚠️ **Old data:** From 2005 → May not reflect modern systems

**Use cases:**
- Benchmarking on **complex, diverse** log data
- Testing robustness to high template diversity
- Evaluating on natural production failures

---

## Implications for Experiments

### For RQ1 (Effectiveness)

**Expected results:**
- **HDFS (simpler):** All methods likely perform well (F1 > 0.90)
  - Reason: Only 29 templates, clear patterns, controlled anomalies
  - Differentiator: Handling imbalance (1:33 ratio)

- **BGL (complex):** Larger performance gaps between methods
  - Reason: 1,775 templates, diverse failures, rare events
  - LLM/Transformer advantage clearer here

**Hypothesis:**
```
HDFS:  LightAD ≈ LogFormer ≈ LogRAG (all ~0.92-0.96 F1)
BGL:   LightAD < LogFormer < LogRAG (gap: 0.88 → 0.92 → 0.94)
```

### For RQ2 (Cost)

**Dataset size impact:**
- HDFS: 575K blocks → Fast to train/test (~minutes for all methods)
- BGL: 4.3M logs → Longer training (~hours for LogFormer/LogRAG)

**Complexity impact:**
- HDFS (29 templates) → Small feature space → LightAD very fast
- BGL (1,775 templates) → Large feature space → May challenge classical ML

### For RQ3 (Trade-offs)

**Different optimal methods per dataset?**
- HDFS: LightAD sufficient (simple data, fast method)
- BGL: LogFormer/LogRAG needed (complex data, worth the cost)

### For RQ4 (Explainability & Errors)

**Expected error patterns:**
- **HDFS:**
  - FN: Rare anomaly types (imbalance)
  - FP: Short sequences (insufficient context)

- **BGL:**
  - FN: Unseen templates (high diversity)
  - FP: Semantic ambiguity (natural errors harder to classify)

---

## Dataset Selection Rationale

**Why these two?**
1. **Complementary characteristics:**
   - HDFS: Simple, controlled, session-based
   - BGL: Complex, natural, event-based

2. **Standard benchmarks:**
   - Both from LogHub (reproducible)
   - Widely used in literature (comparable to prior work)

3. **Cover key challenges:**
   - Imbalance (HDFS 1:33, BGL 1:7)
   - Diversity (HDFS 29, BGL 1,775)
   - Realism (HDFS synthetic, BGL natural)

**What's missing?**
- Modern cloud systems (AWS, Azure, GCP)
- Microservices logs (distributed tracing)
- Streaming logs (real-time processing)

**Future work:** Extend to modern datasets (e.g., AIOps Challenge datasets)

---

## ⚠️ BGL Anomaly Rate Issue

**Problem:** 12.08% anomaly rate vs expected 0.4%

**Possible causes:**
1. **Label extraction too aggressive:** Marking all ERROR/FATAL as anomalies
2. **Different BGL version:** May be using different subset
3. **Ground truth mismatch:** LogHub labels may differ from original paper

**Action needed:**
1. Review `extract_label()` function in parser
2. Compare with LogHub official labels
3. If needed, adjust threshold (e.g., only FATAL → anomaly)

**Impact:**
- **Low for benchmarking:** As long as consistent across methods
- **Important for literature comparison:** Need to document difference

---

## Visualization Summary

Generated figures in `analysis/figures/`:

1. **`anomaly_rate_comparison.png`**
   - Bar chart: HDFS 2.93% vs BGL 12.08%
   - Shows imbalance severity

2. **`hdfs_sequence_length.png`**
   - Histogram: Distribution of sequence lengths
   - Mean 19.4, Median 19, relatively consistent

3. **`template_diversity.png`**
   - Bar chart: 29 vs 1,775 templates
   - Visualizes complexity difference

---

## References

**Data sources:**
- HDFS_v1: `data/raw/hdfs_v1/preprocessed/`
- BGL: `data/parsed/bgl_structured.jsonl`

**Analysis script:**
- `scripts/analyze_datasets.py`

**Statistics:**
- `analysis/dataset_statistics.json` (full details)

---

**Last updated:** 2026-11-26 16:22  
**Next:** Task 1.8 - HDFS vs BGL detailed comparison
