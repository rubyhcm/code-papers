# Đặc Điểm Dữ Liệu Log Hệ Thống

> **Mục đích:** Hiểu sâu về bản chất dữ liệu log để thiết kế phương pháp phát hiện bất thường hiệu quả
> 
> **Nguồn:** LogHub (Zhu et al. 2023), Drain (He et al. 2017), Surveys

---

## 1. Định Nghĩa và Vai Trò

### 1.1 Log là gì?

**Log (System log / Event log):** Bản ghi tự động các sự kiện, trạng thái, và hoạt động của hệ thống phần mềm trong quá trình vận hành.

**Mục đích:**
- **Debugging:** Truy vết lỗi và tái hiện failure scenarios
- **Monitoring:** Giám sát health và performance của hệ thống
- **Auditing:** Tuân thủ compliance và security requirements
- **Diagnosis:** Root cause analysis khi có sự cố

**Ví dụ log line (HDFS):**
```
081109 203518 148 INFO dfs.DataNode$PacketResponder: Received block blk_-1608999687919862906 of size 67108864 from /10.250.10.6
```

Phân tích:
- **Timestamp:** `081109 203518 148` (Nov 09, 2008, 20:35:18.148)
- **Log level:** `INFO`
- **Component:** `dfs.DataNode$PacketResponder`
- **Message:** `Received block blk_-1608999687919862906 of size 67108864 from /10.250.10.6`

---

## 2. Đặc Điểm Chính của Dữ Liệu Log

### 2.1 Semi-Structured (Bán cấu trúc)

**Hybrid nature:** Logs kết hợp cả structured fields và free-text messages

```
[Timestamp] [Level] [Component] Free-text message with <variable> values
   ↑         ↑          ↑                      ↑
Structured part                        Unstructured part
```

**Ví dụ so sánh:**

| Log format | Structured? | Challenge |
|------------|-------------|-----------|
| **JSON logs** | High | Dễ parse nhưng hiếm trong legacy systems |
| **Syslog (RFC 5424)** | Medium | Standard format nhưng message vẫn free-text |
| **Application logs** | Low | Mỗi developer viết theo style riêng |
| **Console logs** | Very low | Không có format cố định |

**Implication cho LogAD:**
- Cannot directly use as tabular data (cần parsing trước)
- Free-text message chứa semantic info quan trọng
- Variables (IDs, IPs, paths) cần được extract thành parameters

---

### 2.2 Non-Stationary (Không dừng / Tiến hóa theo thời gian)

**Problem:** Log patterns thay đổi khi hệ thống evolve

#### 2.2.1 Template Drift

**Scenario:** Software update thêm/sửa log statements

**Example:**
```
Version 1.0:  "Starting service on port 8080"
Version 1.1:  "Starting service on port 8080 with TLS enabled"
                                             ^^^^^^^^^^^^^^^^^^
                                             New info added
```

**Impact:**
- Models trained on v1.0 coi v1.1 logs là "unseen" → false positive
- Need periodic retraining

#### 2.2.2 Semantic Drift

**Scenario:** Cùng template nhưng ý nghĩa thay đổi

**Example:**
```
Before migration: "Database connection timeout" → Anomaly (critical issue)
After migration:  "Database connection timeout" → Normal (expected retry behavior)
```

**Impact:**
- Supervised models với old labels không còn chính xác
- Need label refreshing

#### 2.2.3 Volume Fluctuation

**Scenario:** Log volume thay đổi theo load, time of day, events

**Example (e-commerce):**
```
Normal day:    10K logs/hour
Black Friday:  500K logs/hour (50x spike)
```

**Impact:**
- Fixed-window approaches break
- Need adaptive windowing

**Solution approaches:**
- **Online learning:** Update models incrementally
- **Robust methods:** LightAD's KNN, DT less sensitive to drift than overfitted DL
- **Template monitoring:** Track new templates separately

---

### 2.3 High-Velocity (Tốc độ cao)

**Scale:** Modern systems generate massive log volumes

