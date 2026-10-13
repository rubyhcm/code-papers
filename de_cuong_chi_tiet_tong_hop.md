# ĐỀ CƯƠNG CHI TIẾT LUẬN VĂN THẠC SĨ (TỔNG HỢP)

---

## THÔNG TIN CHUNG

**Tên đề tài (Tiếng Việt):**
Đánh giá thực nghiệm các phương pháp phát hiện bất thường dựa trên dữ liệu log: Từ học máy cổ điển đến mô hình ngôn ngữ lớn

**Tên đề tài (Tiếng Anh):**
An Empirical Evaluation of Log-Based Anomaly Detection Methods: From Classical Machine Learning to Large Language Models

---

## CHƯƠNG 1: GIỚI THIỆU

### 1.1. Bối cảnh và động lực nghiên cứu

Các hệ thống phần mềm hiện đại — từ cụm phân tán (Hadoop, HDFS), siêu máy tính (BlueGene/L), đến hạ tầng đám mây (OpenStack) — liên tục sinh ra khối lượng log khổng lồ (hàng triệu dòng/ngày). Log là nguồn dữ liệu quan trọng bậc nhất để giám sát vận hành, phát hiện sự cố và bảo đảm an ninh hệ thống.

Phát hiện bất thường dựa trên log (*Log-Based Anomaly Detection — LogAD*) là bài toán tự động phân loại hoặc gắn cờ những bản ghi/chuỗi sự kiện bất thường nhằm rút ngắn thời gian phát hiện lỗi, giảm thiểu thời gian dừng dịch vụ và cảnh báo sớm cho đội vận hành (SRE).

Trong giai đoạn 2024–2025, bài toán LogAD chứng kiến sự bùng nổ với các xu hướng kỹ thuật rất khác nhau:

