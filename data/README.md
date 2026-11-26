# Dataset Documentation

> **Purpose:** Document datasets used in thesis for reproducibility
> **Last updated:** 2026-11-26

---

## Datasets Overview

| Dataset | Source | Version | Size (raw) | Size (parsed) | Templates | Sessions/Blocks | Anomaly Rate |
|---------|--------|---------|------------|---------------|-----------|-----------------|--------------|
| **HDFS_v1** | LogHub | v1 | 1.5 GB | 51 MB | 29 | 575,061 | 2.9% |
| **BGL** | LogHub | v1 | 709 MB | TBD | ~377 | TBD | 0.4% |

---

## 1. HDFS_v1 (Hadoop Distributed File System)

### 1.1 Source Information

- **Origin:** Hadoop Distributed File System logs
- **Collection period:** 2008 (38 hours)
- **System:** Production Hadoop cluster (203 nodes)
- **LogHub URL:** https://zenodo.org/record/8196385
- **Version:** v1 (original release, not v2 or v3)

### 1.2 Data Characteristics

**Raw logs:**
- **File:** `data/raw/hdfs_v1/HDFS.log`
- **Size:** 1.5 GB
- **Total lines:** 11,175,629 log lines
- **Format:** `<Date> <Time> <Pid> <Level> <Component>: <Content>`

**Example log line:**
```
081109 203518 148 INFO dfs.DataNode$PacketResponder: Received block blk_-1608999687919862906 of size 67108864 from /10.250.10.6
```

**Parsed/Preprocessed:**
- **Location:** `data/raw/hdfs_v1/preprocessed/`
- **Files:**
  - `HDFS.log_templates.csv`: 29 unique log templates (EventId E1-E29)
  - `Event_occurrence_matrix.csv`: Block × Template count matrix
  - `Event_traces.csv`: Block → Event sequence mapping
  - `anomaly_label.csv`: 575,061 blocks with labels (0=normal, 1=anomaly)
  - `HDFS.npz`: Numpy compressed features

### 1.3 Labeling Strategy

**Type:** Fault injection study
- **Normal blocks:** Logs collected during healthy operation
- **Anomaly blocks:** Logs containing events triggered by injected faults
  - HDFS node failures
  - Disk errors
  - Network partitions
  - Data corruption

**Anomaly rate:** 2.9% (16,838 anomalous blocks out of 575,061)

**Label format (`anomaly_label.csv`):**
```csv
BlockId,Label
blk_-1608999687919862906,Normal
blk_-1026395186347067408,Anomaly
...
```

### 1.4 Session Grouping

**Key concept:** Logs grouped by **BlockId**

Each block represents a workflow:
1. Client requests block write
2. DataNode receives block
3. Block written to disk
4. Replication to other nodes
5. Acknowledgment sent

**Implication:** 
- Anomaly detection at **block level**, not individual log line
- One block = one classification instance
- 575,061 blocks → 575,061 classification instances

### 1.5 Template Statistics

**Total templates:** 29

**Top 5 most frequent templates:**
| EventId | Template | Frequency |
|---------|----------|-----------|
| E5 | Receiving block [*] src: [*] dest: [*] | ~15% |
| E22 | Received block [*] of size [*] from [*] | ~12% |
| E23 | Verification succeeded for [*] | ~11% |
| E9 | Served block [*] to [*] | ~10% |
| E11 | PacketResponder [*] for block [*] terminating | ~8% |

**Rare templates:** E1, E2, E3 (<0.1% each) - often associated with anomalies

### 1.6 Data Splits

**Current state:** Full dataset available, need to split

**Planned split (80/10/10):**
- **Train:** 460,049 blocks (80%)
- **Validation:** 57,506 blocks (10%)
- **Test:** 57,506 blocks (10%)

**Strategy:** Stratified by label to preserve anomaly rate

---

## 2. BGL (BlueGene/L Supercomputer)

### 2.1 Source Information

- **Origin:** BlueGene/L supercomputer at Lawrence Livermore National Lab
- **Collection period:** 2005 (214 days)
- **System:** 128K-processor supercomputer
- **LogHub URL:** https://zenodo.org/record/8196385
- **Version:** v1

### 2.2 Data Characteristics

**Raw logs:**
- **File:** `data/raw/bgl/BGL.log`
- **Size:** 709 MB
- **Total lines:** 4,747,963 log lines
- **Format:** `- <Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>`

**Example log line:**
```
- 2005.06.03 R02-M1-N0-C:J12-U01 2005-06-03-15.42.50.675872 R02-M1-N0-C:J12-U01 RAS KERNEL FATAL data storage interrupt
```

**Parsed/Preprocessed:**
- **Location:** TBD - Need to run Drain parser
- **Expected templates:** ~377 (from literature)

### 2.3 Labeling Strategy

**Type:** Natural errors (production system)
- **Normal logs:** INFO, WARNING levels
- **Anomaly logs:** ERROR, FATAL, SEVERE levels

**Anomaly rate:** 0.4% (much lower than HDFS)

**Label extraction:** Based on log level field (column 8)

### 2.4 Session Grouping

**Key difference from HDFS:** No natural session ID (like BlockId)

**Strategy:** Time-based windowing
- **Window size:** 20 seconds (from literature)
- **Sliding:** 10 seconds overlap
- **Labeling:** Window is anomalous if ANY log in it is anomalous

