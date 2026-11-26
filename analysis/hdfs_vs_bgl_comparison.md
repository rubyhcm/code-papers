# HDFS_v1 vs BGL: Detailed Comparison

> **Purpose:** Deep analysis of differences between two datasets for thesis
> **Last updated:** 2026-11-26 16:24

---

## Executive Summary

HDFS_v1 and BGL represent **two extremes** in the log anomaly detection landscape:

| Dimension | HDFS_v1 | BGL | Winner for Testing |
|-----------|---------|-----|-------------------|
| **Simplicity** | ⭐⭐⭐⭐⭐ Simple | ⭐ Complex | HDFS (easier baseline) |
| **Realism** | ⭐⭐ Synthetic | ⭐⭐⭐⭐⭐ Natural | BGL (production-like) |
| **Structure** | ⭐⭐⭐⭐⭐ Well-defined sessions | ⭐ Ad-hoc windows | HDFS (cleaner) |
| **Diversity** | ⭐ Low (29 templates) | ⭐⭐⭐⭐⭐ High (1,775) | BGL (challenging) |
| **Imbalance** | ⭐⭐⭐⭐⭐ Severe (1:33) | ⭐⭐⭐ Moderate (1:7) | HDFS (tests robustness) |

**Complementarity:** Together, they provide **comprehensive coverage** of LogAD challenges.

---

## 1. System Characteristics

### 1.1 Origin

**HDFS_v1:**
- **System:** Hadoop Distributed File System (version 1.0)
- **Scale:** 203-node cluster
- **Workload:** MapReduce jobs (sorting, word count)
- **Period:** 38 hours of operation
- **Year:** 2008

**BGL:**
- **System:** BlueGene/L supercomputer at Lawrence Livermore National Lab
- **Scale:** 128K processors
- **Workload:** Scientific computing (simulations)
- **Period:** 214 days of operation
- **Year:** 2005

### 1.2 Architecture Differences

```
HDFS (Distributed File System):
┌─────────────┐
│ NameNode    │ ← Coordinates
└─────────────┘
       │
  ┌────┴────┬────────┬────────┐
  │         │        │        │
┌─▼───┐   ┌─▼───┐  ┌─▼───┐  ...
│DN 1 │   │DN 2 │  │DN 3 │  
└─────┘   └─────┘  └─────┘
 (203 nodes)

Logs: Operations on blocks (read, write, replicate)

BGL (Supercomputer):
┌──────────────────────────────────┐
│  128K Processors (Tightly Coupled)│
└──────────────────────────────────┘
       │
  ┌────┴────┬────────┬────────┐
  │         │        │        │
 RAS    APP/MPI   KERNEL   Other
(Logs from multiple subsystems)

Logs: Hardware errors, app failures, kernel panics
```

**Implication:**
- **HDFS:** Workflow-oriented (block operations have clear start/end)
- **BGL:** Event-oriented (independent hardware/software events)

---

## 2. Log Format & Structure

### 2.1 Raw Log Format

**HDFS_v1:**
```
<Date> <Time> <Pid> <Level> <Component>: <Content>
081109 203518 148 INFO dfs.DataNode$PacketResponder: Received block blk_-1608999687919862906 of size 67108864 from /10.250.10.6
│      │       │   │    │                            │
Date   Time   PID Level Component                   Free-text content
```

**Fields:** 6 (highly structured prefix)

**BGL:**
```
- <Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>
- 2005.06.03 R02-M1-N0-C:J12-U01 2005-06-03-15.42.50.675872 R02-M1-N0-C:J12-U01 RAS KERNEL FATAL data storage interrupt
│ │          │                    │                          │                    │   │      │     │
- Label      Timestamp            Date                        NodeRepeat           Type Comp  Level Content
```

**Fields:** 10 (more complex, redundant fields)

### 2.2 Parsing Complexity

| Aspect | HDFS_v1 | BGL |
|--------|---------|-----|
| **Regex complexity** | Simple (5 groups) | Complex (9 groups) |
| **Field redundancy** | Low | High (Node appears 2x, Date 2x) |
| **Drain success rate** | ~100% | ~92% (8% parse errors) |
| **Template extraction** | Easy (clear structure) | Harder (variable formats) |

**Example parsing result:**

```python
# HDFS (clean)
{
  'Date': '081109',
  'Time': '203518',
  'Level': 'INFO',
  'Component': 'dfs.DataNode$PacketResponder',
  'Content': 'Received block <*> of size <*> from <*>'
}

# BGL (messier)
{
  'Date': '2005.06.03',  # First occurrence
  'Timestamp': 'R02-M1-N0-C:J12-U01',  # Actually a node ID
  'Time': '2005-06-03-15.42.50.675872',  # Second date+time
  'Node': 'R02-M1-N0-C:J12-U01',  # Duplicate
  'Level': 'FATAL',
  'Content': 'data storage interrupt'
}
```

