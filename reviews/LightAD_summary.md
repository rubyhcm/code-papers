# Deep Learning or Classical Machine Learning? An Empirical Study on Log-Based Anomaly Detection

## Metadata
- **Authors:** Boxi Yu, Jiayi Yao, Qiuai Fu, Zhiqing Zhong, Haotian Xie, Yaoliang Wu, Yuchi Ma, Pinjia He
- **Venue:** ICSE '24, April 14–20, 2024, Lisbon, Portugal
- **DOI/arXiv:** https://doi.org/10.1145/3597503.3623308
- **GitHub:** https://github.com/BoxiYu/LightAD

## Problem Statement
Investigates whether DL methods have advantages over simple ML methods in log anomaly detection, considering computational costs

## Method/Architecture
LightAD framework that compares simple algorithms (KNN, Decision Tree, SLFN) with DL methods (CNN, LogRobust, NeuralLog) using Bayesian optimization for hyperparameter tuning

## Datasets Used
- HDFS: 11.2M logs, 0.15% anomaly rate
- BGL: 4.7M logs, 7.3% anomaly rate
- Thunderbird: 10M subset, 3.5% anomaly rate
- Spirit: 8M subset, 9.6% anomaly rate
- Liberty: 10M subset, 32.6% anomaly rate

## Evaluation Metrics
Precision, Recall, F1-Score (L1-Score in paper), Training Time, Inference Time

## Key Results
- KNN achieves F1=0.9802 on BGL (better than NeuralLog's 0.9641)
- KNN trains 1,000-3,225× faster than NeuralLog
- Simple methods outperform DL on all 5 datasets
- On deduplicated HDFS: DT F1=0.9410 vs CNN F1=0.9244

## Limitations (as stated in paper)
- All public datasets from 2005-2009, possibly not representative of modern systems
- Only supervised models tested, not unsupervised (e.g., DeepLog)
- Large datasets use only 3.7-4.7% subsets

## Reproducibility Status
- **GitHub Repository:** Available at https://github.com/BoxiYu/LightAD
- **Status:** To be verified in Month 3
