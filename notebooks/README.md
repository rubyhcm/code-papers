# Kaggle Notebooks — LogAD Benchmark

Ba notebooks để train/validate/test trên Kaggle GPU.  
Tất cả đều **clone code từ** `https://github.com/rubyhcm/code-papers`.

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

```
git clone https://github.com/rubyhcm/code-papers → LightAD/
↓
preprocess.py --dataset hdfs/bgl
↓
main_hdfs.py --model knn/dt/slfn
main_super.py --dataset bgl
↓
parse logs → lightad_results.json
```

- CPU-compatible, ~30-60 phút (full HDFS)

---

## Notebook 2: LogFormer

```
git clone → LogFormer/
↓
parse_log.py (Drain)
↓
preprocess/preprocess_bgl.py + preprocess_hdfs.py (SentenceTransformer)
↓
train_transformer.py --log_name BGL/HDFS
↓
tune_transformer.py --tune_mode adapter
↓
parse result/ → logformer_results.json
```

- **GPU required** (T4 hoặc P100)
- ~2-4 giờ (10 pre-train + 20 tune epochs)
- Tăng `PRE_EPOCHS`/`TUNE_EPOCHS` cho kết quả tốt hơn

---

## Notebook 3: LogRAG

```
git clone → LogRAG/
↓
Drain parse → dataset/BGL/bgl-example.log_structured.csv
↓
SentenceTransformer encoder → pretrained/
↓
config.yaml (device, epochs, API key, RAG params)
↓
python main.py
  ├── DeepSVDD train (normal logs only)
  ├── anomaly candidates → output/anomaly_logs_detc_by_svdd.csv
  └── RAG post-process (FAISS + LLM verify)
↓
lograg_results.json
```

- **GPU required**
- OpenAI API key (optional) → thêm vào Kaggle Secrets tên `OPENAI_API_KEY`
- Không có key → RAG bị disable, chỉ chạy DeepSVDD
- Local LLM: set `USE_LOCAL_LLM = True` (cần ~14GB VRAM)

---

## Output Files

Download từ `/kaggle/working/`:

```
lightad_results/
├── lightad_results.json
└── lightad_results.png

logformer_results/
├── logformer_results.json
├── logformer_results.png
└── logformer_curves.png

lograg_results/
├── lograg_results.json
└── lograg_results.png
```

Copy vào `results/` của repo để tích hợp vào Chapter 4.
