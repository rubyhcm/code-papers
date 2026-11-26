# Taxonomy of Anomaly Detection

> **Task 2.1-2.4:** Hệ thống hóa phát hiện bất thường  
> **Date:** 2026-11-26  
> **Purpose:** Formal classification of anomaly types and detection approaches

---

## 1. Anomaly vs Fault vs Failure

These terms are often confused. We adopt the following definitions:

| Term | Definition | Level | Example (Log Context) |
|------|------------|-------|---------------------|
| **Anomaly** | Deviation from expected behavior (data-centric) | Data | Unusual log event sequence |
| **Fault** | Root cause of a problem (system-centric) | System | Memory leak in Service X |
| **Failure** | Observable malfunction (user-centric) | Service | Service timeout, 500 error |

**Relationships:**
```
Fault → Anomaly → Failure
```

- Not all anomalies are faults (benign deviations)
- Not all faults cause immediate failures (latent bugs)
- Anomaly detection is a **proxy** for fault/failure detection

**Example Scenario:**

```
1. Fault:        Memory leak introduced in deployment v2.3
                 ↓
2. Anomaly:      Increasing frequency of "OutOfMemory" log events
                 Growing heap usage patterns in log metrics
                 ↓
3. Failure:      Service crashes with OOM error
                 User sees "503 Service Unavailable"
```

**LogAD Focus:** We detect **anomalies** (unusual log patterns) which may indicate **faults** before they cause **failures**.

---

## 2. Types of Anomalies

### 2.1 Point Anomaly

**Definition:** A single data point that deviates significantly from the rest of the dataset.

**In LogAD:**
- One log event that never appeared in training
- Example: `"ERROR: UnknownException in module X"` (never seen before)

**Detection:**
- Frequency-based: Rare event detection
- Statistical: Outlier in feature space

**Challenges:**
- High false positive rate (legitimate new events)
- Requires representative training data

**Example:**
```
Normal:   INFO: Request processed in 20ms
Normal:   INFO: Request processed in 25ms
Anomaly:  FATAL: Segmentation fault at address 0x0000  ← Point anomaly
Normal:   INFO: Request processed in 22ms
```

---

### 2.2 Collective Anomaly (Sequential Anomaly)

**Definition:** A collection of data points that is anomalous as a whole, even though individual points may appear normal.

**In LogAD:**
- Sequence of log events that is unusual
- Example: Normal events A→B→C, but seeing A→C→B is anomalous

**Detection:**
- Sequence modeling: LSTM, Transformer
- N-gram analysis: Check if sequence seen in training

**Challenges:**
- Longer sequences harder to detect
- Need to capture temporal dependencies

**Example:**
```
Normal sequence:
  1. INFO: Connection established
  2. INFO: Authentication successful
  3. INFO: Data transfer started
  4. INFO: Data transfer complete
  5. INFO: Connection closed

Anomalous sequence:
  1. INFO: Connection established
  2. INFO: Data transfer started    ← Skipped authentication!
  3. INFO: Data transfer complete
  4. INFO: Connection closed
```

Each individual event is normal, but the **sequence** is anomalous.

---

### 2.3 Contextual Anomaly

**Definition:** A data point that is anomalous only in a specific context, but normal in other contexts.

**In LogAD:**
- Event is normal in one context (e.g., daytime), anomalous in another (e.g., nighttime)
- Example: Heavy traffic logs at 3 AM (unusual), but normal at 3 PM

**Detection:**
- Requires context features (time, session ID, user)
- Conditional models: P(event | context)

**Challenges:**
- Need to identify relevant context
- Context may be implicit in log data

**Example:**
```
Context: Business hours (9 AM - 6 PM)
  INFO: 10,000 login requests    ← Normal

Context: Midnight (12 AM - 1 AM)
  INFO: 10,000 login requests    ← Anomalous! (Possible attack)
```

---

### 2.4 Summary Table

| Type | Individual Events | Sequence | Context | Detection Method |
|------|------------------|----------|---------|-----------------|
| **Point** | Anomalous | N/A | Independent | Frequency, outlier detection |
| **Collective** | Normal | Anomalous | Temporal | Sequence modeling (LSTM, Transformer) |
| **Contextual** | Depends | Depends | Context-dependent | Conditional models |

**Most LogAD work focuses on:** **Collective (Sequential) Anomalies**

---

## 3. Detection Approaches (by Supervision)

### 3.1 Supervised Learning

**Definition:** Train on labeled data (both normal and anomalous samples).

**Advantages:**
- High accuracy if labels are correct
- Can learn complex decision boundaries

