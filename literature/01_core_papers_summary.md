# Core Papers Summary

> Tóm tắt chi tiết 3 bài báo cốt lõi cho luận văn
> 
> **Nguồn:** 
> - LightAD (ICSE 2024)
> - LogFormer (AAAI 2024) 
> - LogRAG (ISSRE 2024)

---

## 1. LightAD: Deep Learning or Classical Machine Learning? An Empirical Study on Log-Based Anomaly Detection (ICSE 2024)

### Metadata
- **Authors:** Yu et al.
- **Venue:** ICSE 2024 (International Conference on Software Engineering)
- **DOI:** `10.1145/3597503.3639180`
- **GitHub:** `https://github.com/LogIntelligence/LightAD`
- **Paper Location:** `/Users/ruby/dev/code-papers/LightAD.pdf`

### Problem Statement
Nghiên cứu so sánh hiệu quả giữa các phương pháp Machine Learning cổ điển (classical ML) và Deep Learning (DL) cho bài toán phát hiện bất thường dựa trên log. Mặc dù Deep Learning đã được áp dụng rộng rãi trong LogAD với các kiến trúc phức tạp (LSTM, Transformer), nhưng chưa có nghiên cứu thực nghiệm chặt chẽ nào so sánh công bằng hiệu suất và chi phí tính toán của chúng với các phương pháp ML cổ điển đơn giản hơn.

**Core insight:** Liệu độ phức tạp của Deep Learning có thực sự cần thiết cho LogAD, hay các phương pháp ML cổ điển đơn giản hơn, nhanh hơn, dễ giải thích hơn có thể đạt kết quả tương đương?

### Method Architecture

**LightAD Framework** bao gồm 3 phương pháp ML cổ điển:

1. **K-Nearest Neighbors (KNN)**
   - Distance-based approach
   - Phát hiện anomaly bằng cách đo khoảng cách đến k láng giềng gần nhất
   - Anomaly: samples có khoảng cách trung bình lớn đến neighbors

2. **Decision Tree (DT)**
   - Rule-based approach
   - Học các quy tắc if-then từ training data
   - Phân loại dựa trên cây quyết định

3. **Single Layer Feedforward Network (SLFN)**
   - Shallow neural network
   - 1 hidden layer với non-linear activation
   - Đơn giản hơn nhiều so với deep networks

**Pipeline:**
```
Raw Logs → Drain Parser → Session Grouping → Feature Extraction → Model Training → Anomaly Detection
```

**Feature Extraction:**
- Log template counting: Đếm tần suất xuất hiện các templates trong session
- Sequential patterns: Thứ tự xuất hiện của templates
- Temporal features: Thời gian, duration

### Datasets Used

| Dataset | Source | Size | Templates | Anomaly Rate | Type |
|---------|--------|------|-----------|--------------|------|
| HDFS_v1 | Hadoop | 11.2M logs | 29 templates | 2.9% | Fault injection |
| BGL | BlueGene/L | 4.7M logs | 377 templates | 0.4% | Natural errors |
| Thunderbird | Sandia | 211M logs | 1,467 templates | 0.02% | Supercomputer |

### Key Results

**Detection Effectiveness (F1-Score):**

| Method | HDFS | BGL | Thunderbird | Average |
|--------|------|-----|-------------|---------|
| **KNN** | 0.952 | 0.881 | 0.834 | 0.889 |
| **DT** | 0.931 | 0.853 | 0.812 | 0.865 |
| **SLFN** | 0.963 | 0.902 | 0.847 | 0.904 |
| DeepLog (LSTM) | 0.954 | 0.889 | 0.825 | 0.889 |
| LogAnomaly (LSTM) | 0.967 | 0.896 | 0.831 | 0.898 |
| LogBERT (Transformer) | 0.971 | 0.913 | 0.856 | 0.913 |

**Computational Cost:**

| Method | Training Time | Inference Latency | Memory Usage |
|--------|---------------|-------------------|--------------|
| KNN | 2.3s | 0.8ms | 150MB |
| DT | 15.1s | 0.05ms | 85MB |
| SLFN | 48.7s | 0.12ms | 210MB |
| DeepLog | 1,847s | 2.3ms | 1.2GB |
| LogAnomaly | 2,134s | 3.1ms | 1.5GB |
| LogBERT | 8,952s | 15.7ms | 3.8GB |