| Xu hướng | Đại diện | Điểm nổi bật |
|---|---|---|
| Học máy cổ điển được đánh giá lại | **LightAD** (ICSE'24) | KNN/DT/SLFN cho hiệu quả đáng ngạc nhiên |
| Học sâu tuần tự cải tiến | **LogFormer** (AAAI'24) | Pre-train + Adapter tuning trên Transformer |
| Transformer đa phương thức | **CoLog** (Sci. Reports 2025) | Collaborative Transformers + MHIA + MAL |
| Mạng nơ-ron đồ thị | **Logs2Graph** (ICSE'24 Companion) | OCDiGCN: One-Class Digraph Inception GCN |
| LLM + RAG bán giám sát | **LogRAG** (ISSRE'24) | DeepSVDD + RAG + LLM tái đánh giá |
| Thống kê cải tiến | **SemPCA** | PCA++ trên biểu diễn ngữ nghĩa log |

### 1.2. Vấn đề nghiên cứu và khoảng trống

Mỗi phương pháp thường được công bố với bộ dữ liệu, giao thức đánh giá, môi trường và cách tiền xử lý **riêng biệt**, dẫn đến khó khăn trong việc đối chiếu trực tiếp. Cụ thể:

1. **Thiếu giao thức đánh giá thống nhất:** Các nghiên cứu dùng cách chia dữ liệu, cách tính chỉ số và cách xử lý nhãn khác nhau.
2. **Chưa có benchmark đa họ kỹ thuật:** Chưa có đánh giá nào đặt **đồng thời cả năm họ kỹ thuật** (cổ điển, học sâu, Transformer đa phương thức, GNN, LLM/RAG) lên cùng một benchmark.
3. **Bỏ qua khả năng phát hiện sớm:** Hầu hết chỉ đo kết quả cuối chuỗi, không đánh giá hiệu quả khi chỉ có một phần chuỗi log.
4. **Chưa so sánh chi phí tính toán công bằng:** Đánh đổi giữa chi phí LLM/RAG (LogRAG) so với phương pháp nhẹ (LightAD, SemPCA) chưa được làm rõ.
5. **Độ ổn định giữa các bộ dữ liệu:** Chưa rõ phương pháp tốt trên HDFS có ổn định trên OpenStack/BGL hay không.
6. **Thiếu phân tích lỗi có cấu trúc:** Chưa có phân tích FP/FN đặc trưng của từng phương pháp khi gặp fault injection (HDFS_v3) vs. lỗi tự nhiên (BGL).
7. **OpenStack ít được đánh giá:** Hầu hết phương pháp trong dự án chưa hỗ trợ OpenStack, để lại khoảng trống về tính tổng quát hóa trên log đám mây.

### 1.3. Ý nghĩa khoa học và thực tiễn

**Về khoa học:**
- Cung cấp bằng chứng so sánh đáng tin cậy, có thể tái lập cho cộng đồng nghiên cứu LogAD
- Chuẩn hóa giao thức đánh giá và chỉ ra hướng nghiên cứu tiếp theo

**Về thực tiễn:**
- Đưa ra khuyến nghị lựa chọn phương pháp có điều kiện (theo loại dữ liệu, ràng buộc tài nguyên, yêu cầu về độ trễ và khả năng giải thích)
- Giúp kỹ sư vận hành (SRE) quyết định nhanh nên triển khai công cụ nào

### 1.4. Mục tiêu nghiên cứu

**Mục tiêu tổng quát:**
Đánh giá một cách có hệ thống và công bằng hiệu quả phát hiện bất thường, chi phí tính toán, tính ổn định và khả năng giải thích của sáu phương pháp LogAD đại diện cho năm họ kỹ thuật, trên các bộ dữ liệu log chuẩn, trong một giao thức thực nghiệm mô tả rõ và có thể tái lập.

**Mục tiêu cụ thể:**

1. Tái lập thành công mã nguồn của sáu phương pháp trong môi trường chung.
2. Xây dựng pipeline tiền xử lý và đánh giá thống nhất cho các bộ dữ liệu; mở rộng pipeline đầu vào để cả sáu phương pháp chạy được trên HDFS_v3, BGL và OpenStack.
3. Đo lường và so sánh hiệu quả phát hiện (P/R/F1/PR-AUC) và chi phí tính toán (thời gian huấn luyện, suy luận, bộ nhớ).
4. Phân tích độ ổn định giữa các bộ dữ liệu, phân tích lỗi và khả năng phát hiện sớm.
5. Rút ra khuyến nghị lựa chọn phương pháp theo điều kiện sử dụng.

### 1.5. Câu hỏi nghiên cứu (Research Questions)

| RQ | Nội dung | Mục đích |
|---|---|---|
| **RQ1** | Sáu phương pháp đạt Precision, Recall, F1, PR-AUC như thế nào trên HDFS_v3, BGL, OpenStack khi đánh giá theo cùng một giao thức? | Xác lập baseline so sánh công bằng |
| **RQ2** | Thứ hạng và hiệu quả có thay đổi giữa các bộ dữ liệu có đặc tính khác nhau? | Đánh giá khả năng tổng quát hóa |
| **RQ3** | Đánh đổi giữa độ chính xác và chi phí tính toán (thời gian huấn luyện, suy luận, bộ nhớ) như thế nào? | So sánh ML nhẹ vs. học sâu vs. LLM |
| **RQ4** | Hiệu quả thay đổi thế nào khi chỉ quan sát 10%, 25%, 50%, 75% chuỗi log? | Đánh giá tính thực dụng trong giám sát thời gian thực |
| **RQ5** | Kiểu trường hợp nào thường bị bỏ sót (FN) hoặc gây cảnh báo sai (FP)? Phương pháp nào hỗ trợ giải thích quyết định? | Hiểu cơ chế thất bại, đánh giá khả năng giải thích |

### 1.6. Phạm vi và giả định

- **Trong phạm vi:** 6 phương pháp (CoLog, LightAD, LogFormer, LogRAG, Logs2Graph, SemPCA); 3 bộ dữ liệu (HDFS_v3, BGL, OpenStack) từ LogHub
- **Ngoài phạm vi:** Không đề xuất thuật toán mới; không so sánh số liệu từ bài báo gốc mà không tái lập; không tinh chỉnh mô hình bằng tập kiểm thử; không đánh giá phương pháp không có mã nguồn

### 1.7. Đóng góp dự kiến

1. **Benchmark có thể tái lập** gồm mã nguồn, cấu hình, script tiền xử lý và đánh giá thống nhất
2. **Bảng kết quả và phân tích định lượng** so sánh hiệu quả phát hiện và chi phí tính toán
3. **Đường cong phát hiện sớm** theo tỷ lệ tiền tố chuỗi log
4. **Phân tích lỗi có cấu trúc** (taxonomy của FP/FN) gắn với đặc tính dữ liệu
5. **Khuyến nghị thực tiễn** lựa chọn phương pháp theo điều kiện vận hành

### 1.8. Cấu trúc luận văn

*(Trình bày tóm tắt nội dung các chương)*

---

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN NGHIÊN CỨU

### 2.1. Log hệ thống: đặc điểm, cấu trúc và vai trò

- Định nghĩa log hệ thống và các thành phần: timestamp, severity level, component, content
- Mẫu log (*log template/event*), chuỗi sự kiện, phiên/session/block/trace
- Vai trò của log trong AIOps và giám sát hệ thống

### 2.2. Bài toán phát hiện bất thường log: định nghĩa và phân loại

- Bất thường điểm (*point anomaly*) và bất thường tập thể (*collective anomaly*)
- Các dạng bài toán LogAD: phân loại nhị phân, phát hiện tuần tự, không giám sát/bán giám sát, trực tuyến và phát hiện sớm
- So sánh supervised vs. semi-supervised vs. unsupervised trong bối cảnh LogAD

### 2.3. Quy trình Log Anomaly Detection chuẩn

```
Raw Logs → Log Parsing → Log Grouping → Feature Extraction → Anomaly Detection → Alert
```

- **Log Parsing:** Drain (He et al., 2017) — cây có độ sâu cố định, phân tích trực tuyến
- Ảnh hưởng của lỗi parsing tới downstream task (LogRAG paper chỉ ra vấn đề này)
- **Log Grouping:** theo session/block/trace/window (fixed-size, sliding, session-based)
- **Feature Extraction:** event count vector, TF-IDF, semantic embedding, graph structure

### 2.4. Phân loại các họ phương pháp

| Họ kỹ thuật | Đại diện | Ý tưởng cốt lõi | Kiểu học |
|---|---|---|---|
| Thống kê / ML cổ điển | SemPCA, LightAD | PCA/đếm + phân loại đơn giản (KNN, DT, SLFN) | Không giám sát / Giám sát |
| Học sâu tuần tự | LogFormer | Pre-train Transformer + Adapter fine-tune | Tự giám sát + tinh chỉnh |
| Transformer đa phương thức | CoLog | Collaborative Transformers + MHIA + MAL | Giám sát |
| Mạng nơ-ron đồ thị | Logs2Graph | OCDiGCN: log → đồ thị có hướng/trọng số → one-class GCN | Không giám sát (one-class) |
| LLM + RAG bán giám sát | LogRAG | DeepSVDD phát hiện sơ bộ + RAG + LLM tái đánh giá | Bán giám sát |

### 2.5. Tổng quan chi tiết sáu phương pháp được đánh giá

#### 2.5.1. CoLog (Scientific Reports 2025)

- **Kiến trúc:** Collaborative Transformers + Multi-Head Impressed Attention (MHIA) + Modality Adaptation Layer (MAL)
- **Ý tưởng:** Áp dụng multimodal sentiment analysis vào LogAD; mã hóa cộng tác nhiều modality của log (text, semantic, structural)
- **Khả năng:** Phát hiện cả point lẫn collective anomaly
- **Tiền xử lý:** Dùng sentence-transformer (`all-MiniLM-L6-v2`) để embedding, TomekLinks resampling; **không dùng Drain** log parsing truyền thống
- **Dữ liệu hỗ trợ (mã nguồn):** Casper-RW, DFRWS (Jhuisi, Nssal), Honeynet 7, Zookeeper, Hadoop, BGL
- **Lưu ý:** Cần spaCy `en_core_web_lg`; dùng Hadoop (không phải HDFS_v3); cần mở rộng cho HDFS_v3 và OpenStack

#### 2.5.2. LightAD (ICSE 2024)

- **Kiến trúc:** KNN (k=1), Decision Tree, SLFN (MLP 1 hidden layer, 25 units)
- **Ý tưởng:** Đánh giá lại ML cổ điển với tiền xử lý đơn giản; chứng minh ML nhẹ có thể đạt SOTA
- **Tiền xử lý:** Loại bỏ token chứa chữ số → event count vector (naive aggregation); có tùy chọn deduplicate
- **Chiến lược chia:** HDFS theo random shuffle (5 lần), BGL/supercomputer theo chronological split
- **Dữ liệu hỗ trợ:** HDFS, BGL, Spirit, Liberty, Thunderbird
- **Lưu ý:** Không hỗ trợ OpenStack; hardcoded paths cần chỉnh sửa

#### 2.5.3. LogFormer (AAAI 2024)

- **Kiến trúc:** Transformer Encoder (4 layers, 8 heads, d=768) + Adapter modules + Positional Encoding
- **Ý tưởng:** Pipeline hai giai đoạn: (1) Pre-train trên log không nhãn bằng masked prediction, (2) Adapter tuning (chỉ fine-tune adapter + classifier, đóng băng backbone)
- **Chế độ huấn luyện:** `train_adapter()` (adapter + norm layers), `train_classifier()` (chỉ FC layer cuối)
- **Tiền xử lý:** Drain parsing → Sentence embedding (768d)
- **Dữ liệu hỗ trợ:** LogHub (HDFS, BGL, Thunderbird, Spirit, OpenStack, …) — phương pháp **duy nhất hỗ trợ sẵn cả 3 dataset**

#### 2.5.4. LogRAG (ISSRE 2024)

- **Kiến trúc:** 2-phase pipeline:
  - Phase 1: DeepSVDD (soft-boundary, MLP network) phát hiện anomaly sơ bộ bằng log token embeddings
  - Phase 2: RAG + LLM (GPT-3.5-turbo hoặc Mistral-7B) tái đánh giá các mẫu được phát hiện bằng log template embeddings
- **Ý tưởng:** Giảm FP bằng cách dùng LLM + RAG để xác minh lại kết quả; dùng cả log token lẫn log template để giảm ảnh hưởng parsing errors
- **Tiền xử lý:** Drain parsing → BigLog pretrained encoder → window-based grouping (window_size=200, window_time=1800s)
- **Dữ liệu hỗ trợ:** BGL, Spirit
- **Lưu ý:** Cần API key OpenAI hoặc Mistral-7B; chi phí tính toán cao; chưa hỗ trợ HDFS_v3 và OpenStack

#### 2.5.5. Logs2Graph (ICSE 2024 Companion)

- **Kiến trúc:** OCDiGCN (One-Class Digraph Inception Convolutional Networks)
- **Ý tưởng:** Biểu diễn nhóm log thành đồ thị có hướng, có trọng số (directed, edge-weighted, attributed) → graph-level anomaly detection + node-level explanation
- **Pipeline:** Log parsing → Log grouping → Graph generation (adjacency matrix) → OCDiGCN training → Anomaly scoring + explanation
- **Khả năng giải thích:** Node importance scores cho thấy log event nào đóng góp nhiều nhất vào anomaly score
- **Dữ liệu hỗ trợ:** HDFS, Hadoop, Spirit, BGL, Thunderbird (mỗi dataset có script riêng: `GraphGeneration_xxx.py`, `main_xxx.py`)
- **Lưu ý:** `root_path` hardcoded; chưa hỗ trợ OpenStack; cần tạo `GraphGeneration_OpenStack.py` và `main_OpenStack.py`

#### 2.5.6. SemPCA (Empirical Study)

- **Kiến trúc:** PCA++ (PCA cải tiến) trên biểu diễn ngữ nghĩa log
- **Ý tưởng:** Kết hợp TF-IDF template encoding + GloVe semantic embedding + Sequential Add → PCA dimension reduction → anomaly score (SPE/Q-statistic)
- **Tiền xử lý:** Drain3 (IBM) parsing → TF-IDF template encoding → GloVe 6B 300d embedding → chia 6:1:3 (cut_by_613)
- **Dữ liệu hỗ trợ:** HDFS, BGL, Spirit
- **Lưu ý:** **Yêu cầu scikit-learn ≤ 0.24** (joblib compatibility issue); seed cố định = 6; chưa hỗ trợ OpenStack

### 2.6. Bộ dữ liệu benchmark: HDFS_v3, OpenStack, BGL

#### 2.6.1. Mô tả chi tiết

| Đặc tính | HDFS_v3 (TraceBench) | OpenStack | BGL |
|---|---|---|---|
| **Loại hệ thống** | Hệ phân tán (Hadoop HDFS) | Hạ tầng đám mây (IaaS) | Siêu máy tính (BlueGene/L) |
| **Quy mô** | ~14.8M dòng, 2.96 GiB | ~207K dòng, 58.61 MiB | ~4.75M dòng, 708.76 MiB |
| **Cơ chế nhãn** | Fault injection có kiểm soát (MTracer, 17 loại fault) | Failure injection trên CloudLab | Lỗi tự nhiên production |
| **Cấp độ nhãn** | Trace-level | Session-level | Line-level (alert tag) |
| **Tỷ lệ bất thường** | Có kiểm soát theo kịch bản | Cân bằng hơn do injection | ~7.3% (tự nhiên) |
| **Nguồn** | LogHub / TraceBench | LogHub | LogHub / USENIX CFDR |

#### 2.6.2. Ma trận hỗ trợ (mã nguồn hiện tại)

| Phương pháp | HDFS_v3 | BGL | OpenStack | Cần mở rộng |
|---|---|---|---|---|
| CoLog | – (dùng Hadoop) | ✓ | ✗ | HDFS_v3 (ánh xạ Hadoop→HDFS), OpenStack |
| LightAD | ✓ | ✓ | ✗ | OpenStack |
| LogFormer | ✓ | ✓ | ✓ | — (hỗ trợ đầy đủ) |
| LogRAG | ✗ | ✓ | ✗ | HDFS_v3, OpenStack |
| Logs2Graph | ✓ | ✓ | ✗ | OpenStack |
| SemPCA | ✓ | ✓ | ✗ | OpenStack |

#### 2.6.3. Lý do chọn ba bộ dữ liệu

- Bao phủ ba loại môi trường hệ thống quan trọng (phân tán, đám mây, siêu máy tính)
- Khác nhau về cơ chế nhãn (injection vs. tự nhiên), cấp độ nhãn, quy mô
- Đều có nhãn công khai, được sử dụng rộng rãi trong cộng đồng nghiên cứu
- Cho phép đánh giá khả năng tổng quát hóa

### 2.7. Chỉ số đánh giá và sự không đồng nhất trong tài liệu

- Precision, Recall, F1-score: cách tính khác nhau giữa các bài báo (cấp mẫu, cấp window, cấp block)
- PR-AUC vs. ROC-AUC: lựa chọn trong bối cảnh dữ liệu mất cân bằng
- FPR: quan trọng cho vận hành thực tế nhưng thường bị bỏ qua
- Chi phí tính toán: hiếm khi được báo cáo đồng nhất

### 2.8. Khoảng trống nghiên cứu (tổng hợp)

1. Chưa có benchmark đa phương pháp trên giao thức thống nhất bao gồm cả GNN và RAG+LLM trên HDFS_v3, OpenStack, BGL cùng lúc
2. Chưa có đánh giá hệ thống về phát hiện sớm (prefix-based) trên nhiều phương pháp với ba loại môi trường
3. Chưa có phân tích chi phí tính toán so sánh trực tiếp giữa ML cổ điển và học sâu nặng trên cùng phần cứng
4. Chưa có phân tích lỗi có cấu trúc giải thích FP/FN đặc trưng khi gặp fault injection (HDFS_v3) vs. lỗi tự nhiên (BGL)
5. Vấn đề đánh đổi giữa chi phí LLM/RAG và phương pháp nhẹ chưa được làm rõ
6. OpenStack ít được đánh giá, để lại khoảng trống về tính tổng quát hóa trên log đám mây

---

## CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU VÀ THIẾT KẾ THỰC NGHIỆM

### 3.1. Câu hỏi nghiên cứu chi tiết

*(Xem Mục 1.5 — mỗi RQ được phát triển thành: mục đích, kết quả cần có, phương pháp trả lời)*

| RQ | Kết quả cần có | Phương pháp trả lời |
|---|---|---|
| RQ1 | Bảng benchmark chéo (6 × 3 × P/R/F1) | So sánh trực tiếp trên cùng pipeline |
| RQ2 | Rank correlation (Spearman/Kendall); trường hợp điển hình | Phân tích thay đổi thứ hạng; fault injection vs. lỗi tự nhiên |
| RQ3 | Biểu đồ F1 vs. latency; bảng RAM/GPU memory | Đo thời gian + bộ nhớ trên cùng phần cứng |
| RQ4 | Đường cong F1 theo tiền tố (10/25/50/75/100%) | Cắt chuỗi log tại các mốc; đánh giá F1/Recall tại mỗi mốc |
| RQ5 | Taxonomy lỗi FP/FN; case study; đánh giá giải thích | Lấy mẫu 50-100 FP/FN; phân loại thủ công; Logs2Graph node score, LogRAG LLM reasoning |

### 3.2. Tiêu chí lựa chọn baseline

Sáu phương pháp được chọn vì thỏa mãn đồng thời:

1. **Tính đại diện:** bao phủ năm họ kỹ thuật khác biệt
2. **Tính thời sự:** công bố 2024–2025 (SOTA gần nhất)
3. **Khả năng tái lập:** có mã nguồn mở đầy đủ trong dự án
4. **Tính so sánh:** có giao thoa bộ dữ liệu để đánh giá chung

Mỗi baseline được ghi nhận:
- Trích dẫn gốc, nhóm phương pháp, kiểu học
- Yêu cầu nhãn, đầu vào/đầu ra, tiền xử lý
- Mã nguồn/commit, điểm mạnh/hạn chế
- Rủi ro tái lập (dependencies, hardcoded paths, etc.)

### 3.3. Lựa chọn và mô tả bộ dữ liệu

- **Nguồn:** LogHub (logpai/loghub) — ghi nhận phiên bản/commit khi tải
- **Ghi nhận:** số bản ghi, tỷ lệ bất thường, cấp độ nhãn
- **Đặc biệt lưu ý:** cấp độ nhãn ảnh hưởng tới cách tính metric và khả năng đo phát hiện sớm

### 3.4. Quy trình tiền xử lý thống nhất

```
┌──────────────────────────────────────────────────────────────────┐
│                    UNIFIED PREPROCESSING PIPELINE                 │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Raw Logs ──→ Drain Parsing ──→ Template + Parameters             │
│                    │                                              │
│                    ├──→ Session/Block/Window Grouping              │
│                    │         │                                    │
│                    │         ├──→ Event Count Vector (LightAD)    │
│                    │         ├──→ TF-IDF + GloVe (SemPCA)        │
│                    │         ├──→ Sentence Embedding (LogFormer)  │
│                    │         ├──→ Graph Construction (Logs2Graph)  │
│                    │         ├──→ DeepSVDD Embedding (LogRAG)     │
│                    │         └──→ Multi-modal Embedding (CoLog*)  │
│                    │                                              │
│  * CoLog dùng sentence-transformer thay vì Drain                 │
│    → ghi rõ khác biệt, không ép đồng nhất                       │
└──────────────────────────────────────────────────────────────────┘
```

**Nguyên tắc:**
- **Drain** là log parser chuẩn cho 5/6 phương pháp (CoLog dùng sentence-transformer — tôn trọng thiết kế gốc, ghi rõ khác biệt)
- Ghi tỷ lệ lỗi parsing cho từng dataset
- Chuẩn hóa timestamp; loại bỏ bản ghi thiếu trường bắt buộc
- Xử lý dữ liệu trùng lặp, thiếu và mẫu không hợp lệ

### 3.5. Đồng bộ hóa pipeline đầu vào (mở rộng mã nguồn)

| Phương pháp | Mở rộng cần thực hiện | Mức độ phức tạp | Chi tiết kỹ thuật |
|---|---|---|---|
| CoLog | Thêm HDFS_v3 (ánh xạ Hadoop→HDFS), OpenStack | Trung bình | Tạo preprocessing script mới trong `groundtruth/`; điều chỉnh `--dataset` parameter |
| LightAD | Thêm OpenStack | Trung bình | Tạo `preprocess.py --dataset openstack`; viết loader mới trong `utils.py` |
| LogRAG | Thêm HDFS_v3, OpenStack | Cao | Tạo `log_structured.csv` cho HDFS_v3/OpenStack; điều chỉnh window strategy |
| Logs2Graph | Thêm OpenStack | Trung bình | Tạo `GraphGeneration_OpenStack.py` và `main_OpenStack.py` theo mẫu existing |
| SemPCA | Thêm OpenStack | Thấp-Trung bình | Tạo dataset folder + config; điều chỉnh `cut_by_613` cho OpenStack sessions |
| LogFormer | Không cần | — | Đã hỗ trợ đầy đủ |

### 3.6. Giao thức chia dữ liệu và kiểm soát data leakage

| Dataset | Chiến lược chia | Chi tiết |
|---|---|---|
| **HDFS_v3** | Theo trace ID | `normal_trace.csv` + `failure_trace.csv`; 80/10/10; đảm bảo phân phối loại fault đa dạng trong test |
| **BGL** | Chronological split | Fixed-size window theo thời gian; không random shuffle để tránh data leakage |
| **OpenStack** | Theo session/workflow | 80/10/10; giữ tỷ lệ normal/anomaly nhất quán |

**Kiểm soát:**
- Kiểm tra mẫu trùng lặp/chuỗi chồng lấn giữa train/val/test
- Không dùng thông tin tương lai trong thí nghiệm phát hiện sớm
- Ngưỡng chỉ chọn trên validation, không trên test

### 3.7. Thiết lập huấn luyện và hiệu chỉnh siêu tham số

- Siêu tham số từ bài báo gốc làm điểm khởi đầu
- Grid search giới hạn trên validation khi bài báo không công bố đủ
- Áp dụng cùng quy trình tuning cho **TẤT CẢ** phương pháp
- **Random seed cố định:** 42 cho mọi thành phần (trừ SemPCA đã cố định seed=6, cần ghi nhận)
- Chạy lặp nhiều lần khi có yếu tố ngẫu nhiên → báo cáo trung bình ± std

**Siêu tham số quan trọng theo phương pháp (từ mã nguồn):**

| Phương pháp | Siêu tham số chính |
|---|---|
| CoLog | epochs=100, batch_size=32, model=`all-MiniLM-L6-v2`, resample_method=TomekLinks |
| LightAD | KNN: n_neighbors=1; DT: default; SLFN: hidden_layer_sizes=(25,) |
| LogFormer | num_layers=4, nhead=8, dim=768, adapter_size=64, dim_feedforward=3072, dropout=0.1 |
| LogRAG | lr=0.0001, n_epochs=150, batch_size=40960, window_size=200, threshold=0.8, topk=5 |
| Logs2Graph | (Từ GLAM framework — cần đọc chi tiết config) |
| SemPCA | n_components=20, c_alpha=3.2905, GloVe 6B 300d, cut_by_613 |

### 3.8. Chỉ số đánh giá chi tiết

| Chỉ số | Đơn vị / cách tính | RQ liên quan |
|---|---|---|
| Precision | TP/(TP+FP) cấp mẫu | RQ1, RQ2, RQ4 |
| Recall | TP/(TP+FN) cấp mẫu | RQ1, RQ2, RQ4 |
| F1-score | 2×P×R/(P+R) | RQ1, RQ2, RQ4 |
| PR-AUC | Khi mô hình cho anomaly score | RQ1 |
| False Positive Rate | FP/(FP+TN) | RQ1, RQ5 |
| Thời gian huấn luyện | giây (trên cùng phần cứng) | RQ3 |
| Độ trễ suy luận | ms/sample trung bình | RQ3 |
| Bộ nhớ đỉnh | MB/GB (GPU + RAM) | RQ3 |
| F1/Recall theo tiền tố | Tại 10%, 25%, 50%, 75%, 100% | RQ4 |
| Rank correlation | Spearman/Kendall τ giữa datasets | RQ2 |
| Taxonomy lỗi FP/FN | Phân nhóm có tiêu chí rõ | RQ5 |

### 3.9. Thiết kế đánh giá phát hiện sớm (RQ4)

- Định nghĩa "sớm" bằng tỷ lệ tiền tố: 10%, 25%, 50%, 75%, 100%
- Chỉ áp dụng với dataset/phương pháp cho phép xác định dự đoán tại từng tiền tố
- Không dùng thông tin xuất hiện sau thời điểm giả định phát hiện
- Vẽ đường cong hiệu quả theo tiền tố; phân tích đánh đổi early detection vs. FPR
- Tách riêng phân tích cho: fault injection (HDFS_v3) vs. lỗi tự nhiên (BGL) vs. cloud failure (OpenStack)

### 3.10. Quy trình phân tích lỗi (RQ5)

1. Trích xuất **50–100 FP** và **50–100 FN** từ mỗi phương pháp trên mỗi dataset
2. Phân loại thủ công (với kiểm tra chéo) vào các nhóm:
   - Unseen log template (template chưa gặp trong training)
   - Chuỗi quá ngắn/quá dài
   - Bất thường lặp lại (repeated anomaly pattern)
   - Nhiễu nhãn (noisy labels)
   - Mất cân bằng lớp (class imbalance effect)
3. Tổng hợp tỷ lệ từng nhóm lỗi theo phương pháp
4. **Đánh giá khả năng giải thích:**
   - Logs2Graph: node importance scores — log event nào đóng góp nhiều nhất vào anomaly score
   - LogRAG: LLM reasoning — lý do tái phân loại qua prompt

### 3.11. Môi trường thực nghiệm

| Thành phần | Yêu cầu | Ghi chú |
|---|---|---|
| GPU | NVIDIA RTX 3090 hoặc tương đương | Cùng GPU cho mọi phương pháp |
| RAM | ≥ 32 GB | |
| Python | 3.8 (compatibility tốt nhất) | SemPCA yêu cầu 3.8; LogRAG yêu cầu 3.8.18 |
| PyTorch | 1.13+ | LogFormer dùng nn.MultiheadAttention batch_first |
| scikit-learn | ≤ 0.24 (SemPCA) / latest (LightAD) | Cần 2 virtual environments hoặc ghi nhận khác biệt |
| transformers | 4.x | LogRAG, LogFormer |
| LLM API | OpenAI GPT-3.5-turbo hoặc Mistral-7B local | LogRAG; cần API key hoặc GPU đủ cho Mistral |
| spaCy | `en_core_web_lg` | CoLog |
| GloVe | `glove.6B.300d.txt` | SemPCA |

**Ngoại lệ cần ghi nhận:**
- LogRAG cần API LLM (chi phí $, latency không kiểm soát hoàn toàn)
- SemPCA bị giới hạn scikit-learn ≤ 0.24
- CoLog cần spaCy model riêng

### 3.12. Kiểm soát sai lệch, độ tin cậy và tái lập

- Ngăn rò rỉ dữ liệu giữa train/validation/test
- So sánh công bằng: giữ giống nhau điều kiện có thể; tôn trọng yêu cầu đầu vào riêng và ghi rõ khác biệt
- Báo cáo tính ngẫu nhiên và độ biến thiên
- Tránh khẳng định nhân quả khi thiết kế chỉ cho thấy mối liên hệ
- Cung cấp gói tái lập: mã, cấu hình, script, tài liệu
- Nêu rõ giới hạn chia sẻ (API key, giấy phép dữ liệu)
- Báo cáo cả lần chạy thất bại

---

## CHƯƠNG 4: KẾT QUẢ THỰC NGHIỆM

### 4.1. RQ1: Hiệu quả phát hiện tổng thể

- Bảng benchmark chéo: 6 phương pháp × 3 dataset × (P, R, F1, PR-AUC)
- Thống kê: trung bình ± std qua nhiều lần chạy
- So sánh với kết quả báo cáo trong bài báo gốc (nếu có thể)
- Phân tích: phương pháp nào đạt F1 cao nhất tổng thể? Có khác biệt đáng kể?

### 4.2. RQ2: Độ ổn định giữa các tập dữ liệu

- Rank correlation (Spearman ρ, Kendall τ) giữa thứ hạng trên 3 datasets
- Trường hợp điển hình: phương pháp nào "overfit" vào đặc trưng một loại log?
- So sánh hiệu quả trên fault injection (HDFS_v3) vs. lỗi tự nhiên (BGL) vs. cloud failure (OpenStack)
- Heatmap thay đổi thứ hạng

### 4.3. RQ3: Chi phí tính toán

- Bảng chi phí: thời gian huấn luyện, suy luận, bộ nhớ GPU/RAM
- Biểu đồ scatter: F1 vs. inference latency
- Biểu đồ: F1 vs. total memory footprint
- Phân tích đặc biệt: chi phí API LLM của LogRAG ($ + latency) vs. thời gian chạy LightAD (vài giây)
- Throughput (samples/second) cho kịch bản thời gian thực

### 4.4. RQ4: Khả năng phát hiện sớm

- Đường cong F1 theo tỷ lệ tiền tố (10/25/50/75/100%) cho mỗi phương pháp × mỗi dataset
- Phân tích: phương pháp nào duy trì hiệu quả tốt nhất khi chỉ có dữ liệu đầu chuỗi?
- Đánh đổi early detection vs. FPR
- So sánh theo loại dataset: trace-level (HDFS_v3) vs. session (OpenStack) vs. line-level (BGL)

### 4.5. RQ5: Phân tích lỗi và khả năng giải thích

- Taxonomy lỗi FP/FN:
  - Bảng tổng hợp tỷ lệ từng nhóm lỗi theo phương pháp
  - Case study minh họa (ví dụ cụ thể)
- Đánh giá định tính khả năng giải thích:
  - Logs2Graph: ví dụ node importance scores
  - LogRAG: ví dụ LLM reasoning output
- Phân tích liên hệ lỗi với đặc tính dữ liệu

---

## CHƯƠNG 5: THẢO LUẬN

### 5.1. Tổng hợp phát hiện chính theo RQ

- Bảng tóm tắt câu trả lời cho mỗi RQ
- Phát hiện bất ngờ / mâu thuẫn với kết quả bài báo gốc

### 5.2. Khuyến nghị lựa chọn phương pháp theo điều kiện thực tế

| Ràng buộc | Khuyến nghị (dự kiến) |
|---|---|
| Tài nguyên hạn chế, cần nhanh | LightAD / SemPCA |
| Yêu cầu F1 cao nhất, có GPU | LogFormer / CoLog |
| Cần giải thích anomaly | Logs2Graph / LogRAG |
| Cần phát hiện sớm | (Tùy thuộc kết quả RQ4) |
| Log đám mây | (Tùy thuộc kết quả trên OpenStack) |
| Giảm FP là ưu tiên | LogRAG (LLM tái đánh giá) |

### 5.3. Hạn chế của nghiên cứu

- Chỉ đại diện cho 6 phương pháp và 3 bộ dữ liệu
- Số đo hiệu năng trên 1 môi trường phần cứng
- Yêu cầu đặc thù (API LLM, scikit-learn version)
- Phát hiện sớm chỉ áp dụng khi nhãn/cấu trúc cho phép
- Pipeline mở rộng có thể tạo khác biệt so với thiết kế gốc

### 5.4. Threats to Validity

- **Internal validity:** data leakage, hyperparameter fairness, random seed consistency
- **External validity:** 3 datasets không đại diện cho mọi hệ thống
- **Construct validity:** metric definition consistency, label granularity differences
- **Conclusion validity:** statistical significance, multiple comparisons

### 5.5. Hướng nghiên cứu tiếp theo

- Mở rộng benchmark cho streaming/online detection
- Kết hợp ưu điểm của nhiều họ phương pháp (ensemble)
- Đánh giá trên dữ liệu log thương mại thực tế
- Tự động hóa lựa chọn phương pháp (AutoML for LogAD)

---

## CHƯƠNG 6: KẾT LUẬN

- Tóm tắt câu trả lời cho 5 RQ
- Đóng góp chính
- Lời kết và ý nghĩa thực tiễn

---

## TÀI LIỆU THAM KHẢO

### Bài báo gốc của 6 phương pháp:
1. Nasirzadeh, M., Tahmoresnezhad, J., & Rashidi-Khazaee, P. (2025). *A unified framework for detecting point and collective anomalies in operating system logs via collaborative transformers.* Scientific Reports, 15, Article 27693. **(CoLog)**
2. Yu, B., Yao, J., Fu, Q., et al. (2024). *Deep Learning or Classical Machine Learning? An Empirical Study on Log-Based Anomaly Detection.* ICSE 2024. **(LightAD)**
3. Guo, H., Yang, J., Liu, J., et al. (2024). *LogFormer: A Pre-train and Tuning Pipeline for Log Anomaly Detection.* AAAI 2024. **(LogFormer)**
4. (2024). *Leveraging RAG-Enhanced Large Language Model for Semi-Supervised Log Anomaly Detection.* ISSRE 2024. **(LogRAG)**
5. Li, Z., Shi, J., & van Leeuwen, M. (2024). *Graph Neural Networks based Log Anomaly Detection and Explanation.* ICSE-Companion 2024. **(Logs2Graph)**
6. *Try with Simpler – An Evaluation of Improved Principal Component Analysis in Log-based Anomaly Detection.* **(SemPCA)**

### Công trình nền tảng:
7. He, P., Zhu, J., Zheng, Z., & Lyu, M. R. (2017). *Drain: An Online Log Parsing Approach with Fixed Depth Tree.* ICWS 2017.
8. Du, M., Li, F., Zheng, G., & Srikumar, V. (2017). *DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning.* CCS 2017.
9. Meng, W., et al. (2019). *LogAnomaly: Unsupervised Detection of Sequential and Quantitative Anomalies in Unstructured Logs.* IJCAI 2019.
10. Zhang, X., et al. (2019). *Robust Log-Based Anomaly Detection on Unstable Log Data.* FSE 2019. (LogRobust)
11. Guo, H., et al. (2021). *LogBERT: Log Anomaly Detection via BERT.* IJCNN 2021.

### Bộ dữ liệu:
12. Zhu, J., et al. (2023). *Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics.* ISSRE 2023.
13. Zhou, X., et al. (2014). *TraceBench: An Open Data Set for Trace-oriented Monitoring.* CloudCom 2014. (HDFS_v3)
14. Oliner, A. & Stearley, J. (2007). *What Supercomputers Say: A Study of Five System Logs.* DSN 2007. (BGL)

### Phương pháp luận:
15. ACM SIGSOFT Empirical Standards (thiết kế và báo cáo nghiên cứu thực nghiệm)

---

## PHỤ LỤC

### Phụ lục A: Bảng tổng hợp bài báo tham khảo (30+ bài)
- Bảng trích xuất: tên, năm, kiến trúc, kiểu học, dữ liệu, metric, hạn chế

### Phụ lục B: Bảng đặc tả kỹ thuật chi tiết 6 phương pháp
- Input/Output format
- Dependencies và phiên bản
- Kiến trúc mô hình (sơ đồ)
- Training procedure
- Inference procedure

### Phụ lục C: Cấu hình siêu tham số chi tiết
- Bảng siêu tham số cuối cùng cho mỗi baseline × mỗi dataset
- Grid search ranges đã thử
- Lệnh chạy chính xác

### Phụ lục D: Kết quả thô đầy đủ
- Bảng kết quả cho mọi lần chạy (không chỉ trung bình)
- Confusion matrices
- Script tạo biểu đồ

### Phụ lục E: Mô tả pipeline tái lập
- Hướng dẫn cài đặt (Docker / virtualenv)
- Hướng dẫn chạy từng bước
- Cấu trúc repository

### Phụ lục F: Danh sách trường hợp lỗi trong phân tích lỗi (RQ5)
- Ví dụ cụ thể FP/FN với log content
- Phân nhóm và giải thích

### Phụ lục G: Checklist thực nghiệm
- Threats to validity checklist
- Reproducibility checklist