---

## 3. Labeling Strategy

### 3.1 Anomaly Generation

**HDFS_v1: Fault Injection**

**Method:**
1. Run healthy workload → Collect normal logs
2. Inject faults:
   - Kill DataNode processes
   - Corrupt disk blocks
   - Network partitions
   - Disk full errors
3. Collect logs during failures → Label as anomalies

**Pros:**
- ✅ **Clean labels:** Know exactly when anomaly occurs
- ✅ **Controlled:** Can inject specific failure types
- ✅ **Reproducible:** Can re-run same faults

**Cons:**
- ❌ **Synthetic:** May not reflect real production failures
- ❌ **Limited diversity:** Only injected failure modes
- ❌ **Detection bias:** Models may "memorize" injected patterns

**BGL: Natural Errors**

**Method:**
1. Collect all logs from production system (214 days)
2. Extract labels from log level field:
   - FATAL, SEVERE, ERROR → Anomaly
   - WARNING, INFO → Normal
3. No human verification

**Pros:**
- ✅ **Realistic:** Actual production failures
- ✅ **Diverse:** 214 days → Many failure modes
- ✅ **Unbiased:** No synthetic patterns

**Cons:**
- ❌ **Noisy labels:** Log level may not equal anomaly
  - Example: "ERROR: Retrying connection" (normal behavior)
- ❌ **Ground truth unclear:** No oracle for correctness
- ❌ **Imbalanced:** Our parsing shows 12% anomaly (too high?)

### 3.2 Label Quality

**HDFS_v1:**
- **Precision:** High (~99%) - Fault injection = clear anomaly
- **Recall:** High (~99%) - All injected faults logged
- **Confidence:** ⭐⭐⭐⭐⭐ (5/5)

**BGL:**
- **Precision:** Medium (~80%?) - Some ERRORs are normal
- **Recall:** Medium (~70%?) - Some anomalies may not be FATAL
- **Confidence:** ⭐⭐⭐ (3/5)

**Our BGL issue (12% vs 0.4%):**
- **Hypothesis:** Original paper used stricter criteria (only specific error codes)
- **Our approach:** Mark all FATAL/ERROR as anomaly (too aggressive)
- **Action needed:** Review and potentially adjust

---

## 4. Session Grouping

### 4.1 HDFS: Block-Based Sessions

**Natural grouping by BlockId:**

```
Block blk_123:
  Log 1: "Receiving block blk_123 from client"
  Log 2: "Wrote block blk_123 to disk"
  Log 3: "Replicating block blk_123 to DN2"
  Log 4: "Replicating block blk_123 to DN3"
  Log 5: "Block blk_123 replicated successfully"
  → ONE SESSION (5 events)

Label: Anomaly if ANY event in session is anomalous
```

**Characteristics:**
- **Natural semantics:** Block = unit of work
- **Clear boundaries:** Session starts/ends with block lifecycle
- **Variable length:** 2-298 events (mean 19.4)
- **No overlap:** Each log belongs to exactly one block

**Advantages:**
- ✅ Semantically meaningful
- ✅ No arbitrary parameters (window size)
- ✅ Aligns with system design