**Disadvantages:**
- Requires large labeled dataset (expensive!)
- Cannot detect novel anomalies (unseen in training)

**In our study:**
- **LightAD:** Decision Tree, SLFN (when trained with labels)
- **Example:** Train on 80% labeled logs, test on 20%

**Key Assumption:** Anomalies in test set are similar to training anomalies.

---

### 3.2 Semi-Supervised Learning

**Definition:** Train mostly on normal data, with few (or no) anomalies.

**Approaches:**
1. **One-class classification:** Learn boundary around normal data
   - Example: DeepSVDD (used in LogRAG)
2. **Anomaly detection with few labeled anomalies:** Few-shot learning

**Advantages:**
- Realistic: Normal data is abundant, anomalies are rare
- Can detect novel anomalies (not seen in training)

**Disadvantages:**
- May have higher false positive rate
- Assumes training data is "clean" (no hidden anomalies)

**In our study:**
- **LogRAG:** DeepSVDD trains on mostly normal data, then uses RAG for few-shot refinement

**Key Assumption:** Test anomalies deviate from normal manifold learned during training.

---

### 3.3 Unsupervised Learning

**Definition:** No labels at all; detect anomalies purely based on deviations from data distribution.

**Approaches:**
- Clustering: Anomalies are far from cluster centers
- Density estimation: Anomalies have low probability
- Reconstruction: Anomalies have high reconstruction error (Autoencoders)

**Advantages:**
- No labeling cost
- Can discover unknown anomaly types

**Disadvantages:**
- Highest false positive rate
- Hard to evaluate without labels (need labeled test set)

**In our study:**
- **LightAD-KNN:** Distance-based unsupervised (can run without labels)

**Key Assumption:** Anomalies are "outliers" in the data distribution.

---

### 3.4 Summary Table

| Approach | Training Data | Strengths | Weaknesses | Use Case |
|----------|--------------|-----------|------------|----------|
| **Supervised** | Labeled (normal + anomaly) | High accuracy | Expensive labels | Known anomaly types |
| **Semi-supervised** | Mostly normal + few labeled | Detects novel anomalies | Higher FP rate | Rare anomalies |
| **Unsupervised** | Unlabeled | No labeling cost | Highest FP rate | Exploratory analysis |

---

## 4. Classification of Our 3 Methods

### 4.1 LightAD

**Type:** Classical Machine Learning

**Models:**
1. **KNN (K-Nearest Neighbors)**
   - Approach: Distance-based
   - Supervision: Can be supervised or unsupervised
   - Anomaly: Points far from k nearest neighbors

2. **DT (Decision Tree)**
   - Approach: Rule-based
   - Supervision: Supervised
   - Anomaly: Learned from labeled examples

3. **SLFN (Single-Layer Feedforward Network)**
   - Approach: Neural network (shallow)
   - Supervision: Supervised
   - Anomaly: Learned classification boundary

**Anomaly Type Addressed:** Primarily **collective** (uses session-level features: event count vectors)

**Explainability:**
- KNN: Show nearest neighbors
- DT: Show decision path (highly interpretable)
- SLFN: Feature importance (less interpretable)

---

### 4.2 LogFormer

**Type:** Deep Learning (Transformer)

**Architecture:**
- Pre-training: Self-supervised on unlabeled logs (mask language modeling)
- Adapter tuning: Supervised fine-tuning on labeled logs

**Supervision:** Semi-supervised (pre-train on unlabeled, tune on labeled)

**Anomaly Type Addressed:** **Collective** (sequential anomalies via attention mechanism)

**Explainability:**
- Attention weights: Which log events the model focuses on
- Moderate interpretability (requires ML knowledge)

---

### 4.3 LogRAG

**Type:** LLM-based (RAG + Reasoning)

**Architecture:**
1. **Phase 1 (DeepSVDD):** Semi-supervised anomaly detection (learns normal data manifold)
2. **Phase 2 (RAG):** Retrieve similar examples + LLM reasoning

**Supervision:** Semi-supervised (DeepSVDD) + Few-shot (RAG)

**Anomaly Type Addressed:** **Collective** (session-level), with **contextual** reasoning via LLM

**Explainability:**
- Retrieved examples: "Similar logs that were anomalous"
- LLM reasoning chain: Natural language explanation
- Highest interpretability (for non-ML users)

---

### 4.3 Comparison Matrix

