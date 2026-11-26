# Method Taxonomy for Log-Based Anomaly Detection

> **Task 2.1-2.4 (Part 2):** Classification of detection methods  
> **Date:** 2026-11-26  
> **Purpose:** Systematic categorization of LogAD approaches

---

## 1. Overview

This document classifies log-based anomaly detection methods into a hierarchical taxonomy based on:
1. **ML Generation:** Classical ML → Deep Learning → LLM
2. **Learning Paradigm:** Supervised → Semi-supervised → Unsupervised
3. **Architecture:** Distance-based, Tree-based, Neural, Sequential, LLM
4. **Feature Type:** Count-based, Sequential, Semantic

---

## 2. Hierarchical Taxonomy

```
Log-Based Anomaly Detection
│
├── Classical Machine Learning
│   ├── Distance-Based
│   │   ├── KNN (K-Nearest Neighbors)
│   │   └── LOF (Local Outlier Factor)
│   │
│   ├── Tree-Based
│   │   ├── Decision Tree
│   │   ├── Random Forest
│   │   └── Isolation Forest
│   │
│   ├── Clustering
│   │   ├── K-Means
│   │   └── DBSCAN
│   │
│   └── Shallow Neural
│       ├── SLFN (Single-Layer Feedforward)
│       └── SVM (Support Vector Machine)
│
├── Deep Learning
│   ├── Recurrent Networks
│   │   ├── DeepLog (LSTM, 2017)
│   │   ├── LogAnomaly (LSTM, 2019)
│   │   └── LogRobust (Attention-LSTM, 2019)
│   │
│   ├── Autoencoders
│   │   ├── LogGAN (GAN-based, 2021)
│   │   └── DeepSVDD (One-class, 2018)
│   │
│   ├── Transformer-Based
│   │   ├── LogBERT (BERT for logs, 2021)
│   │   ├── LogFormer (Pre-train + Adapter, 2024) ⭐ Our study
│   │   └── PLELog (Prompt-based BERT, 2023)
│   │
│   └── Graph Neural Networks
│       └── LogGT (Graph Transformer, 2023)
│
└── Large Language Models
    ├── Prompting-Based
    │   ├── Zero-shot (GPT-4 direct)
    │   └── Few-shot (In-context learning)
    │
    ├── RAG-Based
    │   ├── LogRAG (DeepSVDD + RAG, 2024) ⭐ Our study
    │   └── LogPrompt (Retrieval + Prompting, 2024)
    │
    └── Fine-Tuned
        ├── LogLLM (Fine-tuned LLaMA, 2024)
        └── ChatLog (Fine-tuned GPT-3.5, 2023)
```

---

## 3. Detailed Method Categories

### 3.1 Classical Machine Learning

#### 3.1.1 Distance-Based Methods

**Core Idea:** Anomalies are far from normal data points.

**Methods:**

| Method | Paper | Year | Description | Complexity |
|--------|-------|------|-------------|------------|
| **KNN** | - | Classical | Anomaly if avg distance to k-NN > threshold | O(n²) |
| **LOF** | Breunig et al. | 2000 | Local outlier factor: density-based | O(n²) |

**Advantages:**
- Simple, interpretable (show nearest neighbors)
- No training needed (instance-based)
- Effective for point anomalies

**Disadvantages:**
- High inference cost (need to compute distances)
- Sensitive to feature scaling
- Struggles with high-dimensional data (curse of dimensionality)

**In Our Study:** LightAD-KNN

---

#### 3.1.2 Tree-Based Methods

**Core Idea:** Split data recursively based on features; anomalies follow different decision paths.

**Methods:**

| Method | Paper | Year | Description | Complexity |
|--------|-------|------|-------------|------------|
| **Decision Tree** | - | Classical | Learn if-then rules | O(n log n) train, O(log n) infer |
| **Random Forest** | Breiman | 2001 | Ensemble of trees | O(m·n log n) |
| **Isolation Forest** | Liu et al. | 2008 | Anomalies isolated quickly | O(n log n) |

**Advantages:**
- **Highly interpretable** (can visualize decision tree)
- Handles mixed data types (categorical + numerical)
- No feature scaling needed
- Fast inference

**Disadvantages:**
- Prone to overfitting (single tree)
- May not capture complex patterns

**In Our Study:** LightAD-DT

---

#### 3.1.3 Shallow Neural Networks

**Core Idea:** Learn linear or shallow non-linear decision boundaries.

**Methods:**

| Method | Paper | Year | Description | Complexity |
|--------|-------|------|-------------|------------|
| **SLFN** | Huang et al. | 2006 | Single hidden layer | O(n·d·h) |
| **SVM** | Schölkopf et al. | 2001 | One-class SVM | O(n²) to O(n³) |