| System | Logs/sec | Logs/day | Size/day |
|--------|----------|----------|----------|
| **Small app** | 10-100 | ~8M | 1-10 GB |
| **Microservices** | 1K-10K | ~850M | 100-1000 GB |
| **Cloud platform** | 100K-1M | ~86B | 10-100 TB |
| **Example: Azure** | ~1M | ~86B | ~100 TB |

**Challenges for LogAD:**

#### 2.3.1 Processing Latency
- **Requirement:** Real-time detection (<1s end-to-end)
- **Bottleneck:** 
  - Parsing: ~10K logs/sec (Drain)
  - Feature extraction: ~50K logs/sec
  - Model inference: Varies by method
    - LightAD (KNN): ~100K logs/sec
    - LogFormer: ~2K logs/sec
    - LogRAG: ~20 logs/sec (LLM bottleneck)

#### 2.3.2 Storage Cost
- **Raw logs:** ~100 TB/day → $3K/month on S3
- **Parsed logs:** ~20 TB/day → $600/month
- **Retention:** Typically 7-30 days

**Solution:** 
- Streaming processing (Kafka, Flink)
- Sampling (analyze 10% of logs)
- Tiered storage (hot/warm/cold)

---

### 2.4 Imbalanced (Mất cân bằng nghiêm trọng)

**Core challenge:** Anomalies cực kỳ hiếm

**Typical anomaly rates:**

| Dataset | Total logs | Anomaly rate | Imbalance ratio |
|---------|-----------|--------------|-----------------|
| **HDFS_v1** | 11.2M | 2.9% | 1:33 |
| **BGL** | 4.7M | 0.4% | 1:250 |
| **Thunderbird** | 211M | 0.02% | 1:5000 |
| **Spirit** | 272M | 0.01% | 1:10000 |

**Impact on models:**

#### 2.4.1 Metric Selection
❌ **Accuracy is misleading:**
```
BGL: 99.6% normal → Predict all "normal" → 99.6% accuracy!
                                           But 0% anomaly recall
```

✅ **Use imbalance-aware metrics:**
- **Precision / Recall / F1:** Explicitly measure anomaly detection
- **PR-AUC:** Area under Precision-Recall curve
- **ROC-AUC:** Less suitable (inflated by TN dominance)

#### 2.4.2 Training Strategy
- **Undersampling:** Remove normal samples
  - Pro: Balanced training
  - Con: Waste data

- **Oversampling:** Duplicate anomaly samples
  - Pro: Use all data
  - Con: Overfitting risk

- **Class weights:** Penalize misclassifying minority class
  ```python
  class_weight = {0: 1.0, 1: 250.0}  # For BGL
  ```

- **Threshold tuning:** Adjust decision threshold on validation set
  ```python
  # Default: threshold = 0.5
  # For BGL: threshold = 0.05 (favor recall)
  ```

#### 2.4.3 Evaluation Protocol
⚠️ **Never use test set for threshold tuning!**

Correct split:
```
Data → 80% Train | 10% Validation | 10% Test
                      ↓                 ↓
                  Tune threshold    Final evaluation
```

---

### 2.5 Contextual (Phụ thuộc ngữ cảnh)

**Key insight:** Một log event là normal hay anomaly phụ thuộc vào context

#### 2.5.1 Sequential Context

**Example:**
```
✓ Normal sequence:
    Start transaction → Lock resource → Update data → Release lock → Commit

✗ Anomalous sequence:
    Start transaction → Lock resource → Update data → Commit
                                                       ^^^^^^^
                                                 Missing "Release lock"!
```

**Implication:**
- Need sequence modeling (LSTM, Transformer)
- Cannot treat logs independently (BoW insufficient)

#### 2.5.2 Temporal Context

**Example:**
```
"High CPU usage" log:
    - During business hours (9am-5pm): Normal
    - During nighttime (3am):          Anomaly (unexpected workload)
```

**Implication:**
- Add temporal features: hour, day_of_week
- Time-aware windowing

#### 2.5.3 Session/Workflow Context