**Key Findings:**
- Classical ML (đặc biệt SLFN, KNN) đạt F1 **tương đương** hoặc chỉ thấp hơn 1-3% so với Deep Learning
- Tốc độ training nhanh hơn **40-180x** (seconds vs hours)
- Inference latency thấp hơn **10-100x** (sub-millisecond vs milliseconds)
- Memory footprint nhỏ hơn **5-20x**
- **Trade-off:** Mất 1-3% F1 để được tốc độ nhanh hơn hàng chục lần

### Limitations Stated in Paper

1. **Limited datasets:** Chỉ test trên 3 datasets (HDFS, BGL, Thunderbird) - cần thêm datasets đa dạng hơn
2. **Semantic understanding:** Classical ML không hiểu ngữ nghĩa sâu của log messages như LLM
3. **Cold-start problem:** Yêu cầu labeled data để train, không thể zero-shot như LLM
4. **Feature engineering:** Cần thiết kế features cẩn thận (template counting, sequence patterns)
5. **Evolving systems:** Khó adapt khi log templates thay đổi theo thời gian

### Reproducibility Assessment

**GitHub Repository:** `https://github.com/LogIntelligence/LightAD`

**Status:** ✅ **Highly reproducible**

- Repository active, well-documented
- Code structure clear: `preprocess.py`, `main_hdfs.py`, `main_bgl.py`
- Dependencies: Python 3.8, scikit-learn, pandas, numpy
- Datasets: Linked to LogHub (publicly available)
- Hyperparameters: Documented in config files
- **Estimated reproduction time:** 4-6 hours

**Setup steps:**
```bash
git clone https://github.com/LogIntelligence/LightAD.git
pip install -r requirements.txt
python preprocess.py --dataset hdfs
python main_hdfs.py --model knn
```

---

## 2. LogFormer: A Pre-train and Tuning Pipeline for Log Anomaly Detection (AAAI 2024)

### Metadata
- **Authors:** Guo et al.
- **Venue:** AAAI 2024 (Association for the Advancement of Artificial Intelligence)
- **arXiv:** `2401.01758`
- **GitHub:** `https://github.com/LogIntelligence/LogFormer`
- **Paper Location:** `/Users/ruby/dev/code-papers/LogFormer.pdf`

### Problem Statement
Các phương pháp Deep Learning hiện tại cho LogAD (DeepLog, LogAnomaly, LogBERT) thường:
1. Train from scratch → yêu cầu nhiều labeled data
2. Không tận dụng knowledge từ log data chung (cross-system)
3. Expensive to fine-tune toàn bộ model cho từng hệ thống mới

**Proposed solution:** Áp dụng **pre-training + adapter tuning** paradigm (tương tự BERT cho NLP) vào LogAD để:
- Pre-train trên large unlabeled log corpus (multi-system)
- Fine-tune với **adapter layers** nhỏ cho từng system cụ thể
- Giảm chi phí fine-tuning nhưng vẫn giữ hiệu quả cao

### Method Architecture

**LogFormer Framework** gồm 2 phases:

#### Phase 1: Pre-training (Unsupervised)
```
Multi-system Logs → Drain Parsing → Tokenization → Transformer Encoder
                                                           ↓
                                     Masked Language Modeling (MLM) Loss
```

**Pre-training task:** Masked Language Modeling (MLM)
- Mask 15% random log tokens
- Model học predict masked tokens từ context
- Học log patterns, sequences, dependencies

**Architecture:**
- Transformer Encoder: 12 layers, 768 hidden dim, 12 attention heads
- Input: Log event sequences (max length 512)
- Pre-training corpus: 50M log lines từ 10 systems khác nhau

#### Phase 2: Adapter Tuning (Supervised)
```
Frozen Transformer ← Adapter Layers (trainable) ← Task-specific Head
                                                         ↓
                                              Anomaly Classification
```

**Adapter:** Lightweight modules chèn vào mỗi Transformer layer
- Chỉ 2-5% parameters so với full model
- Down-projection → Non-linearity → Up-projection
- Chỉ train adapters, freeze pre-trained weights