**Implication:**
- More arbitrary than HDFS block-based
- Need to tune window size on validation set

### 2.5 Template Statistics

**Expected:** ~377 unique templates (much more diverse than HDFS)

**Reason for high diversity:**
- Multiple subsystems (RAS, APP, KERNEL, etc.)
- Multiple severity levels
- Longer observation period (214 days vs 38 hours)

### 2.6 Data Splits

**Strategy:** Chronological split (not random!)
- **Reason:** Temporal validity - test on future data
- **Train:** First 80% chronologically
- **Validation:** Next 10%
- **Test:** Last 10%

**No shuffling:** Preserves temporal order

---

## 3. Data Preprocessing Pipeline

### 3.1 For HDFS_v1 (Already done)

```bash
# Already preprocessed, available at:
data/raw/hdfs_v1/preprocessed/
```

**What was done:**
1. ✅ Drain parsing: Extract 29 templates
2. ✅ BlockId extraction: Group logs by block
3. ✅ Feature extraction: Event count matrix
4. ✅ Labeling: Map blocks to normal/anomaly

### 3.2 For BGL (TODO - Task 1.6)

```python
# Script to create: scripts/parse_logs.py
from drain3 import TemplateMiner
import pandas as pd

# 1. Parse BGL logs with Drain
# 2. Extract timestamps and labels
# 3. Create time-based windows
# 4. Generate event sequences per window
# 5. Save structured output
```

---

## 4. Data Quality Checks

### 4.1 HDFS_v1 Validation

- [x] File integrity: SHA256 checksum verified
- [x] Template count: 29 (expected range: 20-50 ✓)
- [x] Block count: 575,061 (matches literature ✓)
- [x] Anomaly rate: 2.9% (matches literature ✓)
- [x] No missing values in labels
- [x] BlockId unique and complete

### 4.2 BGL Validation (TODO)

- [ ] File integrity: Checksum
- [ ] Parse without errors
- [ ] Template count ~377
- [ ] Anomaly rate ~0.4%
- [ ] Timestamps valid and monotonic

---

## 5. Data Usage in Experiments

### 5.1 Training Phase

**HDFS_v1:**
- Use `Event_occurrence_matrix.csv` for feature vectors
- Use `Event_traces.csv` for sequence modeling
- Use `anomaly_label.csv` for labels

**BGL:**
- After parsing, generate similar files
- Window-based features

### 5.2 Evaluation Phase

**Metrics computed per dataset:**
- Precision, Recall, F1-score
- PR-AUC (Precision-Recall Area Under Curve)
- FPR (False Positive Rate)

**Cross-dataset comparison:**
- Compare methods on HDFS (block-based, injected faults)
- Compare methods on BGL (time-based, natural errors)
- Analyze: Which method generalizes better?

---

## 6. Known Issues and Limitations

### 6.1 HDFS_v1

**Limitations:**
1. **Synthetic anomalies:** Injected faults may not reflect real production failures
2. **Short duration:** 38 hours may not cover all failure modes
3. **Small template diversity:** Only 29 templates (simpler than real systems)

**Mitigation:**
- Complement with BGL (natural errors)
- Acknowledge in Threats to Validity (Chapter 5)

### 6.2 BGL

**Limitations:**
1. **Old data:** From 2005 (may not reflect modern systems)
2. **Specific architecture:** BlueGene/L (not typical cloud workload)
3. **Window size sensitivity:** Arbitrary 20-second window

**Mitigation:**
- Standard benchmark in literature (comparable to prior work)
- Tune window size on validation set
- Document sensitivity analysis

---

## 7. Data Governance

### 7.1 Licensing

**Both datasets:**
- **Source:** LogHub (public research dataset)
- **License:** MIT License (permissive)
- **Citation required:** Yes - cite LogHub paper (Zhu et al. 2023)

### 7.2 Privacy

**No PII (Personally Identifiable Information):**
- HDFS: Only BlockIds (hashed), IP addresses (internal), no usernames
- BGL: Only node IDs, no user data

**Safe for research:** ✓

### 7.3 Redistribution

**Our policy:**
- Do NOT redistribute raw data (cite LogHub instead)
- CAN redistribute preprocessed/derived features
- MUST provide scripts to reproduce from LogHub

---

## 8. References

**Primary dataset paper:**
```bibtex
@inproceedings{zhu2023loghub,
  title={A Data Collection for Evaluating the Performance of Log Parsers},
  author={Zhu, Jieming and Liu, Shilin and He, Pinjia and Zhang, Qi and Lyu, Michael R.},
  booktitle={2023 IEEE 34th International Symposium on Software Reliability Engineering (ISSRE)},
  year={2023},
  organization={IEEE},
  note={Zenodo: https://zenodo.org/record/8196385}
}
```

**HDFS original paper:**
```bibtex
@inproceedings{xu2009detecting,
  title={Detecting Large-Scale System Problems by Mining Console Logs},
  author={Xu, Wei and Huang, Ling and Fox, Armando and Patterson, David and Jordan, Michael},
  booktitle={ACM SOSP},
  year={2009}
}
```

**BGL original source:**
```
Oliner, A., & Stearley, J. (2007). What Supercomputers Say: A Study of Five System Logs. 
37th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN'07).
```

---

**Document status:** ✅ HDFS_v1 documented, BGL partial (pending parsing)
**Last updated:** 2026-11-26 15:50
**Next task:** Parse BGL logs (Task 1.6)