**Example (HDFS):**
```
Session for Block_123:
    Log 1: "Received block"
    Log 2: "Wrote block to disk"
    Log 3: "Replicated to 3 nodes"
    → If any step missing → Anomaly
```

**Implication:**
- Group logs by session (BlockID, RequestID, UserID)
- Anomaly detection at session level (not individual log)

---

## 3. Taxonomy of Log Formats

### 3.1 By Structure Level

| Type | Description | Example | Parsing Difficulty |
|------|-------------|---------|-------------------|
| **Structured** | Fixed fields, machine-readable | JSON, XML, CSV | Easy (regex) |
| **Semi-structured** | Fixed prefix + free-text | Syslog, Apache | Medium (Drain) |
| **Unstructured** | Arbitrary format | Console output | Hard (LLM?) |

### 3.2 By Domain

| Domain | Characteristics | Key Challenges |
|--------|-----------------|----------------|
| **System logs (OS)** | Kernel, driver events | Low-level, cryptic |
| **Application logs** | Business logic | High-level, verbose |
| **Network logs** | Firewall, router | IP/MAC addresses |
| **Security logs** | Auth, audit | Sensitive data, rare anomalies |
| **Distributed system** | Microservices, tracing | Correlation across services |

### 3.3 Examples từ LogHub

#### HDFS_v1 (Hadoop Distributed File System)
```
Format: <Date> <Time> <Pid> <Level> <Component>: <Content>
Example: 081109 203518 148 INFO dfs.DataNode$PacketResponder: Received block ...

Characteristics:
- Block-based: Logs grouped by BlockId
- Structured prefix
- 29 unique templates (low diversity)
- 2.9% anomaly (injected faults)
- Version: v1 (original LogHub release)
```

#### BGL (BlueGene/L Supercomputer)
```
Format: - <Date> <Time> <Level> <Component> <Content>
Example: - 2005.06.03 R02-M1-N0-C:J12-U01 2005-06-03-15.42.50.675872 R02-M1-N0-C:J12-U01 RAS KERNEL FATAL ...

Characteristics:
- Time-based windowing (no natural session)
- 377 templates (high diversity)
- 0.4% anomaly (natural errors)
- Alert codes: FATAL, ERROR, WARNING, INFO
```

---

## 4. Log Parsing Challenges

### 4.1 Parameter Extraction

**Problem:** Separate templates from parameters

**Example:**
```
Raw log 1: "User alice logged in from 192.168.1.1"
Raw log 2: "User bob logged in from 10.0.0.5"

Desired:
  Template:   "User <*> logged in from <*>"
  Parameters: ["alice", "192.168.1.1"], ["bob", "10.0.0.5"]
```

**Challenge:** Heuristic-based (regex, LCS) có thể sai

**Bad parse:**
```
Wrong template: "User alice logged in from <*>"
                      ^^^^^ Should be a parameter!
```

### 4.2 Template Evolution

**Problem:** New templates appear over time

**Statistic (from LogHub paper):**
- HDFS: 5-10% new templates per month
- BGL: 15-20% new templates per month

**Impact on anomaly detection:**
- **Conservative parser:** New template → New anomaly (false positive)
- **Aggressive parser:** Merge similar templates → Miss subtle anomalies

**Solution (Drain):**
- Similarity threshold: 0.5 (tune per dataset)
- Online mode: Update parse tree incrementally

### 4.3 Multi-line Logs

**Problem:** One log event spans multiple lines (e.g., stack trace)

**Example:**
```
ERROR: NullPointerException at line 42
    at com.example.MyClass.method(MyClass.java:42)
    at com.example.Main.main(Main.java:10)
```

**How to handle:**
- **Merge:** Treat as one log event
- **Keep separate:** Link via correlation ID
- **Drain limitation:** Assumes one line = one event

---

## 5. Implications for Our Study

### 5.1 For Data Preprocessing (Task 1.6)

Based on characteristics:

1. **Use Drain parser** (handles semi-structured well)
2. **Session grouping:**
   - HDFS: By BlockId (natural workflow)
   - BGL: By time window (no natural session)