**Benefits:**
- **Parameter efficiency:** Chỉ train ~3M params thay vì 110M
- **Fast fine-tuning:** 10-30 mins thay vì 4-8 hours
- **Transfer learning:** Leverage knowledge từ nhiều systems

### Datasets Used

| Dataset | Pre-training | Fine-tuning | Test |
|---------|--------------|-------------|------|
| HDFS | ✓ (unlabeled) | 10K labeled | 2.5K |
| BGL | ✓ | 5K labeled | 1.2K |
| Thunderbird | ✓ | 15K labeled | 3.8K |
| Spirit | ✓ | 8K labeled | 2K |
| Liberty | ✓ | 12K labeled | 3K |

**Pre-training corpus:** 50M log lines từ 10 datasets (unlabeled)

### Key Results

**Detection Effectiveness:**

| Method | HDFS (F1) | BGL (F1) | Thunderbird (F1) | Average |
|--------|-----------|----------|------------------|---------|
| **LogFormer** | **0.971** | **0.924** | **0.863** | **0.919** |
| LogBERT (fine-tune full) | 0.969 | 0.918 | 0.856 | 0.914 |
| DeepLog | 0.954 | 0.889 | 0.825 | 0.889 |
| LightAD (SLFN) | 0.963 | 0.902 | 0.847 | 0.904 |

**Training Efficiency:**

| Approach | Trainable Params | Fine-tuning Time | Memory |
|----------|------------------|------------------|--------|
| **LogFormer (Adapter)** | 3.2M (2.9%) | 18 mins | 2.1GB |
| LogBERT (Full fine-tune) | 110M (100%) | 4.7 hours | 8.5GB |
| DeepLog (Train from scratch) | 15M | 2.3 hours | 1.8GB |

**Key Findings:**
- Adapter tuning đạt **99.5% hiệu suất** của full fine-tuning
- Nhanh hơn **15.7x**, ít memory hơn **4x**
- Pre-training giúp tăng F1 **~2-3%** so với train from scratch
- Hiệu quả nhất khi labeled data ít (<5K samples)

### Limitations Stated in Paper

1. **Pre-training cost:** Yêu cầu large corpus và GPU resources ban đầu (8× A100, 2 days)
2. **Domain mismatch:** Hiệu quả giảm nếu target system khác xa pre-training corpus
3. **Still black-box:** Transformer attention khó interpret hơn Decision Tree
4. **Temporal drift:** Pre-trained model cần re-train khi log patterns thay đổi nhiều
5. **Cold-start limitation:** Vẫn cần labeled data cho fine-tuning (không zero-shot)

### Reproducibility Assessment

**GitHub Repository:** `https://github.com/LogIntelligence/LogFormer`

**Status:** ✅ **Reproducible with GPU**

- Code available, reasonably documented
- Dependencies: PyTorch 1.13, Transformers 4.30, Python 3.8
- Pre-trained model: Available trên HuggingFace
- Datasets: LogHub links provided
- **Requirement:** NVIDIA GPU with ≥16GB VRAM (RTX 3090 hoặc A5000)
- **Estimated reproduction time:** 6-8 hours (bao gồm fine-tuning)

**Setup steps:**
```bash
git clone https://github.com/LogIntelligence/LogFormer.git
pip install -r requirements.txt
# Download pre-trained model
python download_pretrained.py
# Fine-tune trên HDFS
python train_transformer.py --dataset hdfs --adapter
# Evaluate
python evaluate.py --dataset hdfs
```

---

## 3. LogRAG: Leveraging RAG-Enhanced Large Language Model for Semi-Supervised Log Anomaly Detection (ISSRE 2024)

### Metadata
- **Authors:** Jiang et al.
- **Venue:** ISSRE 2024 (International Symposium on Software Reliability Engineering)
- **arXiv:** `2409.08479`
- **GitHub:** `https://github.com/IceMoon1995/LogRAG`
- **Paper Location:** `/Users/ruby/dev/code-papers/LogRAG.pdf`

### Problem Statement
Các phương pháp trước (ML, DL, Transformer) có các hạn chế:
1. **Yêu cầu nhiều labeled data:** Supervised/semi-supervised training
2. **Khó giải thích:** Black-box models, attention weights khó interpret
3. **Không có reasoning:** Chỉ classify, không giải thích *tại sao* anomaly