**Advantages:**
- Fast training (SLFN)
- Well-established theory (SVM)
- Lower cost than deep learning

**Disadvantages:**
- Limited expressiveness (shallow)
- Less interpretable than trees
- May underfit complex patterns

**In Our Study:** LightAD-SLFN

---

### 3.2 Deep Learning

#### 3.2.1 Recurrent Networks (LSTM)

**Core Idea:** Model sequential dependencies in log event sequences.

**Key Papers:**

| Method | Paper | Venue | Year | Architecture | Key Innovation |
|--------|-------|-------|------|-------------|----------------|
| **DeepLog** | Du et al. | CCS | 2017 | LSTM | First DL for LogAD; predict next event |
| **LogAnomaly** | Meng et al. | IJCAI | 2019 | LSTM + Templates | Semantic + quantitative features |
| **LogRobust** | Zhang et al. | FSE | 2019 | Attention-LSTM | Robust to unstable log data |

**Approach:**
1. Parse logs into event sequences
2. Train LSTM to predict next event
3. Anomaly: Unexpected next event (low probability)

**Advantages:**
- Captures temporal dependencies
- Effective for collective anomalies
- Can model variable-length sequences

**Disadvantages:**
- Slow training (sequential)
- Struggles with long sequences (vanishing gradient)
- Requires large training data

---

#### 3.2.2 Transformer-Based Methods

**Core Idea:** Use self-attention to capture long-range dependencies.

**Key Papers:**

| Method | Paper | Venue | Year | Architecture | Key Innovation |
|--------|-------|-------|------|-------------|----------------|
| **LogBERT** | Guo et al. | IJCNN | 2021 | BERT for logs | Masked log prediction |
| **LogFormer** ⭐ | Guo et al. | AAAI | 2024 | Pre-train + Adapter | Parameter-efficient tuning |
| **PLELog** | Le & Zhang | ASE | 2023 | BERT + Prompting | Prompt learning for few-shot |

**LogFormer Architecture (Our Study):**
```
Phase 1: Pre-training
  Input: Unlabeled log sequences
  Task: Masked Language Modeling (MLM)
  → Pre-trained Transformer

Phase 2: Adapter Tuning
  Input: Labeled log sequences
  Task: Binary classification (normal/anomaly)
  → Fine-tuned with adapters (only 1-5% params updated)
```

**Advantages:**
- **Parallel training** (faster than LSTM)
- **Long-range dependencies** (attention mechanism)
- **Pre-training** leverages unlabeled data
- **Parameter-efficient** (adapter tuning)

**Disadvantages:**
- High GPU memory (self-attention is O(n²))
- Requires large corpus for pre-training
- Less interpretable than classical ML (attention weights need expertise)

**In Our Study:** LogFormer

---

#### 3.2.3 Autoencoders & One-Class Methods

**Core Idea:** Learn to reconstruct normal data; anomalies have high reconstruction error.

**Methods:**

| Method | Paper | Year | Architecture | Key Innovation |
|--------|-------|------|-------------|----------------|
| **DeepSVDD** | Ruff et al. | ICML 2018 | One-class neural net | Hypersphere boundary |
| **LogGAN** | Zhou et al. | 2021 | GAN | Adversarial training |

**DeepSVDD (Used in LogRAG):**
- Train encoder to map normal data to small hypersphere
- Anomaly: Point far from sphere center

**Advantages:**
- Semi-supervised (trains on normal data only)
- Can detect novel anomalies

**Disadvantages:**
- Assumes anomalies are "far" from normal manifold
- Hyperparameter sensitive (sphere radius)

---

### 3.3 Large Language Models

#### 3.3.1 Prompting-Based Methods

**Core Idea:** Use LLM's pre-trained knowledge directly with prompts.

**Approaches:**

| Approach | Description | Example | Pros | Cons |
|----------|-------------|---------|------|------|
| **Zero-shot** | Direct prompting | "Is this log anomalous? [LOG]" | No training | Low accuracy |
| **Few-shot** | In-context examples | "Normal: [LOG1]. Anomaly: [LOG2]. Test: [LOG3]?" | Better than zero-shot | Limited context window |

**Challenges:**
- LLMs not trained specifically for logs
- Generic knowledge may not transfer
- High API cost per query

---

#### 3.3.2 RAG-Based Methods

**Core Idea:** Retrieve relevant examples, then use LLM to reason.

**Key Paper:**

**LogRAG (Our Study)** - Jiang et al., ISSRE 2024