3. **Handle new templates:**
   - Track template frequencies
   - Separate "seen" vs "unseen" in evaluation

### 5.2 For Method Design

| Characteristic | LightAD | LogFormer | LogRAG |
|----------------|---------|-----------|--------|
| **Semi-structured** | ✓ Template counting | ✓ Tokenization | ✓ Template text |
| **Non-stationary** | ✓ KNN adapts fast | △ Need retraining | ✓ Few-shot adapts |
| **High-velocity** | ✓ Fast inference | △ GPU needed | ✗ LLM slow |
| **Imbalanced** | ✓ Class weights | ✓ Focal loss | ✓ Semi-supervised |
| **Contextual** | △ Sequence features | ✓ Transformer | ✓ RAG examples |

**Key insight:**
- LightAD: Good for high-velocity, unstable systems
- LogFormer: Good for stable systems with GPU
- LogRAG: Good when explainability > speed

### 5.3 For Evaluation (RQ1-RQ4)

**Metric selection:**
- Primary: **F1, PR-AUC** (imbalance-aware)
- Secondary: **FPR** (false alarm rate - practical concern)
- Avoid: Accuracy (misleading)

**Baselines:**
- Must handle same characteristics
- Fair comparison: Same parser (Drain), same split

**Error analysis (RQ4):**
- Classify errors by root cause:
  - Unseen templates (non-stationary)
  - Short sequences (insufficient context)
  - Rare patterns (imbalance)

---

## 6. Best Practices from Literature

### 6.1 Data Splitting Protocol

**For HDFS (session-based):**
```python
# Group by BlockId first, THEN split
blocks = df.groupby('BlockId')
train_blocks, test_blocks = train_test_split(
    blocks, 
    test_size=0.2, 
    stratify=blocks['label'],  # Preserve anomaly rate
    random_state=42
)
```

✗ **Wrong:** Split log lines directly → Data leakage (same block in train/test)

**For BGL (time-based):**
```python
# Chronological split (temporal validity)
# First 80% for train, last 20% for test
# No shuffling!
train = df[:int(0.8 * len(df))]
test = df[int(0.8 * len(df)):]
```

✗ **Wrong:** Random split → Unrealistic (can't predict past from future)

### 6.2 Parser Configuration

**Drain parameters (from paper):**
- `depth`: 4 (default, works for most datasets)
- `st` (similarity threshold): 
  - HDFS: 0.5 (templates more stable)
  - BGL: 0.4 (templates more diverse)
- `maxChild`: 100

**Validation:**
- Manual inspection of top 20 templates
- Check: Parameters correctly extracted?
- Check: Similar logs merged?

---

## 7. Summary

### Core Characteristics

| Characteristic | Description | Challenge for LogAD |
|----------------|-------------|---------------------|
| **Semi-structured** | Structured + free-text | Need parsing |
| **Non-stationary** | Templates evolve | Need online learning |
| **High-velocity** | Millions logs/sec | Need fast inference |
| **Imbalanced** | <1% anomalies | Need balanced metrics |
| **Contextual** | Meaning depends on context | Need sequence modeling |

### Key Takeaways

1. **Logs ≠ Tabular data:** Cannot directly apply standard ML
2. **Parsing is critical:** Drain is current best practice
3. **Context matters:** Session/sequence/temporal grouping essential
4. **Imbalance is severe:** F1/PR-AUC mandatory
5. **Evolution is inevitable:** Robustness > accuracy in production

### For Our Thesis

**Research gap:**
- Most papers test on static datasets
- Our contribution: **Compare methods across characteristics**
  - Which method handles non-stationary better? (LightAD vs LogRAG?)
  - Which handles high-velocity better? (LightAD fast!)
  - Trade-offs?

**Experimental design:**
- Same parser (Drain) for all methods
- Same splits (reproduce)
- Measure not just F1 but also latency, memory (RQ2)

---

**Document status:** ✅ COMPLETE
**Time spent:** ~3 hours
**Next task:** TASK 1.4 - ACM Empirical Standards
