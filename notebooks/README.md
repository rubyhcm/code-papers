# Kaggle Notebooks — LogAD Benchmark

Ba notebooks để train/validate/test trên Kaggle GPU.

## Notebooks

| File | Method | GPU | LLM key |
|---|---|---|---|
| `01_lightad_benchmark.ipynb` | LightAD (KNN / DT / SLFN) | Optional | No |
| `02_logformer_benchmark.ipynb` | LogFormer (Transformer + Adapter) | Required | No |
| `03_lograg_benchmark.ipynb` | LogRAG (DeepSVDD + RAG + LLM) | Required | Optional |

---

## Kaggle Dataset Setup

Upload 3 files vào **một Kaggle Dataset** tên `logad-data`:

```
logad-data/
├── hdfs/
│   ├── HDFS.log           (~2.7 GB)
│   └── anomaly_label.csv  (~12 MB)
└── bgl/
    └── BGL.log            (~1.8 GB)
```

Download nguồn: https://zenodo.org/record/8196385

---

## Notebook 1: LightAD

- Chạy trên CPU (không cần GPU)
- 3 models: KNN, Decision Tree, SLFN
- 5-fold HDFS + single-run BGL
- Output: `lightad_results.json`, 2 plots

**Expected runtime:** ~30-60 phút (CPU, full HDFS)

---

## Notebook 2: LogFormer

- **Cần GPU** (T4 hoặc P100)
- Pipeline: Drain parse → SentenceTransformer embed → Transformer pre-train → Adapter tune
- Output: `logformer_results.json`, training curves

**Expected runtime:** ~2-4 giờ (GPU T4, 5+10 epochs)

Tăng `PRE_EPOCHS` và `TUNE_EPOCHS` cho kết quả tốt hơn theo paper (10 + 20).

---

## Notebook 3: LogRAG

- **Cần GPU** (cho DeepSVDD + local LLM nếu dùng)
- **OpenAI API key** (optional — có fallback retrieval-only nếu không có key)
  - Add key vào Kaggle Secrets với tên `OPENAI_API_KEY`
  - Hoặc set `USE_LOCAL_LLM = True` để dùng Mistral-7B (cần ~14GB VRAM)
- Output: `lograg_results.json`, score distribution plot

**Expected cost (OpenAI):** ~$0.15 per run (500 LLM calls)  
**Expected runtime:** ~1-2 giờ

---

## Output Files

Sau khi chạy, download từ `/kaggle/working/`:

```
lightad_results/
├── lightad_results.json
├── lightad_results.png
└── lightad_runtime.png

logformer_results/
├── logformer_results.json
└── logformer_curves.png

lograg_results/
├── lograg_results.json
├── svdd_loss.png
├── svdd_scores.png
└── lograg_results.png
```

Copy vào `results/` của repo để tích hợp vào Chapter 4.