**Architecture:**
```
Phase 1: DeepSVDD Anomaly Detection
  → Identify candidate anomalies

Phase 2: Retrieval-Augmented Generation
  For each candidate:
    1. Retrieve top-k similar log sessions (FAISS)
    2. Construct prompt: "Given these examples: [Retrieved], is [Test] anomalous?"
    3. LLM reasoning: GPT-3.5/4 generates explanation
    4. Final decision: Combine DeepSVDD score + LLM reasoning
```

**Advantages:**
- **Explainable:** LLM provides natural language explanation
- **Few-shot learning:** Retrieves similar examples
- **Semi-supervised:** DeepSVDD phase uses unlabeled data

**Disadvantages:**
- **High cost:** API calls for each test sample
- **Latency:** Retrieval + LLM inference slow
- **Hallucination risk:** LLM may generate plausible but incorrect explanations

**In Our Study:** LogRAG (BGL + HDFS extension)

---

#### 3.3.3 Fine-Tuned LLMs

**Core Idea:** Fine-tune LLM specifically on log data.

**Methods:**

| Method | Base LLM | Venue | Year | Key Insight |
|--------|----------|-------|------|-------------|
| **LogLLM** | LLaMA-7B | arXiv | 2024 | Fine-tune on log corpus |
| **ChatLog** | GPT-3.5 | arXiv | 2023 | Instruction tuning for logs |

**Advantages:**
- Better accuracy than prompting
- Task-specific adaptation

**Disadvantages:**
- Expensive fine-tuning (compute, data)
- Requires large labeled log dataset
- Not evaluated in our study (scope)

---

## 4. Comparison Across Dimensions

### 4.1 By Computational Cost

```
Complexity Hierarchy (Training):
  Classical (DT, KNN)  <  Shallow (SLFN)  <  Deep (LSTM, Transformer)  <  LLM (Fine-tuning)
       Minutes                Hours              Days                       Weeks

Complexity Hierarchy (Inference):
  Classical (DT)  <  Shallow (SLFN)  <  Deep (Transformer)  <  LLM (RAG with API)
      <1ms             ~10ms              ~100ms                  1-10 seconds
```

---

### 4.2 By Supervision Requirements

| Method Category | Supervision | Label Requirements | Use Case |
|----------------|-------------|-------------------|----------|
| Classical (KNN) | Unsupervised | None | Exploratory, quick baseline |
| Classical (DT, SLFN) | Supervised | Thousands | Production with labeled data |
| Deep (DeepSVDD) | Semi-sup | Mostly normal | Realistic (anomalies rare) |
| Deep (LogFormer) | Semi-sup | Pre-train unlabeled, tune labeled | Leverage unlabeled data |
| LLM (LogRAG) | Semi-sup | Few-shot | Explainability needed |

---

### 4.3 By Interpretability

```
Interpretability Spectrum:
  Highest                                                              Lowest
     ↓                                                                    ↓
  Decision Tree  >  LogRAG (NL explanation)  >  KNN (neighbors)  >  Attention  >  SLFN

For non-ML users:
  LogRAG (natural language) >> All others
```

---

### 4.4 By Data Requirements

| Method | Training Data Size | Labeled Data | Pre-training | Use Case |
|--------|-------------------|--------------|--------------|----------|
| **KNN** | Moderate (10K-100K) | Optional | No | Small datasets |
| **DT** | Moderate (10K-100K) | Required | No | Interpretable baseline |
| **SLFN** | Large (100K-1M) | Required | No | Fast training |
| **LSTM** | Large (1M-10M) | Required | Optional | Sequential data |
| **Transformer** | Very large (10M-100M) | Unlabeled (pre-train) + Few labeled (tune) | Yes | State-of-art |
| **LLM-RAG** | Moderate (100K-1M) | Few-shot (100-1K) | LLM pre-trained | Explainability |

---

## 5. Evolution of LogAD Methods (Timeline)

```
2017: DeepLog (LSTM)           ← First DL for LogAD
      ↓
2019: LogAnomaly, LogRobust    ← Improved LSTM variants
      ↓
2021: LogBERT                  ← Transformers enter LogAD
      ↓
2023: PLELog                   ← Prompt learning
      ↓
2024: LogFormer ⭐              ← Efficient pre-training + adapters
      LogRAG ⭐                 ← LLM + RAG for explainability
      ↓
2024: LightAD ⭐                ← Revisiting classical ML (efficiency focus)
```

**Trend 1:** Deep Learning dominance (2017-2023)
**Trend 2:** LLM integration (2023-2024)
**Counter-Trend:** Classical ML revival for efficiency (LightAD, 2024)

**Our Study:** Compares all 3 generations (Classical, DL, LLM) for first time!

---

## 6. Positioning Our 3 Methods

### 6.1 LightAD (Classical ML, ICSE 2024)

**Category:** Classical Machine Learning

