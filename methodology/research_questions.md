# Research Questions - Formal Definition

> **Purpose:** Define 4 research questions guiding the thesis
> **Last updated:** 2026-11-26

---

## Overview

This thesis addresses **4 complementary research questions** to comprehensively evaluate log-based anomaly detection methods across multiple dimensions: effectiveness, cost, trade-offs, and explainability.

---

## RQ1: Detection Effectiveness

### Question Statement

**What is the detection effectiveness (Precision, Recall, F1-score, PR-AUC, FPR) of LightAD (KNN, DT, SLFN), LogFormer, and LogRAG on HDFS_v1 and BGL datasets when evaluated under a unified experimental protocol?**

### Motivation

**Problem:** Prior work evaluates methods on different datasets, preprocessing pipelines, and train/test splits, making fair comparison impossible.

**Gap identified:** 
- LightAD paper tests on HDFS, BGL, Thunderbird (classical ML)
- LogFormer paper tests on 5 datasets (Transformer)
- LogRAG paper tests ONLY on BGL (LLM + RAG)
- No unified benchmark comparing all three paradigms

**Why important:**
- Practitioners need to know which method achieves best detection accuracy
- Need fair comparison with controlled variables (same parser, same split, same hardware)

### Metrics

| Metric | Formula | Why Use It |
|--------|---------|------------|
| **Precision** | TP / (TP + FP) | Measures false alarm rate |
| **Recall** | TP / (TP + FN) | Measures detection coverage |
| **F1-score** | 2 × (P × R) / (P + R) | Harmonic mean, balances P&R |
| **PR-AUC** | Area under P-R curve | Threshold-independent, good for imbalanced data |
| **FPR** | FP / (FP + TN) | Practical concern: alarm fatigue |

**Primary metric:** F1-score and PR-AUC (imbalance-aware)

**Why not Accuracy?** 
- Misleading for imbalanced data
- BGL: 99.6% normal → Predict all "normal" → 99.6% accuracy but 0% recall!

### Expected Insights

**Hypotheses (exploratory, not confirmatory):**
1. **LogRAG likely highest F1** (LLM reasoning > simpler methods)
2. **LightAD competitive** (empirical evidence from LightAD paper)
3. **LogFormer middle ground** (better than classical, worse than LLM)
4. **Performance varies by dataset:** 
   - HDFS (simple, 29 templates) → All methods may perform similarly
   - BGL (complex, ~377 templates) → LLM advantage clearer

**Key questions to answer:**
- Is the extra complexity of LLM worth it? (+2% F1 for 100x cost?)
- Can classical ML match deep learning on simple datasets?

### Relationship to Literature

**Addresses gap:** 
- Literature review (Section 2) identified lack of unified benchmark
- LightAD compared ML vs DL but not vs LLM
- LogRAG not tested on HDFS
- **Our contribution:** First 3-way comparison (ML / Transformer / LLM) on consistent protocol

**Related work:**
- Chen et al. (TSE 2021): Empirical study of 10+ methods
  - But: No LLM methods (too early)
  - Our improvement: Include 2024 SOTA (LogRAG)

---

## RQ2: Computational Cost

### Question Statement

**What are the computational costs (training time, inference latency, memory usage, throughput, API costs) of LightAD, LogFormer, and LogRAG?**

### Motivation

**Problem:** Academic papers prioritize F1-score, ignore deployment feasibility.

**Gap identified:**
- LightAD mentions speed advantages but no rigorous measurement
- LogFormer reports training time but not inference latency
- LogRAG doesn't report API costs (critical for LLM!)

**Why important:**
- **Real-time systems:** Need <1s end-to-end latency
- **Resource constraints:** Edge devices, embedded systems
- **Cost:** LLM API calls expensive ($1-10 per 1K samples)

**Industrial relevance:** From He et al. (ICSE-SEIP 2020), production challenges:
- Latency > 5s → Unusable for real-time
- Memory > 4GB → Deployment issues
- Training > 24h → Hard to retrain frequently

### Metrics

| Metric | Unit | Measurement Method |
|--------|------|-------------------|
| **Training time** | seconds | Wall-clock time (timed) |
| **Inference latency** | ms/sample | Average over 1000 samples |
| **Peak memory** | GB | GPU VRAM + system RAM |
| **Throughput** | samples/sec | Batch inference |
| **API cost** | USD/1K samples | For LogRAG only |

**Hardware:** All measured on SAME machine
- GPU: NVIDIA RTX 3090 (24GB VRAM)
- CPU: 32GB RAM
- OS: Ubuntu 22.04

**Methodology:**
```python
import time
import psutil

start = time.time()
model.fit(X_train, y_train)
training_time = time.time() - start

start = time.time()
predictions = model.predict(X_test)
inference_time = (time.time() - start) / len(X_test) * 1000  # ms per sample
```

