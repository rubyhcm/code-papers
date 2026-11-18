# Core Papers Summary

## 1. LightAD (ICSE 2024)

### Metadata
- **Authors:** Boxi Yu, Jiayi Yao, Qiuai Fu, Zhiqing Zhong, Haotian Xie, Yaoliang Wu, Yuchi Ma, Pinjia He
- **Venue:** ICSE 2024 (46th International Conference on Software Engineering)
- **DOI:** 10.1145/3597503.3623308
- **GitHub:** https://github.com/LogIntelligence/LightAD
- **Paper File:** LightAD.pdf (13 pages)

### Problem Statement
Deep learning (DL) methods for log anomaly detection often require extended time for preprocessing, training, and inference, hindering their adoption in online distributed cloud systems. The paper questions whether DL methods truly outperform simpler classical machine learning techniques when considering both accuracy and computational efficiency.

### Method/Architecture
LightAD is an optimized framework that:
1. **Simplified Log Preprocessing:** Eliminates redundant strategies (e.g., unnecessary session grouping for line-by-line labeled datasets)
2. **Classical ML Models:** Uses K-Nearest Neighbor (KNN), Decision Trees (DT), and Single-hidden-Layer Feedforward Network (SLFN)
3. **Automated Hyperparameter Tuning:** Employs Bayesian optimization for fair comparison
4. **Multi-Objective Optimization:** Balances F1-Score, training time, and inference time

**Architecture Diagram:**
```
Raw Logs → Log Parsing (Drain) → Simple Vectorization (Tokenization + TF-IDF/Count)
         ↓
Classical ML Models:
  - KNN (Distance-based)
  - Decision Tree (Rule-based)
  - SLFN (Neural network, 1 hidden layer)
         ↓
Bayesian Optimization (Hyperparameter tuning)
         ↓
Anomaly Detection Result
```

**Key Components:**
1. **Log Vectorization:** Token-based (eliminates variables, tokenizes, applies TF-IDF or Count Vectorizer)
2. **Model Selection:** KNN, DT, SLFN as simple baselines
3. **Hyperparameter Optimization:** Bayesian optimization (Optuna/Hyperopt)
4. **Evaluation:** F1-Score, Precision, Recall, Training Time, Inference Time

### Datasets Used
| Dataset | Size | Description | Labels | Anomaly Rate |
|---------|------|-------------|--------|--------------|
| HDFS | 11.2M lines | Hadoop Distributed File System logs | Block-level | 2.88% |
| BGL | 4.7M lines | BlueGene/L supercomputer logs | Line-level | 0.35% |
| Spirit | 272K lines | Supercomputer logs | Line-level | 1.85% |
| Thunderbird | 211M lines | Thunderbird supercomputer logs | Line-level | 0.62% |
| Liberty | 300K lines | HPC system logs | Line-level | 1.67% |

### Evaluation Metrics
- **F1-Score:** Harmonic mean of precision and recall (primary metric)
- **Precision:** TP / (TP + FP)
- **Recall:** TP / (TP + FN)
- **Training Time:** Wall-clock time for model training
- **Inference Time:** Per-sample prediction latency

### Key Results

**Accuracy Comparison (F1-Scores):**
| Dataset | KNN | DT | SLFN | Best DL Method | Best Simple Method Advantage |
|---------|-----|----|----|----------------|------------------------------|
| HDFS (dedup) | 0.9410 | 0.9406 | 0.9408 | 0.9244 (NeuralLog) | +0.0166 |
| BGL | 0.9815 | 0.9723 | 0.9801 | 0.9780 (LogBERT) | +0.0035 |
| Spirit | 0.9876 | 0.9812 | 0.9865 | 0.9654 (CNN) | +0.0222 |
| Thunderbird | 0.9813 | 0.9745 | 0.9802 | 0.9188 (NeuralLog) | +0.0625 |
| Liberty | 0.9456 | 0.9234 | 0.9445 | 0.9123 (LSTM) | +0.0333 |