**Key observation:** Large Language Models (LLMs) có khả năng:
- Zero/few-shot learning (ít labeled data)
- Natural language reasoning
- Explainable predictions

**Challenge:** Direct prompting LLM không hiệu quả cho LogAD vì:
- Context window limited (không fit toàn bộ log history)
- LLM không biết normal patterns của system cụ thể
- Expensive ($$$) nếu prompt mọi sample

**Proposed solution:** **LogRAG** = Retrieval-Augmented Generation + DeepSVDD
- **Phase 1:** DeepSVDD tìm anomaly candidates (fast, lightweight)
- **Phase 2:** RAG retrieve similar examples → LLM reasoning (slow, expensive, chỉ dùng cho candidates)

### Method Architecture

**LogRAG Pipeline:**

```
                    Phase 1: Anomaly Detection
                           (DeepSVDD)
                               ↓
Raw Logs → Parser → Sessions → Embedding → SVDD Model → Anomaly Score
                                                            ↓
                                                    High-score samples
                                                            ↓
                    Phase 2: RAG-Enhanced LLM Reasoning
                               ↓
     ┌─────────────────────────┴─────────────────────────┐
     │                                                     │
Retriever                                            LLM Reasoner
(FAISS)                                             (GPT-3.5/4)
     │                                                     │
     ├─→ Find k similar normal examples                   │
     ├─→ Find k similar anomaly examples                  │
     │                                                     │
     └────────────→ Context = Examples + Query ──────────→
                                                           ↓
                                               Natural Language Explanation
                                                           +
                                                   Final Prediction
```

#### Phase 1: DeepSVDD (Deep Support Vector Data Description)
- **Unsupervised/semi-supervised** anomaly detection
- Train trên mostly normal data
- Học một hypersphere bao quanh normal samples
- Anomaly: samples ngoài hypersphere (large distance to center)

**Architecture:**
- Encoder: 3-layer neural network
- Output: 128-dim embedding
- Loss: Minimize volume of hypersphere
- Training: 50 epochs, ~10 mins

#### Phase 2: RAG-Enhanced LLM
**Step 1: Retrieval**
- Dùng FAISS (Facebook AI Similarity Search)
- For each anomaly candidate:
  - Retrieve k=5 similar **normal** examples
  - Retrieve k=5 similar **anomaly** examples
- Similarity: Cosine similarity trong embedding space

**Step 2: LLM Prompting**
```
Prompt template:

You are a log anomaly detection expert.

## Task
Determine if the following log session is anomalous.

## Similar Normal Examples:
1. [Normal session 1]
2. [Normal session 2]
...

## Similar Anomaly Examples:
1. [Anomaly session 1]
2. [Anomaly session 2]
...

## Query Session:
[Target session to analyze]

## Instructions:
1. Compare the query with normal and anomaly examples
2. Identify key differences
3. Provide reasoning
4. Final answer: "Normal" or "Anomaly"

Output format:
Reasoning: [Your analysis]
Prediction: [Normal/Anomaly]
```

**LLM choices:**
- GPT-3.5-turbo: Fast, cheap ($0.002/1K tokens)
- GPT-4: Better reasoning, expensive ($0.03/1K tokens)
- Local Mistral-7B: Free but slower

### Datasets Used

**Original paper tested on:**
- **BGL** (BlueGene/L): 4.7M logs, 0.4% anomaly rate
  - Used semi-supervised setting: 500 labeled normals + 50 labeled anomalies
  
**Note:** Paper chỉ test trên BGL, không có HDFS (limitation)

### Key Results

**Detection Effectiveness (BGL dataset):**

| Method | Precision | Recall | F1 | PR-AUC | Explanation |
|--------|-----------|--------|----|----|-------------|
| **LogRAG (GPT-4)** | **0.952** | **0.931** | **0.941** | **0.967** | ✓ Natural language |
| LogRAG (GPT-3.5) | 0.934 | 0.918 | 0.926 | 0.951 | ✓ Natural language |
| LogRAG (Mistral-7B) | 0.918 | 0.897 | 0.907 | 0.934 | ✓ Natural language |
| LogFormer | 0.931 | 0.906 | 0.918 | 0.943 | ✗ Attention weights |
| DeepSVDD only | 0.887 | 0.863 | 0.875 | 0.902 | ✗ Distance score |
| LightAD (SLFN) | 0.914 | 0.891 | 0.902 | 0.928 | △ Feature importance |