### Expected Insights

**Expected ranking (fastest to slowest):**
1. **LightAD (KNN/DT):** <1ms inference, <1 min training
2. **LogFormer:** ~2-5ms inference, ~30 min training
3. **LogRAG:** ~50-100ms inference (LLM latency)

**Expected memory ranking (smallest to largest):**
1. **LightAD:** <500MB
2. **LogRAG:** ~2GB (DeepSVDD + embeddings)
3. **LogFormer:** ~4GB (Transformer model)

**API cost (LogRAG):**
- GPT-3.5: ~$0.002 per 1K tokens
- Estimated: $2-5 per 1K samples
- For full BGL test set (1K samples): ~$2-5

**Key questions:**
- How much faster is LightAD than LogFormer/LogRAG?
- Is LogFormer practical for real-time?
- Is LogRAG affordable for large-scale deployment?

### Relationship to Literature

**Addresses gap:**
- LightAD (ICSE 2024) showed classical ML is fast but didn't quantify comprehensively
- **Our contribution:** Systematic cost measurement across all dimensions

**Related work:**
- Industrial paper (He et al. ICSE-SEIP 2020) emphasized latency
- Our work quantifies latency for SOTA methods

---

## RQ3: Trade-off Analysis

### Question Statement

**What are the Pareto trade-offs between detection effectiveness (F1-score) and computational cost (latency, memory)? Which method provides the best balance for different deployment scenarios?**

### Motivation

**Problem:** No single method dominates all dimensions.
- Best F1 ≠ Fastest ≠ Cheapest

**Gap identified:**
- Papers optimize for F1 alone
- Ignore cost-effectiveness
- No decision framework for practitioners

**Why important:**
- **Deployment scenarios vary:**
  - **Scenario A:** Real-time monitoring (latency critical)
  - **Scenario B:** Batch processing (cost critical)
  - **Scenario C:** High-stakes (F1 critical, cost secondary)
- Practitioners need guidance: "Which method for MY scenario?"

### Metrics & Analysis

**Pareto frontier:**
- Plot: F1 vs Latency
- Plot: F1 vs Memory
- Plot: F1 vs Total Cost (combine latency + memory + API)

**Non-dominated solutions:**
- Method A dominates B if: F1(A) ≥ F1(B) AND Cost(A) ≤ Cost(B)
- Pareto front: Methods NOT dominated by any other

**Radar chart:** Multi-dimensional comparison
- Dimensions: Effectiveness, Speed, Efficiency, Explainability
- Normalize to [0, 1]
- Visual comparison

### Expected Insights

**Expected Pareto frontier:**
```
High F1 ↑
        |           LogRAG ●
        |       LogFormer ●
        |   LightAD (SLFN) ●
        | LightAD (DT) ●
        |LightAD (KNN) ●
        └────────────────────→ Low Latency
```

**Decision framework:**

| Scenario | Requirement | Recommended Method | Reason |
|----------|-------------|-------------------|---------|
| **Real-time (IoT)** | Latency <1ms | LightAD (KNN/DT) | Only method meeting constraint |
| **Cloud (batch)** | F1 > 0.95 | LogRAG or LogFormer | High accuracy, latency OK |
| **Edge device** | Memory <500MB | LightAD | Fits in constrained devices |
| **Cost-sensitive** | Low API cost | LightAD or LogFormer | No LLM API calls |
| **Explainability** | Human-readable | LogRAG or LightAD (DT) | Natural language / rules |

**Quantify trade-offs:**
- "LogRAG: +3% F1 but 50x slower and $5/1K samples"
- "LightAD: -2% F1 but 100x faster and free"

### Relationship to Literature

**Addresses gap:**
- Literature focuses on maximizing F1
- **Our contribution:** Multi-objective evaluation + decision framework

**Related work:**
- InterpretLog (ICSE 2023): Accuracy vs interpretability trade-off
- Our work: Extends to accuracy vs speed vs cost

---

## RQ4: Explainability and Error Analysis

### Question Statement (Two Parts)

**RQ4a - Error Patterns:** What error patterns (False Positives, False Negatives) do the methods exhibit? Can we categorize errors into a systematic taxonomy?

**RQ4b - Explainability Quality:** How explainable are the predictions? How do explanation types compare in actionability, clarity, and correctness?

### Motivation

**Problem:** 
- Black-box models (even with high F1) are hard to trust
- Practitioners need to understand *why* a prediction was made
- Errors are inevitable → need to understand *which cases* fail

**Gap identified:**
- Papers report aggregate F1
- Don't analyze *what* causes errors
- Don't compare explanation quality systematically

**Why important:**
- **Trust:** SREs won't use black-box detectors
- **Debugging:** Understanding errors improves methods
- **Safety:** In critical systems, explainability is mandatory

### RQ4a: Error Taxonomy