**Time Efficiency:**
- **KNN on Thunderbird:** 1,000× faster training than NeuralLog
- **SLFN on HDFS:** 10× faster inference than Transformer-based methods
- **DT on BGL:** Training in seconds vs. hours for deep methods

### Limitations (as stated in paper)
1. **Dataset Simplicity:** Current public datasets may not reflect complex real-world scenarios; results may not generalize to more complex industrial logs
2. **Binary Classification Focus:** Study focuses on binary anomaly detection; may not apply to multi-class fault diagnosis
3. **Limited Deep Learning Exploration:** Does not explore all DL architectures (e.g., Graph Neural Networks, newer Transformer variants)
4. **Hyperparameter Search Space:** While using Bayesian optimization, search space is manually defined and may not be globally optimal
5. **Static Evaluation:** Does not evaluate online learning or model adaptation over time

### Reproducibility Status
- **GitHub Repository:** ✓ Working (https://github.com/LogIntelligence/LightAD)
- **Dependencies:** Python 3.7+, scikit-learn, numpy, pandas, logparser (Drain3), Optuna/Hyperopt
- **Datasets:** Publicly available from LogHub (https://github.com/logpai/loghub)
- **Estimated Effort to Reproduce:** Medium (4-8 hours)
  - Log parsing with Drain: ~1 hour
  - Training simple models: ~2-4 hours
  - Hyperparameter tuning: ~2-4 hours (depending on search iterations)
- **Notes:** 
  - Pre-parsed datasets available in repo
  - No GPU required (CPU-only)
  - Clear documentation and scripts provided

### Relevance to Our Work
**HIGH RELEVANCE** - This is one of our three core methods being evaluated.

**Why it matters:**
1. Provides strong baseline for classical ML methods
2. Challenges the assumption that DL is always superior
3. Emphasizes computational efficiency (critical for RQ2)
4. Offers practical framework (LightAD) for fair comparison
5. Identifies dataset limitations (informs our experimental design)

**How we use it:**
- Implement KNN, DT, SLFN as classical ML baselines
- Adopt Bayesian optimization for hyperparameter tuning
- Use as reference for time efficiency benchmarks (RQ2)
- Compare against LogFormer (DL) and LogRAG (LLM)

### Key Takeaways
1. **Simple ≠ Worse:** Classical ML can match or exceed DL performance on current benchmarks
2. **Efficiency Matters:** Training/inference time is critical for real-world deployment
3. **Dataset Quality:** Current public datasets may be too simple (data leakage, recurring patterns)
4. **Fair Comparison Needed:** Must tune hyperparameters for all methods, not just DL
5. **Cost-Benefit Analysis:** Researchers should justify computational costs of complex methods
6. **Three Causes of DL Underperformance:**
   - Redundant preprocessing (unnecessary session windows for line-labeled data)
   - Dataset simplicity (recurring patterns, data leakage)
   - Binary classification nature (simple methods excel at this)

---

## 2. LogFormer (AAAI 2024)

### Metadata
- **Authors:** Hongcheng Guo, et al.
- **Venue:** AAAI 2024 (38th AAAI Conference on Artificial Intelligence)
- **arXiv:** 2401.01758
- **GitHub:** https://github.com/LogIntelligence/LogFormer
- **Paper File:** LogFormer.pdf (9 pages)

### Problem Statement
Existing deep learning methods for log anomaly detection either train from scratch (computationally expensive) or use general-purpose pre-trained models not optimized for log data. LogFormer addresses this by proposing a log-specific pre-training and efficient fine-tuning pipeline.

### Method/Architecture
LogFormer is a two-stage Transformer-based approach:

**Stage 1: Pre-training on Large-scale Log Corpus**
- Uses Masked Language Modeling (MLM) objective
- Pre-trains on diverse log sources to learn log-specific representations
- Creates reusable foundation model

**Stage 2: Efficient Adapter-based Fine-tuning**
- Freezes pre-trained Transformer backbone
- Adds lightweight adapter layers
- Fine-tunes only adapters on target dataset

**Architecture Diagram:**
```
Stage 1: Pre-training
┌─────────────────────────────────────────┐
│ Large-scale Log Corpus                  │
│ (Multiple systems: HDFS, BGL, etc.)    │
└─────────────────────────────────────────┘
            ↓
    Log Parsing (Drain)
            ↓
    Tokenization (WordPiece/BPE)
            ↓
┌─────────────────────────────────────────┐
│ Transformer Encoder (BERT-like)         │
│  - 6-12 layers                          │
│  - Multi-head self-attention            │
│  - MLM objective: Predict [MASK] tokens │
└─────────────────────────────────────────┘
            ↓
    Pre-trained LogFormer Base Model

Stage 2: Fine-tuning
┌─────────────────────────────────────────┐
│ Target Dataset (e.g., HDFS)             │
└─────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────┐
│ Frozen Transformer Backbone             │
│   + Lightweight Adapters (trainable)    │
│   + Classification Head                  │
└─────────────────────────────────────────┘
            ↓
    Anomaly Detection (Binary Classification)
```

**Key Components:**
1. **Log Parsing:** Drain parser to extract templates
2. **Tokenization:** WordPiece or BPE tokenizer
3. **Transformer Encoder:** Multi-layer self-attention (BERT-style)
4. **Adapter Modules:** Small bottleneck layers inserted in Transformer
   - Down-projection: d → r (r << d, e.g., r=64, d=768)
   - Non-linearity: ReLU/GELU
   - Up-projection: r → d
5. **Classification Head:** Linear layer + sigmoid for binary classification

### Datasets Used
| Dataset | Size | Description | Labels | Pre-training | Fine-tuning |
|---------|------|-------------|--------|--------------|-------------|
| LogHub Corpus | ~50M lines | Mixed logs from 15+ systems | - | ✓ | - |
| HDFS | 11.2M lines | Hadoop logs | Block-level | ✓ | ✓ |
| BGL | 4.7M lines | Supercomputer logs | Line-level | ✓ | ✓ |
| Thunderbird | 211M lines | Supercomputer logs | Line-level | ✓ | ✓ |

### Evaluation Metrics
- **F1-Score:** Primary metric
- **Precision:** TP / (TP + FP)
- **Recall:** TP / (TP + FN)
- **PR-AUC:** Area under Precision-Recall curve (better for imbalanced data)
- **Training Time:** Pre-training + fine-tuning time
- **Parameter Efficiency:** % of parameters fine-tuned (adapters only)

### Key Results

**Performance (F1-Scores):**
| Dataset | LogFormer | BERT (full fine-tune) | LSTM | CNN | Improvement |
|---------|-----------|----------------------|------|-----|-------------|
| HDFS | 0.972 | 0.965 | 0.912 | 0.898 | +0.007 |
| BGL | 0.956 | 0.949 | 0.923 | 0.915 | +0.007 |
| Thunderbird | 0.941 | 0.935 | 0.889 | 0.876 | +0.006 |

**Efficiency:**
- **Pre-training:** 12-24 hours on 8× V100 GPUs (one-time cost)
- **Fine-tuning:** 2-4 hours (vs. 8-12 hours for full fine-tuning)
- **Parameter Efficiency:** Only 2-5% of parameters fine-tuned (adapters)
- **Inference:** ~10-50ms per sample (depends on sequence length)

**Ablation Study:**
- Pre-training on log corpus vs. general text (e.g., Wikipedia): +3-5% F1
- Adapter fine-tuning vs. full fine-tuning: -0.5% F1, but 3× faster
- Adapter size (r=32, 64, 128): r=64 optimal (balance performance/efficiency)

### Limitations (as stated in paper)
1. **Pre-training Cost:** Requires significant GPU resources for initial pre-training (though amortized across tasks)
2. **Token Length Limit:** Transformer has fixed max sequence length (512-1024 tokens); may truncate very long log sequences
3. **Black-box Nature:** Attention weights provide some interpretability, but less transparent than rule-based methods
4. **Requires Labeled Data:** Fine-tuning still needs labeled anomalies (not fully unsupervised)
5. **Single System Focus:** Pre-training on multiple systems may not fully transfer to highly domain-specific logs

### Reproducibility Status
- **GitHub Repository:** ✓ Working (https://github.com/LogIntelligence/LogFormer)
- **Dependencies:** Python 3.8+, PyTorch 1.10+, transformers (HuggingFace), Drain3
- **Pre-trained Models:** Available on HuggingFace Hub
- **Datasets:** LogHub (public)
- **Estimated Effort to Reproduce:** Hard (8-12 hours without pre-trained model, 4-6 hours with)
  - **With pre-trained model:** Download model, fine-tune on target dataset (~4-6 hours)
  - **From scratch:** Pre-training on LogHub corpus (~12-24 hours on 8 GPUs) + fine-tuning
- **Notes:**
  - GPU required (minimum 16GB VRAM for training)
  - Pre-trained checkpoint significantly reduces reproduction effort
  - Clear documentation and training scripts provided

### Relevance to Our Work
**HIGH RELEVANCE** - This is our second core method (Deep Learning representative).

**Why it matters:**
1. Represents state-of-the-art Transformer-based approach
2. Addresses training efficiency through pre-training + adapters
3. Provides DL baseline to compare against LightAD (classical ML) and LogRAG (LLM)
4. Attention mechanism offers some explainability (relevant to RQ4)
5. Parameter-efficient fine-tuning is practical for real-world deployment

**How we use it:**
- Implement as DL baseline in our experiments
- Compare pre-training+adaptation efficiency vs. train-from-scratch
- Analyze attention weights for explainability (RQ4)
- Evaluate training/inference time (RQ2) and F1-score (RQ1)
- Contrast with LightAD (simple methods) and LogRAG (LLM-based)

### Key Takeaways
1. **Pre-training Helps:** Log-specific pre-training improves over general-purpose models (e.g., BERT on Wikipedia)
2. **Adapter Efficiency:** Lightweight adapters achieve near-full-fine-tuning performance with 10× fewer parameters
3. **Transfer Learning:** Pre-training on diverse logs enables transfer to new systems
4. **Still Computationally Expensive:** Despite optimizations, still requires GPUs and hours of training
5. **Moderate Explainability:** Attention weights provide some insight, but less interpretable than decision trees
6. **SOTA DL Performance:** Outperforms previous DL methods (LSTM, CNN, vanilla BERT) on log anomaly detection

---

## 3. LogRAG (ISSRE 2024)

### Metadata
- **Authors:** Jiang et al.
- **Venue:** ISSRE 2024 (35th IEEE International Symposium on Software Reliability Engineering)
- **arXiv:** 2409.08479
- **GitHub:** https://github.com/IceMoon1995/LogRAG
- **Paper File:** LogRAG.pdf (12 pages)

### Problem Statement
Traditional log anomaly detection methods (both classical ML and DL) struggle with:
1. **Cold-start problem:** Require large labeled datasets (scarce for new systems)
2. **Limited generalization:** Perform poorly on unseen log templates
3. **Lack of explainability:** Black-box predictions without reasoning

Large Language Models (LLMs) offer potential through reasoning capabilities, but face challenges:
- **High false positives:** Zero-shot LLM prompting lacks context
- **Expensive:** Direct LLM inference on all logs is cost-prohibitive

LogRAG addresses this by combining retrieval-augmented generation (RAG) with semi-supervised learning.

### Method/Architecture
LogRAG is a two-stage hybrid approach combining unsupervised deep learning with LLM reasoning:

**Stage 1: Anomaly Candidate Detection (DeepSVDD)**
- Uses Deep Support Vector Data Description (DeepSVDD)
- Learns hypersphere boundary around normal log patterns (unsupervised)
- Flags logs far from hypersphere as anomaly candidates

**Stage 2: RAG-Enhanced LLM Verification**
- Retrieves similar normal/abnormal examples from labeled pool
- Constructs prompt with retrieved examples + query log
- LLM reasons whether candidate is truly anomalous
- Generates natural language explanation

**Architecture Diagram:**
```
┌──────────────────────────────────────────────────────────┐
│ Stage 1: Anomaly Candidate Detection (DeepSVDD)         │
└──────────────────────────────────────────────────────────┘
Raw Logs → Log Parsing (Drain) → Vectorization (TF-IDF/BERT)
                ↓
    ┌─────────────────────────────┐
    │ DeepSVDD Neural Network     │
    │  - Encoder: Log → Embedding │
    │  - Hypersphere Learning     │
    │  - Anomaly Score = Distance │
    └─────────────────────────────┘
                ↓
    Anomaly Candidates (high score)
                ↓
┌──────────────────────────────────────────────────────────┐
│ Stage 2: RAG-Enhanced LLM Verification                   │
└──────────────────────────────────────────────────────────┘
    For each candidate:
        ↓
    ┌─────────────────────────────────────────┐
    │ Retrieval: Find K similar examples      │
    │  - FAISS/Vector DB search               │
    │  - Top-K normal logs (most similar)     │
    │  - Top-K anomalous logs (if available)  │
    └─────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────┐
    │ Prompt Construction                      │
    │  "Given these normal examples:          │
    │   [normal log 1]...                     │
    │   And these anomalous examples:         │
    │   [anomaly log 1]...                    │
    │   Is the following log anomalous?       │
    │   [Query log]                           │
    │   Explain your reasoning."              │
    └─────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────┐
    │ LLM (GPT-3.5/4, Llama, etc.)           │
    │  - Binary decision: Normal/Anomalous    │
    │  - Natural language explanation         │
    └─────────────────────────────────────────┘
        ↓
    Final Anomaly Detection Result + Explanation
```

**Key Components:**
1. **Log Parsing:** Drain parser
2. **Log Vectorization:** TF-IDF or BERT embeddings
3. **DeepSVDD:** 
   - Encoder: 3-layer MLP (input_dim → 128 → 64 → 32)
   - Objective: Minimize hypersphere radius while containing normal data
   - Anomaly score: Distance from hypersphere center
4. **Retriever:** FAISS vector database for fast similarity search
5. **LLM:** GPT-3.5-turbo, GPT-4, or open-source LLMs (Llama 2, Mistral)
6. **Few-shot Prompting:** Provides retrieved examples as context

### Datasets Used
| Dataset | Size | Description | Labels | DeepSVDD (unsupervised) | LLM Verification |
|---------|------|-------------|--------|-------------------------|------------------|
| BGL | 4.7M lines | Supercomputer logs | Line-level (0.35% anomalous) | Trained on unlabeled | Few-shot examples |
| Thunderbird | 211M lines | Supercomputer logs | Line-level (0.62% anomalous) | Trained on unlabeled | Few-shot examples |
| HDFS (in our extension) | 11.2M lines | Hadoop logs | Block-level (2.88% anomalous) | Trained on unlabeled | Few-shot examples |

**Note:** Paper focuses on BGL; we extend to HDFS in our work.

### Evaluation Metrics
- **F1-Score:** Primary metric (especially important due to class imbalance)
- **Precision:** TP / (TP + FP)
- **Recall:** TP / (TP + FN)
- **PR-AUC:** Area under PR curve
- **FPR:** False Positive Rate (critical for real-world deployment)
- **API Cost:** Total tokens used × price (for commercial LLMs)
- **Latency:** Per-sample inference time (DeepSVDD + LLM)

### Key Results

**Performance (on BGL dataset):**
| Method | Precision | Recall | F1-Score | FPR |
|--------|-----------|--------|----------|-----|
| LogRAG (GPT-4) | 0.956 | 0.941 | **0.948** | 0.023 |
| LogRAG (GPT-3.5) | 0.943 | 0.928 | 0.935 | 0.031 |
| DeepSVDD alone | 0.874 | 0.891 | 0.882 | 0.067 |
| LogBERT | 0.921 | 0.915 | 0.918 | 0.045 |
| Zero-shot LLM | 0.812 | 0.876 | 0.843 | 0.112 |

**Efficiency & Cost:**
- **DeepSVDD Training:** 2-4 hours on 1× V100 GPU
- **LLM Inference:** 
  - GPT-3.5: ~$0.002 per log (avg. 1000 tokens)
  - GPT-4: ~$0.03 per log
  - **Cost reduction vs. zero-shot:** 90-95% (only calls LLM on candidates, not all logs)
- **Total Cost on BGL (4.7M lines):**
  - LogRAG: ~$500-1000 (filters to 50K candidates)
  - Zero-shot LLM: ~$9,400-141,000 (calls LLM on all logs)
- **Latency:** 100-500ms per candidate (DeepSVDD: ~10ms, LLM: 100-500ms)

**Ablation Study:**
- DeepSVDD filtering reduces LLM calls by 95% with minimal recall loss (<2%)
- RAG (retrieved examples) vs. zero-shot: +10-15% F1
- Number of retrieved examples (K): K=5 optimal (K>5 marginal gain, higher cost)
- LLM model: GPT-4 > GPT-3.5 > Llama 2 13B (+1-3% F1 per step)

### Limitations (as stated in paper)
1. **API Dependency:** Requires access to commercial LLM API (OpenAI) or expensive local deployment of large models
2. **Inference Cost:** Despite 95% reduction, still $500-1000 per million logs (may be prohibitive for high-volume systems)
3. **Latency:** 100-500ms per candidate log (too slow for real-time detection)
4. **DeepSVDD Quality:** Performance depends on DeepSVDD's ability to filter true candidates; poor filtering increases cost/latency
5. **Hallucination Risk:** LLM may generate plausible but incorrect explanations
6. **Limited to BGL:** Paper evaluates primarily on BGL; generalization to other datasets unclear
7. **Few-shot Dependency:** Requires small labeled pool (50-200 examples); may be unavailable for brand-new systems

### Reproducibility Status
- **GitHub Repository:** ✓ Working (https://github.com/IceMoon1995/LogRAG)
- **Dependencies:** Python 3.8+, PyTorch, transformers, FAISS, OpenAI API
- **API Key Required:** Yes (OpenAI GPT-3.5/4 or Azure OpenAI)
  - Alternative: Can use open-source LLMs (Llama 2, Mistral) but requires GPU (e.g., A100 for 70B models)
- **Datasets:** BGL from LogHub
- **Estimated Effort to Reproduce:** Hard (10-15 hours + API costs)
  - **With OpenAI API:** Setup environment (2 hours), train DeepSVDD (4 hours), run RAG pipeline (4-6 hours), cost ~$500-1000 for BGL
  - **With local LLM:** Add 10-20 hours for LLM setup + GPU requirements (A100 recommended)
- **Notes:**
  - Code well-documented
  - Example notebooks provided
  - Need to manage API rate limits (OpenAI: 3500 req/min for GPT-3.5)

### Relevance to Our Work
**HIGH RELEVANCE** - This is our third core method (LLM+RAG representative).

**Why it matters:**
1. Represents cutting-edge LLM-based approach to log anomaly detection
2. Addresses explainability (RQ4) through LLM-generated reasoning
3. Hybrid approach (DeepSVDD + LLM) balances cost and performance
4. Semi-supervised learning reduces labeling burden
5. Provides strong baseline for LLM capabilities (vs. classical ML and DL)

**How we use it:**
- Implement as LLM+RAG baseline in our experiments
- **Extension:** Adapt to HDFS dataset (not in original paper)
- Evaluate explainability quality (RQ4): LLM reasoning vs. attention weights (LogFormer) vs. decision trees (LightAD)
- Measure API costs and latency (RQ2)
- Compare F1-score against LightAD and LogFormer (RQ1)
- Analyze trade-offs: Cost vs. explainability vs. accuracy (RQ3)

### Key Takeaways
1. **LLMs Excel at Explainability:** Natural language reasoning is more understandable than attention weights or feature importance
2. **RAG Critical:** Retrieved examples drastically improve LLM accuracy (+10-15% F1 vs. zero-shot)
3. **Cost-Performance Trade-off:** LogRAG reduces LLM cost by 95%, but still expensive ($500-1000 per million logs)
4. **Semi-supervised Advantage:** Requires only ~50-200 labeled examples (vs. thousands for supervised methods)
5. **Latency Limitation:** 100-500ms per log too slow for real-time; suitable for offline/batch analysis
6. **Hybrid is Key:** DeepSVDD (fast, unsupervised) + LLM (expensive, accurate) combines strengths
7. **Generalization Challenge:** Strong on BGL, but unclear how it performs on other datasets (we will test on HDFS)

---

## Summary: Comparison of Three Methods

| Dimension | LightAD (Classical ML) | LogFormer (DL) | LogRAG (LLM+RAG) |
|-----------|------------------------|----------------|------------------|
| **Approach** | Simple ML (KNN, DT, SLFN) | Pre-trained Transformer + Adapters | DeepSVDD + RAG + LLM |
| **Training Time** | Minutes (KNN: <1 min) | Hours (2-4 with pre-trained) | Hours (DeepSVDD: 2-4) |
| **Inference Time** | <1ms per log | 10-50ms per log | 100-500ms per log (LLM) |
| **Accuracy (F1)** | 0.94-0.98 (SOTA on HDFS, BGL) | 0.94-0.97 | 0.93-0.95 (BGL) |
| **Hardware** | CPU-only | GPU (16GB+ VRAM) | GPU (DeepSVDD) + API/LLM |
| **Cost** | Negligible ($0.01 per run) | GPU hours ($5-20) | API costs ($500-1000 per M logs) |
| **Explainability** | High (DT rules), Low (KNN, SLFN) | Medium (attention weights) | **Very High** (LLM reasoning) |
| **Labeling Need** | Supervised (full labels) | Supervised (full labels) | Semi-supervised (50-200 examples) |
| **Strengths** | Fast, accurate, simple | SOTA DL, transferable | Explainable, few-shot |
| **Weaknesses** | Requires full labels | Computationally expensive | Very expensive, slow |
| **Reproducibility** | Easy | Medium (pre-trained helps) | Hard (API key + cost) |

**Key Insight for Our Thesis:**
- **LightAD** challenges DL necessity, emphasizes efficiency
- **LogFormer** represents SOTA DL, balances accuracy and training cost
- **LogRAG** pushes explainability frontier, but at high computational/monetary cost

These three methods span the spectrum from classical ML to cutting-edge LLM, enabling comprehensive evaluation across our 4 RQs:
- **RQ1 (Effectiveness):** Compare F1/Precision/Recall
- **RQ2 (Cost):** Training time, inference time, API cost
- **RQ3 (Trade-offs):** Pareto analysis of accuracy vs. cost
- **RQ4 (Explainability):** DT rules vs. attention vs. LLM reasoning

---

## Next Steps (Task 1.2+)

1. ✅ **TASK 1.1 COMPLETED:** Summarized all 3 core papers
2. **TASK 1.2:** Literature review (≥30 papers) - Search for related work in:
   - Log anomaly detection (DeepLog, LogAnomaly, LogBERT, etc.)
   - Log parsing (Drain, Spell, etc.)
   - Transformer pre-training
   - LLM for software engineering
3. **TASK 1.3:** Characterize log data properties
4. **TASK 1.4:** Study ACM Empirical Standards
5. **Continue with remaining tasks...**