**Key Insight:** "Deep learning may be overkill for LogAD"

**Contribution:**
- Shows classical ML (KNN, DT, SLFN) competitive with LSTM on 16 datasets
- Much faster training and inference
- Challenges the "DL is always better" assumption

**Position in Taxonomy:**
- Distance-based (KNN)
- Tree-based (DT)
- Shallow neural (SLFN)

**Why Important:** Efficiency + Interpretability

---

### 6.2 LogFormer (Deep Learning, AAAI 2024)

**Category:** Deep Learning → Transformer

**Key Insight:** "Pre-training + adapter tuning is parameter-efficient"

**Contribution:**
- Pre-train on large unlabeled log corpus (BigLog: 100M logs)
- Fine-tune with adapters (only 1-5% params updated)
- State-of-art on 10 datasets

**Position in Taxonomy:**
- Transformer-based
- Semi-supervised (pre-train unlabeled, tune labeled)

**Why Important:** Leverages unlabeled data + Accuracy

---

### 6.3 LogRAG (LLM, ISSRE 2024)

**Category:** LLM → RAG-based

**Key Insight:** "Combine anomaly detection + LLM reasoning for explainability"

**Contribution:**
- Phase 1: DeepSVDD detects candidates
- Phase 2: RAG retrieves similar examples + LLM explains
- Natural language explanations for SREs

**Position in Taxonomy:**
- LLM-based
- RAG (Retrieval-Augmented Generation)
- Semi-supervised

**Why Important:** Explainability + Few-shot learning

---

## 7. Summary Table: Our 3 Methods

| Dimension | LightAD | LogFormer | LogRAG |
|-----------|---------|-----------|--------|
| **ML Family** | Classical | Deep Learning | LLM |
| **Architecture** | KNN/DT/SLFN | Transformer + Adapter | DeepSVDD + RAG |
| **Supervision** | Sup / Unsup | Semi-supervised | Semi-supervised |
| **Training Data** | 100K-1M | 10M-100M (pre-train) | 100K-1M + LLM API |
| **Training Time** | Minutes | Hours-Days | Hours (DeepSVDD) |
| **Inference Time** | <1ms (DT) | ~100ms | 1-10s (API) |
| **Interpretability** | ⭐⭐⭐⭐ (DT) | ⭐⭐ (Attention) | ⭐⭐⭐⭐⭐ (NL) |
| **Accuracy** | Good | State-of-art | State-of-art |
| **Cost** | Very Low | Medium | High (API) |

---

## 8. Research Gap Addressed by Our Study

**Existing Work:**
- Most papers compare within one generation (e.g., LSTM vs Transformer)
- Few compare across generations (Classical vs DL vs LLM)
- Limited focus on explainability and computational cost

**Our Contribution:**
1. **Cross-generational comparison:** First to systematically compare Classical, DL, LLM on same datasets
2. **Multi-dimensional evaluation:** Not just accuracy, but also cost, explainability, error patterns
3. **Fair protocol:** Same data splits, same hardware, same evaluation metrics
4. **Practical guidelines:** When to use which method (decision tree)

---

## 9. References

### Classical ML
1. Breunig, M. M., et al. (2000). LOF: Identifying density-based local outliers. *SIGMOD*.
2. Liu, F. T., et al. (2008). Isolation forest. *ICDM*.

### Deep Learning
3. Du, M., et al. (2017). DeepLog: Anomaly detection and diagnosis from system logs through deep learning. *CCS*.
4. Meng, W., et al. (2019). LogAnomaly: Unsupervised detection of sequential and quantitative anomalies. *IJCAI*.
5. Guo, H., et al. (2021). LogBERT: Log anomaly detection via BERT. *IJCNN*.
6. Guo, H., et al. (2024). LogFormer: A pre-train and tuning pipeline for log anomaly detection. *AAAI*.
7. Le, V. H., & Zhang, H. (2023). PLELog: Prompt learning for log-based anomaly detection. *ASE*.

### LLM
8. Jiang, Z., et al. (2024). Leveraging RAG-enhanced large language models for semi-supervised log anomaly detection. *ISSRE*.

### Our Methods
9. Yu, X., et al. (2024). Deep learning or classical machine learning? An empirical study on log-based anomaly detection. *ICSE*. (LightAD)
10. Guo, H., et al. (2024). LogFormer: A pre-train and tuning pipeline for log anomaly detection. *AAAI*.
11. Jiang, Z., et al. (2024). LogRAG paper. *ISSRE*.

---

**Status:** ✅ COMPLETE - Comprehensive method taxonomy established

**Next:** Task 2.5 (Write Chapter 2 continuation) or Task 2.6-10 (Environment setup)