**Methodology:**
1. Extract 50-100 FP and 50-100 FN samples per method
2. Manually analyze root causes
3. Create taxonomy

**Proposed taxonomy:**

| Error Type | Description | Example |
|------------|-------------|---------|
| **Unseen template** | Log event not in training | New software version adds log statement |
| **Short sequence** | Insufficient context | Only 2-3 events, hard to judge |
| **Noise** | Parsing errors, malformed logs | Corrupted log line |
| **Semantic ambiguity** | Looks normal but isn't | "Retry succeeded" (after 100 retries = anomaly) |
| **Class imbalance** | Rare anomaly type never seen | Novel failure mode |

**Analysis questions:**
- Which error type most common per method?
- Do methods fail on same cases or different cases?
- Can we predict which cases will be hard?

**Expected insights:**
- **LightAD (KNN/DT):** Likely struggles with unseen templates
- **LogFormer:** Likely better with context (sequential modeling)
- **LogRAG:** Likely handles semantic ambiguity better (LLM reasoning)

### RQ4b: Explainability Comparison

**Explanation types by method:**

| Method | Explanation Type | Example |
|--------|------------------|---------|
| **LightAD (KNN)** | Nearest neighbors | "Anomaly because 5 nearest neighbors are 80% anomalous" |
| **LightAD (DT)** | Decision path | "If EventA=5 AND EventB=0 THEN Anomaly" |
| **LightAD (SLFN)** | Feature importance | "Top features: E5 (0.8), E22 (0.6), E9 (0.4)" |
| **LogFormer** | Attention weights | Heatmap showing which log events model focused on |
| **LogRAG** | Natural language reasoning | "This session is anomalous because repeated 'Connection timeout' (5 times) is unusual. Similar anomalies: Example #3, #7." |

**Evaluation criteria:**

| Criterion | Definition | Assessment Method |
|-----------|------------|-------------------|
| **Actionability** | Can SRE use it to debug? | Manual inspection: Does explanation help locate root cause? |
| **Clarity** | Understandable to non-ML expert? | Readability: Requires ML knowledge? |
| **Correctness** | Aligns with ground truth? | Does explanation match actual reason for label? |

**Scoring (qualitative):**
- ⭐⭐⭐⭐⭐ Excellent
- ⭐⭐⭐⭐ Good
- ⭐⭐⭐ Acceptable
- ⭐⭐ Poor
- ⭐ Unusable

**Expected ranking:**

| Method | Actionability | Clarity | Correctness |
|--------|---------------|---------|-------------|
| LightAD (DT) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| LightAD (KNN) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| LightAD (SLFN) | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| LogFormer | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| LogRAG | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**Key questions:**
- Does LLM natural language explanation truly help debugging?
- Are decision tree rules actionable in practice?
- Is attention better than nothing (vs SLFN)?

### Relationship to Literature

**Addresses gaps:**
- **Error taxonomy:** No prior work categorizes LogAD errors systematically
- **Explainability comparison:** X-LogAD (ASE 2022) used SHAP but didn't compare across paradigms

**Related work:**
- LogLAB (FSE 2021): Attention-based explanations
- X-LogAD (ASE 2022): SHAP for LogAD
- **Our contribution:** Compare 5 explanation types (KNN, DT, SLFN, Attention, LLM)

---

## Summary Table

| RQ | Focus | Metrics | Expected Outcome |
|----|-------|---------|------------------|
| **RQ1** | Effectiveness | P/R/F1/PR-AUC/FPR | Establish fair baseline comparison |
| **RQ2** | Cost | Time/Latency/Memory/Throughput/API | Quantify deployment feasibility |
| **RQ3** | Trade-offs | Pareto analysis | Decision framework for practitioners |
| **RQ4a** | Error patterns | FP/FN taxonomy | Understand failure modes |
| **RQ4b** | Explainability | Actionability/Clarity/Correctness | Compare explanation quality |

---

## Research Contributions

**To academic community:**
1. First unified benchmark: ML vs Transformer vs LLM on LogAD
2. Systematic error taxonomy for LogAD
3. Multi-dimensional explainability comparison

**To practitioners:**
1. Decision framework: Which method for which scenario?
2. Cost-benefit analysis: Is LLM worth it?
3. Error patterns: Where do methods fail?

---

## Validation Strategy

**RQ1-RQ3:** Quantitative
- Statistical tests (Wilcoxon signed-rank)
- Effect sizes (Cohen's d)
- Confidence intervals (5 runs)

**RQ4:** Qualitative + Quantitative
- Quantitative: Error counts, distribution
- Qualitative: Manual analysis of explanations
- (Desirable but out-of-scope: User study with real SREs)

---

**Document status:** ✅ COMPLETE - All 4 RQs formally defined
**Last updated:** 2026-11-26 15:55
**Next:** Integrate into Chapter 3 (Methodology)