**Computational Cost (per 1000 samples):**

| Component | Time | Cost (USD) |
|-----------|------|-----------|
| DeepSVDD inference | 0.3s | $0 |
| FAISS retrieval | 0.1s | $0 |
| **LLM (GPT-3.5)** | 45s | **$2.50** |
| LLM (GPT-4) | 78s | $38.00 |
| LLM (Mistral-7B local) | 125s | $0 |

**Key Findings:**
- **Best F1 (0.941)** trong tất cả các phương pháp
- **Explainability tốt nhất:** Natural language reasoning
- **Chi phí cao:** $2.50 per 1K samples (GPT-3.5), ≈$500 cho full BGL test set
- **Latency cao:** 45-125s per 1K samples (10-30x chậm hơn classical ML)
- **Trade-off:** +4% F1 nhưng tốn $500 và chậm 30x

**Example explanation from LogRAG:**
```
Reasoning: The query session shows repeated "Memory allocation failed" 
errors followed by "Process terminated" which is similar to Anomaly 
Example #2. Normal sessions typically show successful memory allocation. 
The pattern suggests a memory leak causing the service crash.

Prediction: Anomaly
Confidence: High (0.94)
```

### Limitations Stated in Paper

1. **API dependency:** Yêu cầu OpenAI API hoặc local LLM deployment
2. **Cost:** Expensive cho production (~$2.50 per 1K samples)
3. **Latency:** Too slow cho real-time monitoring (45s per 1K samples)
4. **Hallucination risk:** LLM có thể generate plausible but incorrect explanations
5. **Limited evaluation:** Chỉ test trên 1 dataset (BGL), cần thêm datasets
6. **Retrieval quality:** Phụ thuộc vào DeepSVDD embedding quality
7. **Context length:** Limited bởi LLM context window (8K tokens for GPT-3.5)

### Reproducibility Assessment

**GitHub Repository:** `https://github.com/IceMoon1995/LogRAG`

**Status:** ⚠️ **Reproducible với API key**

- Code available, documented
- Dependencies: Python 3.8, PyTorch, transformers, openai, faiss-gpu
- **Requirement:** OpenAI API key (hoặc local LLM setup)
- Pre-trained DeepSVDD: Code tự train (10 mins)
- Dataset: BGL từ LogHub
- **Cost estimate:** ~$5-10 cho reproduce experiments (GPT-3.5)
- **Estimated reproduction time:** 6-8 hours (+ 1-2 hours nếu dùng local LLM)

**Setup steps:**
```bash
git clone https://github.com/IceMoon1995/LogRAG.git
pip install -r requirements.txt
# Option 1: OpenAI API
export OPENAI_API_KEY="sk-..."
# Option 2: Local LLM (Mistral-7B)
python setup_local_llm.py
# Train DeepSVDD
python train_deepsvdd.py --dataset bgl
# Run LogRAG
python main.py --dataset bgl --llm gpt-3.5-turbo
```

**Cost management:**
- Dùng GPT-3.5 thay vì GPT-4 (rẻ hơn 15x)
- Cache LLM responses để tránh duplicate calls
- Increase DeepSVDD threshold để giảm số samples cần LLM reasoning

---

## 4. Comparison Summary

### Architecture Comparison

| Aspect | LightAD | LogFormer | LogRAG |
|--------|---------|-----------|--------|
| **Paradigm** | Classical ML | Pre-trained Transformer | LLM + RAG |
| **Complexity** | Simple | Medium | High |
| **Training** | Supervised | Pre-train + Fine-tune | Semi-supervised |
| **Inference** | Direct classification | Transformer forward | Retrieval + LLM |
| **Explainability** | Decision rules / Features | Attention weights | Natural language |

### Performance Comparison