**Disadvantages:**
- ❌ Not generalizable (most systems don't have BlockId)

### 4.2 BGL: Time-Window Sessions

**Arbitrary windowing (from literature):**

```
Time window (20 seconds):
  [10:00:00] Log 1: "Process started"
  [10:00:05] Log 2: "Memory allocated"
  [10:00:10] Log 3: "FATAL: Segmentation fault"
  [10:00:15] Log 4: "Process terminated"
  → ONE WINDOW (4 events)

Label: Anomaly if ANY event in window is anomalous
```

**Parameters:**
- **Window size:** 20 seconds (from DeepLog paper)
- **Sliding:** 10 seconds overlap (50%)
- **Why 20s?** Arbitrary heuristic (not from domain knowledge)

**Characteristics:**
- **No natural semantics:** 20s has no meaning in BGL
- **Arbitrary boundaries:** Events at 19.9s and 20.1s in different windows
- **Variable length:** Depends on log rate (fluctuates)

**Advantages:**
- ✅ Generalizable to any log data
- ✅ Standard approach in literature

**Disadvantages:**
- ❌ Arbitrary parameters (window size, overlap)
- ❌ Sensitive to log rate (high load = long windows)
- ❌ May split related events across windows

**Parameter sensitivity:**
- Window = 10s: Too short, miss context
- Window = 60s: Too long, dilute anomaly signal
- Window = 20s: "Goldilocks" (empirically works)

---

## 5. Template Diversity

### 5.1 HDFS: Low Diversity (29 templates)

**Distribution:**

| Template ID | Occurrences | Percentage | Example |
|-------------|-------------|------------|---------|
| E5 | 1,723,232 | 15.4% | "Receiving block <*> from <*>" |
| E26 | 1,719,741 | 15.4% | "BLOCK* NameSystem <*> addStoredBlock" |
| E11 | 1,706,679 | 15.3% | "PacketResponder <*> terminating" |
| ... | ... | ... | ... |
| E24 | 57 | 0.0005% | "Adding an already existing block" |

**Characteristics:**
- **Top 5 templates:** ~75% of logs
- **Bottom 10 templates:** <1% of logs
- **Power law distribution:** Few templates dominate

**Why so few?**
1. **Short duration:** 38 hours → Limited code paths executed
2. **Simple operations:** Block read/write/replicate
3. **Controlled workload:** Only MapReduce jobs

**Implication for ML:**
- **Easy to learn:** 29 patterns memorizable
- **Low complexity:** Small feature space (29 dimensions)
- **High redundancy:** Most logs from same 5 templates

### 5.2 BGL: High Diversity (1,775 templates)

**Distribution:**

| Template ID | Occurrences | Percentage | Example |
|-------------|-------------|------------|---------|
| E3 | 1,706,751 | 39.1% | "generating <*>" |
| E551 | 442,966 | 10.1% | "iar <*> dear <*>" |
| E11 | 295,764 | 6.8% | "<*> double-hummer alignment exceptions" |
| ... | ... | ... | ... |
| E1700-E1775 | 1 each | <0.00001% | Various rare errors |

**Characteristics:**
- **Top 1 template:** ~39% of logs (less dominant than HDFS)
- **889 templates:** Only 1 occurrence (singletons)
- **Extreme long tail:** 50% of templates appear <10 times

**Why so many?**
1. **Long duration:** 214 days → Diverse failure modes
2. **Complex system:** Multiple subsystems (RAS, APP, KERNEL)
3. **Hardware errors:** Thousands of unique hardware failure messages

**Implication for ML:**
- **Hard to learn:** 1,775 patterns difficult to memorize
- **High complexity:** Large feature space (1,775 dimensions)
- **Sparse data:** Most templates rarely seen

---

## 6. Anomaly Characteristics

### 6.1 Anomaly Rate

**HDFS_v1: 2.93% (1:33 imbalance)**
- **Interpretation:** ~3 out of 100 blocks are anomalous
- **Severity:** High imbalance (ML challenge)
- **Consistency:** Uniform across dataset (controlled injection)

**BGL: 12.08% (1:7 imbalance) ⚠️**
- **Interpretation:** ~12 out of 100 logs are anomalous
- **Issue:** Expected 0.4% from literature (30x higher!)
- **Hypothesis:** Our label extraction too aggressive
- **Impact:** Less imbalanced → Easier for ML (but inconsistent with literature)

### 6.2 Anomaly Types

**HDFS_v1:**
- **Block corruption:** Checksum mismatch
- **Node failure:** DataNode crash
- **Network partition:** Cannot reach NameNode
- **Disk full:** Cannot write block

**All well-defined, reproducible failure modes.**

**BGL:**
- **Hardware errors:** Memory parity, link card errors
- **Software errors:** Kernel panics, segmentation faults
- **Application errors:** MPI failures, job crashes
- **System errors:** File system corruption, driver errors

**Diverse, one-off, production failures.**

### 6.3 Implications for Detectability

**HDFS (easier):**
- Clear patterns: "Block X checksum failed" → Always anomaly
- Consistent: Same fault type has same log pattern
- Low noise: Fault injection = clean signal

**Expected detection F1: 0.90-0.96** (all methods likely work)

**BGL (harder):**
- Ambiguous patterns: "ERROR: Retry connection" → Maybe normal
- Inconsistent: Same failure may have different log patterns
- High noise: Production = noisy labels

**Expected detection F1: 0.85-0.94** (larger method differences)

---

## 7. Implications for Our 4 Research Questions

### RQ1: Detection Effectiveness

**Hypothesis:**
- **HDFS:** Small performance gaps (all methods ~0.92-0.96)
  - Reason: Simple, 29 templates, clear patterns
- **BGL:** Larger gaps (0.88 → 0.92 → 0.94)
  - Reason: Complex, 1,775 templates, ambiguous patterns
  - LLM reasoning advantage clearer here

**Key comparison:**
- Do methods generalize from HDFS (simple) to BGL (complex)?
- Or does each method have dataset-specific strengths?

### RQ2: Computational Cost

**Dataset complexity impact:**
- **HDFS (29 templates):**
  - LightAD: Very fast (small feature space)
  - LogFormer: Fast (short sequences)
  - LogRAG: Moderate (fewer retrievals)

- **BGL (1,775 templates):**
  - LightAD: May slow down (large feature space)
  - LogFormer: Same (transformer scales well)
  - LogRAG: Slower (more complex retrievals)

**Metric:** Measure latency/throughput on both datasets → Assess scalability

### RQ3: Trade-offs

**Different optimal methods per dataset:**
- **HDFS:** LightAD likely sufficient (simple data, why pay for complexity?)
- **BGL:** LogFormer/LogRAG may be necessary (complex data, worth the cost)

**Decision framework:**
- If your logs are like HDFS (simple, structured) → Use LightAD
- If your logs are like BGL (complex, diverse) → Consider LogFormer/LogRAG

### RQ4: Explainability & Errors

**Expected error patterns:**

**HDFS:**
- **FP:** Short sequences (<5 events) → Insufficient context
- **FN:** Rare anomaly types (imbalance) → Never seen in training

**BGL:**
- **FP:** Ambiguous errors ("ERROR" that's normal) → Labeling noise
- **FN:** Unseen templates (singletons) → Novel failure modes

**Explainability:**
- **HDFS:** Decision tree rules likely clear (simple patterns)
- **BGL:** LLM reasoning likely needed (semantic understanding)

---

## 8. Recommendations for Thesis

### 8.1 Experimental Protocol

**Use BOTH datasets (not just one):**
- **HDFS:** Establish baseline on simple data
- **BGL:** Test generalization to complex data

**Report results separately:**
```
Table: RQ1 Results

| Method | HDFS F1 | BGL F1 | Average | Gap |
|--------|---------|--------|---------|-----|
| LightAD | 0.95 | 0.88 | 0.915 | 0.07 |
| LogFormer | 0.96 | 0.92 | 0.940 | 0.04 |
| LogRAG | 0.96 | 0.94 | 0.950 | 0.02 |
```

**Key insight:** Which method has smallest gap? (Best generalization)

### 8.2 Addressing BGL Label Issue

**Options:**
1. **Use as-is (12%):** Document difference, justify as "stricter threshold"
2. **Re-label:** Use original LogHub labels (if available)
3. **Adjust threshold:** Only mark FATAL (not ERROR) as anomaly

**Recommended:** Option 2 (use official labels) → Comparable to literature

### 8.3 Discussion Points (Chapter 5)

**HDFS-specific insights:**
- "On simple, structured logs (HDFS), all methods perform well (F1 > 0.90)"
- "Session-based grouping (BlockId) enables clear anomaly detection"

**BGL-specific insights:**
- "On complex, diverse logs (BGL), transformer/LLM methods show clear advantage"
- "High template diversity (1,775) challenges classical ML feature extraction"

**Cross-dataset insights:**
- "Method X generalizes better (small HDFS-BGL gap)"
- "Method Y specializes (high F1 on HDFS, drops on BGL)"

---

## 9. Threats to Validity

### 9.1 Internal Validity

**Threat:** Different preprocessing for HDFS vs BGL
- **HDFS:** Pre-processed by LogHub (Drain already run)
- **BGL:** We ran Drain ourselves
- **Mitigation:** Use same Drain config for both (sim_th=0.4)

**Threat:** Different label quality
- **HDFS:** High-quality (fault injection)
- **BGL:** Lower quality (log level heuristic)
- **Mitigation:** Acknowledge in limitations, report label noise

### 9.2 External Validity

**Threat:** Limited to 2 datasets
- **Generalization:** Results may not apply to modern cloud logs
- **Mitigation:** Choose complementary datasets (HDFS simple, BGL complex)

**Threat:** Old data (2005-2008)
- **Relevance:** May not reflect modern systems
- **Mitigation:** Standard benchmarks in literature (comparable to prior work)

---

## 10. Summary Table

| Aspect | HDFS_v1 | BGL | Complementarity |
|--------|---------|-----|-----------------|
| **Complexity** | Simple (29 templates) | Complex (1,775) | ✅ Cover spectrum |
| **Realism** | Synthetic (fault injection) | Natural (production) | ✅ Both evaluation modes |
| **Structure** | Workflow (block-based) | Event (time-based) | ✅ Different grouping strategies |
| **Imbalance** | Severe (1:33) | Moderate (1:7) ⚠️ | ✅ Test robustness |
| **Duration** | Short (38h) | Long (214d) | ✅ Different coverage |
| **Labeling** | Clean (injected) | Noisy (heuristic) | ✅ Test noise robustness |

**Conclusion:** HDFS and BGL are **highly complementary** for comprehensive benchmarking.

---

**Last updated:** 2026-11-26 16:28  
**Status:** ✅ COMPLETE - Detailed comparison done  
**Next:** Tasks 1.10-11 (Draft Chapters 1-2)
