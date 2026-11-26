# Environment Setup Guide

> **Last updated:** 2026-11-26  
> **Platform:** macOS (Apple Silicon / Intel) · Linux (GPU server for training)

---

## Overview

This project requires two environments:

| Environment | Purpose | Platform |
|---|---|---|
| `venv/` (local) | Development, preprocessing, analysis | macOS |
| GPU server | Training LogFormer, LogRAG | Linux + NVIDIA GPU |

---

## Local Setup (macOS)

### Prerequisites

- Python 3.10+ (tested with 3.15)
- pip 24+

### Quick Start

```bash
# 1. Clone repo
git clone https://github.com/rubyhcm/code-papers.git
cd code-papers

# 2. Create venv
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify
python scripts/verify_environment.py
```

### Installed Packages

| Package | Version | Purpose |
|---|---|---|
| torch | 2.15.0 | Deep learning (CPU on macOS) |
| transformers | 5.x | LogFormer, LogRAG pretrained models |
| scikit-learn | 1.9+ | LightAD classical ML |
| drain3 | 0.9.11 | Log parsing |
| pandas | 3.x | Data processing |
| numpy | 2.x | Numerical computation |
| matplotlib | 3.x | Visualization |
| seaborn | 0.13+ | Statistical plots |

---

## GPU Server Setup (Training)

### Requirements

- NVIDIA GPU (RTX 3090 or better recommended)
- CUDA 11.7+
- Python 3.8–3.10

### Setup

```bash
# Install PyTorch with CUDA
pip install torch==1.13.1 torchvision --index-url https://download.pytorch.org/whl/cu117

# Install remaining deps
pip install transformers==4.30.0 scikit-learn==1.3.0 drain3 pandas numpy matplotlib seaborn accelerate

# Verify GPU
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

---

## Project Repositories

The three method repositories are included in the project root:

| Repo | Path | Paper |
|---|---|---|
| LightAD | `LightAD/` | ICSE 2024 |
| LogFormer | `LogFormer/` | AAAI 2024 |
| LogRAG | `LogRAG/` | ISSRE 2024 |

Each repo has its own `requirements.txt`. Install within the shared venv or create separate envs if dependency conflicts arise.

---

## Data

Raw datasets are **not tracked in git** (too large). Download from LogHub:

```bash
# HDFS_v1
mkdir -p data/raw/hdfs_v1
# Download from: https://zenodo.org/record/8196385

# BGL
mkdir -p data/raw/bgl
# Download from: https://zenodo.org/record/8196385
```

Parsed outputs in `data/parsed/` are also excluded from git. Re-run:

```bash
python scripts/parse_bgl_logs.py
```

---

## Verification

```bash
source venv/bin/activate
python scripts/verify_environment.py
```

Expected output:

```
=== Environment Verification ===
✓ Python: 3.x.x
✓ PyTorch: 2.15.0
✓ Transformers: 5.x
✓ Scikit-learn: 1.9.x
✓ Drain3: 0.9.11
✓ Repo LightAD: LightAD/
✓ Repo LogFormer: LogFormer/
✓ Repo LogRAG: LogRAG/
All checks passed.
```

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'torch'`**  
→ Make sure venv is activated: `source venv/bin/activate`

**Torch CUDA not available on macOS**  
→ Expected. macOS uses CPU build. Run training on GPU server.

**LogRAG requires OpenAI API key**  
→ Set `export OPENAI_API_KEY=sk-...` or configure local LLM in `LogRAG/config.yaml`.