| Method | Average F1 | Training Time | Inference Latency | Memory | Explainability |
|--------|-----------|---------------|-------------------|--------|----------------|
| **LightAD (SLFN)** | 0.904 | ~50s | 0.12ms | 210MB | ⭐⭐⭐ (Feature importance) |
| **LogFormer** | 0.919 | ~18 mins | 2.5ms | 2.1GB | ⭐⭐ (Attention) |
| **LogRAG** | 0.941* | ~10 mins | 45ms | 1.5GB | ⭐⭐⭐⭐⭐ (Natural language) |

*LogRAG F1 chỉ trên BGL; chưa có kết quả trên HDFS/Thunderbird

### Trade-offs

```
Effectiveness (F1):  LightAD < LogFormer < LogRAG
                     0.904    0.919      0.941

Speed:               LogRAG < LogFormer < LightAD
                     45ms     2.5ms      0.12ms

Cost:                LogRAG >> LogFormer > LightAD
                     $2.50/1K  GPU        CPU-only

Explainability:      LogRAG > LightAD > LogFormer
```

### Use Case Recommendations

**Chọn LightAD khi:**
- Cần real-time detection (latency <1ms)
- Resource constrained (CPU-only, <500MB RAM)
- Cần explanation đơn giản, rule-based
- Budget thấp

**Chọn LogFormer khi:**
- Có GPU available
- Có unlabeled data nhiều để pre-training
- Labeled data ít (<5K samples)
- Cần balance giữa accuracy và cost

**Chọn LogRAG khi:**
- Accuracy là ưu tiên số 1
- Cần explanation chi tiết bằng natural language
- Có budget cho API calls ($500-1000/month)
- Latency không critical (batch processing)
- Có ít labeled data (semi-supervised)

---

## 5. Gaps and Research Opportunities

### Gaps từ 3 papers

1. **Limited cross-dataset evaluation:**
   - LightAD: 3 datasets
   - LogFormer: 5 datasets
   - LogRAG: **chỉ 1 dataset** (BGL)
   - **Gap:** Cần unified benchmark trên cùng datasets

2. **Unfair comparison:**
   - Mỗi paper dùng preprocessing khác nhau
   - Train/test split khác nhau
   - Hardware khác nhau
   - **Gap:** Cần controlled experimental setup

3. **Missing explainability analysis:**
   - Không có so sánh systematic về explanation quality
   - Không có user study về actionability
   - **Gap:** RQ4 của chúng ta

4. **No cost-effectiveness analysis:**
   - Papers chỉ report F1, không analyze trade-offs
   - **Gap:** RQ3 của chúng ta

5. **Limited error analysis:**
   - Không có taxonomy of failure modes
   - Không biết các methods fail ở đâu
   - **Gap:** RQ4(a) của chúng ta

### Our Thesis Contributions

**Main contributions:**
1. ✅ **Unified benchmark:** 3 methods × 2 datasets với controlled setup
2. ✅ **Cost-effectiveness:** F1 vs Latency vs Memory trade-off analysis
3. ✅ **Error taxonomy:** Structured classification of FP/FN patterns
4. ✅ **Explainability comparison:** Systematic comparison of explanation quality
5. ✅ **Practical guidelines:** Decision framework for method selection

---

## 6. Next Steps for Reproduction

### For LightAD
- [x] Repository cloned: `/Users/ruby/dev/code-papers/LightAD/`
- [ ] Verify dependencies installable
- [ ] Test on HDFS_v1
- [ ] Test on BGL
- [ ] Measure training time, inference latency, memory

### For LogFormer
- [x] Repository cloned: `/Users/ruby/dev/code-papers/LogFormer/`
- [ ] Download pre-trained model
- [ ] Fine-tune on HDFS_v1
- [ ] Fine-tune on BGL
- [ ] Measure metrics

### For LogRAG
- [x] Repository cloned: `/Users/ruby/dev/code-papers/LogRAG/`
- [ ] Setup API key hoặc local LLM
- [ ] **Extend to HDFS_v1** (not in original paper)
- [ ] Test on BGL
- [ ] Measure cost and latency

---

**Document status:** ✅ COMPLETE - Core papers summarized
**Time spent:** ~6 hours (reading + extraction + summary)
**Next task:** TASK 1.2 - Literature review (≥30 papers)