| Method | ML Family | Supervision | Anomaly Type | Explainability | Complexity |
|--------|-----------|-------------|--------------|----------------|------------|
| **LightAD-KNN** | Classical ML | Unsup/Sup | Collective | ⭐⭐⭐ (neighbors) | Low |
| **LightAD-DT** | Classical ML | Supervised | Collective | ⭐⭐⭐⭐⭐ (rules) | Low |
| **LightAD-SLFN** | Shallow DL | Supervised | Collective | ⭐⭐ (features) | Medium |
| **LogFormer** | Deep Learning | Semi-sup | Collective | ⭐⭐ (attention) | High |
| **LogRAG** | LLM | Semi-sup | Collective + Context | ⭐⭐⭐⭐⭐ (NL) | Very High |

---

## 5. Mapping to Research Questions

### RQ1 (Effectiveness)
- Evaluate all 3 supervision types: Supervised (LightAD), Semi-sup (LogFormer, LogRAG), Unsup (LightAD-KNN)

### RQ2 (Computational Cost)
- Complexity hierarchy: Classical < Shallow DL < Deep DL < LLM
- Hypothesis: LightAD fastest, LogRAG most expensive

### RQ3 (Trade-offs)
- Pareto frontier: Effectiveness vs Cost
- Expected: LightAD-DT = "Pareto optimal" (high F1, low cost)

### RQ4 (Explainability)
- Explainability spectrum: DT (best) → RAG (best for non-experts) → Attention (moderate) → SLFN (worst)

---

## 6. Challenges in Log-Based Anomaly Detection

### Challenge 1: High Dimensionality
- **Problem:** Thousands of unique log templates → sparse feature space
- **Solution:** Dimensionality reduction (PCA, embeddings), template clustering

### Challenge 2: Concept Drift
- **Problem:** Log templates evolve over time (software updates)
- **Solution:** Online learning, periodic retraining

### Challenge 3: Class Imbalance
- **Problem:** 95-99% normal logs, 1-5% anomalies
- **Solution:** Resampling (SMOTE), cost-sensitive learning, PR-AUC instead of Accuracy

### Challenge 4: Ambiguous Labels
- **Problem:** What is an "anomaly"? (Soft failures, warnings)
- **Solution:** Multiple annotators, consensus labeling

### Challenge 5: Temporal Dependencies
- **Problem:** Anomalies span multiple events (collective anomalies)
- **Solution:** Sequence modeling (LSTM, Transformer), session grouping

### Challenge 6: Explainability vs Accuracy
- **Problem:** Black-box models (DL) are more accurate but less interpretable
- **Solution:** Hybrid approaches (LogRAG), attention visualization, post-hoc explanations

---

## 7. Relationship to Related Work

### Traditional Anomaly Detection (Non-Log)
- **Image:** CNNs for defect detection
- **Network:** IDS using flow statistics
- **Time Series:** ARIMA, LSTM for forecasting

**LogAD Differences:**
- Semi-structured data (templates + parameters)
- Discrete event sequences (not continuous signals)
- Domain-specific semantics (log parsing needed)

### AIOps and Site Reliability Engineering (SRE)
- LogAD is one component of AIOps
- Other components: Metrics anomaly, trace analysis, incident prediction
- Our work focuses on **log-based** detection

---

## 8. Summary

**Key Taxonomies:**
1. **Anomaly Types:** Point, Collective, Contextual
2. **Supervision:** Supervised, Semi-supervised, Unsupervised
3. **ML Families:** Classical, Deep Learning, LLM

**Our Study:**
- **3 Methods:** LightAD (Classical), LogFormer (DL), LogRAG (LLM)
- **3 Supervision Types:** All covered
- **1 Anomaly Type:** Collective (sequential)
- **2 Datasets:** HDFS (simple), BGL (complex)

**Contribution:** First systematic comparison across **ML generations** (Classical → DL → LLM) with unified protocol.

---

## References

1. Chandola, V., Banerjee, A., & Kumar, V. (2009). Anomaly detection: A survey. *ACM Computing Surveys*, 41(3), 1-58.
2. Chalapathy, R., & Chawla, S. (2019). Deep learning for anomaly detection: A survey. *arXiv:1901.03407*.
3. Pang, G., Shen, C., Cao, L., & Hengel, A. V. D. (2021). Deep learning for anomaly detection: A review. *ACM Computing Surveys*, 54(2), 1-38.
4. He, S., Zhu, J., He, P., & Lyu, M. R. (2020). Loghub: A large collection of system log datasets towards automated log analytics. *arXiv:2008.06448*.

---

**Status:** ✅ COMPLETE - Formal taxonomy established for thesis Chapter 2

**Next:** Task 2.5 (Write Chapter 2 continuation on anomaly detection methods)
