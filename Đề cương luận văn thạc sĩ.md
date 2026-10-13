# ĐỀ CƯƠNG CHI TIẾT LUẬN VĂN THẠC SĨ

---

## PHẦN I — THÔNG TIN CHUNG

**Tên đề tài (Tiếng Việt):**
Đánh giá thực nghiệm các phương pháp phát hiện bất thường dựa trên dữ liệu log: Từ học máy cổ điển đến mô hình ngôn ngữ lớn

**Tên đề tài (Tiếng Anh):**
An Empirical Evaluation of Log-Based Anomaly Detection Methods: From Classical Machine Learning to Large Language Models

---

## PHẦN II — ĐẶT VẤN ĐỀ VÀ LÝ DO CHỌN ĐỀ TÀI

### 1. Bối cảnh

Các hệ thống phần mềm hiện đại — từ cụm phân tán (Hadoop, HDFS), siêu máy tính (BGL, Thunderbird) đến hạ tầng đám mây — liên tục sinh ra khối lượng log khổng lồ. Log là nhật ký hoạt động chứa các sự kiện hệ thống, lỗi, cảnh báo và trạng thái vận hành. Kỹ sư vận hành (Site Reliability Engineer) dựa vào log để chẩn đoán sự cố, nhưng với quy mô hàng triệu dòng log mỗi ngày, việc phân tích thủ công là không khả thi.

Phát hiện bất thường tự động dựa trên log (Log-Based Anomaly Detection) trở thành bài toán cốt lõi trong AIOps. Từ 2017 đến nay, hàng chục phương pháp học sâu đã được công bố: DeepLog (LSTM, 2017), LogAnomaly (GRU + ngữ nghĩa, 2019), LogRobust (Attention, 2019), LogBERT (BERT, 2021), LogFormer (Transformer chia sẻ tham số, 2023), Logs2Graph (GNN đồ thị có hướng, 2024), LightAD (Machine Learning cổ điển, 2024), LogRAG (RAG + LLM, 2024), v.v.

Nghiên cứu này sử dụng ba bộ dữ liệu từ **LogHub** — bộ sưu tập log hệ thống công khai chuẩn mực trong cộng đồng nghiên cứu (Zhu et al., ISSRE 2023) — bao gồm: **HDFS_v3 (TraceBench)** đại diện cho hệ thống phân tán với fault injection có kiểm soát, **OpenStack** đại diện cho hạ tầng đám mây hiện đại, và **BGL** đại diện cho siêu máy tính với nhãn cấp dòng. Ba bộ dữ liệu này bao phủ ba loại môi trường hệ thống quan trọng và khác nhau về đặc tính log, giúp đánh giá khả năng tổng quát hóa của các phương pháp.

### 2. Vấn đề nghiên cứu

Mặc dù mỗi bài báo báo cáo hiệu quả cao trên tập dữ liệu riêng của mình, có một số vấn đề chưa được giải quyết một cách có hệ thống:

- **Thiếu giao thức đánh giá thống nhất:** Các nghiên cứu dùng cách chia dữ liệu, cách tính chỉ số và cách xử lý nhãn khác nhau, khiến so sánh trực tiếp giữa các bài báo không đáng tin cậy.
- **Bỏ qua khả năng phát hiện sớm:** Hầu hết chỉ đo kết quả cuối chuỗi, không đánh giá mô hình hoạt động thế nào khi chỉ có một phần chuỗi log — điều quan trọng trong thực tế vận hành thời gian thực.
- **Chưa so sánh chi phí tính toán:** Một số phương pháp như LogRAG tích hợp LLM rất nặng, trong khi LightAD sử dụng ML cổ điển nhẹ hơn nhiều. Sự đánh đổi giữa độ chính xác và chi phí chưa được định lượng công bằng.
- **Độ ổn định giữa các tập dữ liệu:** Chưa rõ một phương pháp tốt trên HDFS_v3 có ổn định trên OpenStack, BGL hay không — đặc biệt khi ba bộ dữ liệu này khác nhau về môi trường (hệ thống phân tán, đám mây, siêu máy tính), cơ chế gán nhãn (trace-level, session-level, line-level) và tỷ lệ bất thường.
- **Tác động của log parsing:** LogRAG chỉ ra lỗi parsing ảnh hưởng đến kết quả, nhưng chưa có nghiên cứu đo lường mức độ ảnh hưởng này một cách hệ thống trên nhiều phương pháp.

### 3. Ý nghĩa khoa học và thực tiễn

- **Khoa học:** Cung cấp bộ benchmark có kiểm soát với giao thức thống nhất, cho phép các nghiên cứu sau so sánh công bằng.
- **Thực tiễn:** Giúp kỹ sư vận hành lựa chọn phương pháp phù hợp với ràng buộc thực tế (tài nguyên, loại log, yêu cầu phát hiện sớm).

---

## PHẦN III — TỔNG QUAN NGHIÊN CỨU

### 1. Phân loại phương pháp

| Nhóm | Phương pháp đại diện | Cách tiếp cận |
|---|---|---|
| Mô hình tuần tự (LSTM/GRU) | DeepLog, LogAnomaly | Dự đoán log tiếp theo |
| Attention/Transformer | LogRobust, LogFormer | Biểu diễn ngữ nghĩa chuỗi |
| BERT-based | LogBERT | Masked token prediction |
| Đồ thị (GNN) | Logs2Graph | Biểu diễn log dưới dạng đồ thị có hướng |
| ML cổ điển | LightAD (KNN, DT, SLFN) | Đặc trưng đếm sự kiện |
| RAG + LLM | LogRAG | Phát hiện kết hợp LLM |
| Bán giám sát | SemPCA, CoLog | PCA ngữ nghĩa, Transformer cộng tác |

### 2. Bộ dữ liệu phổ biến trong nghiên cứu log anomaly detection

| Dataset | Nguồn | Quy mô | Có nhãn | Ghi chú |
|---|---|---|---|---|
| HDFS_v1 | Hệ thống phân tán Hadoop | ~11.2M dòng, 1.47GiB | ✔️ | Nhãn cấp block/session, được dùng rộng rãi nhất |
| HDFS_v3 (TraceBench) | HDFS với fault injection (TraceBench/MTracer) | ~14.8M dòng, 2.96GiB | ✔️ | Nhãn cấp trace, 17 loại fault injection |
| OpenStack | Hạ tầng đám mây (CloudLab) | ~207K dòng, 58.61MiB | ✔️ | Có cả log bình thường và failure injection |
| BGL | Siêu máy tính Blue Gene/L (LLNL) | ~4.75M dòng, 708.76MiB | ✔️ | Nhãn cấp dòng log (alert/non-alert) |
| Thunderbird | Siêu máy tính Sandia | ~211M dòng, 29.60GiB | ✔️ | Quy mô rất lớn, tỷ lệ bất thường thấp |

### 3. Khoảng trống nghiên cứu

Qua tổng quan tài liệu, có thể xác định ít nhất bốn khoảng trống chưa được lấp đầy bởi một nghiên cứu đơn lẻ nào:

1. Chưa có benchmark đa phương pháp trên giao thức thống nhất bao gồm cả nhóm GNN (Logs2Graph) và nhóm RAG+LLM (LogRAG) trên bộ dữ liệu HDFS_v3, OpenStack và BGL cùng lúc.
2. Chưa có đánh giá hệ thống về khả năng phát hiện sớm (prefix-based evaluation) trên nhiều phương pháp với ba loại môi trường hệ thống khác nhau.
3. Chưa có phân tích chi phí tính toán so sánh trực tiếp giữa ML cổ điển (LightAD) và học sâu nặng (LogRAG) trên cùng bộ dữ liệu và phần cứng.
4. Chưa có phân tích lỗi có cấu trúc giải thích nguyên nhân false positive/false negative đặc trưng của từng phương pháp, đặc biệt khi gặp fault injection có kiểm soát (HDFS_v3) so với lỗi tự nhiên (BGL).

---

## PHẦN IV — MỤC TIÊU VÀ CÂU HỎI NGHIÊN CỨU

### Mục tiêu tổng quát

Đánh giá có hệ thống hiệu quả phát hiện, khả năng phát hiện sớm, chi phí tính toán và tính ổn định của một nhóm phương pháp phát hiện bất thường log đại diện, trong một giao thức thực nghiệm thống nhất, có thể mô tả rõ và tái lập được.

### Câu hỏi nghiên cứu (Research Questions)

**RQ1 — Hiệu quả phát hiện tổng thể:**
Các phương pháp đại diện đạt Precision, Recall và F1-score như thế nào khi được đánh giá theo cùng một giao thức chia dữ liệu, cùng log parser và cùng cách tính nhãn trên ba bộ dữ liệu HDFS_v3, OpenStack và BGL?

- *Mục đích:* Xác lập baseline so sánh công bằng, loại bỏ nhiễu từ sự khác biệt giao thức giữa các bài báo.
- *Kết quả cần có:* Bảng benchmark chéo (mô hình × dataset: HDFS_v3 / OpenStack / BGL).

**RQ2 — Khả năng phát hiện sớm:**
Hiệu quả của các phương pháp thay đổi thế nào khi chỉ quan sát được 25%, 50%, 75% và 100% chuỗi log của một phiên?

- *Mục đích:* Đánh giá tính thực dụng trong kịch bản giám sát thời gian thực.
- *Kết quả cần có:* Đường cong F1 theo tỷ lệ tiền tố; phân tích đánh đổi giữa phát hiện sớm và false positive rate.

**RQ3 — Chi phí tính toán:**
Các phương pháp đánh đổi hiệu quả phát hiện với chi phí huấn luyện và suy luận như thế nào?

- *Mục đích:* Giúp lựa chọn phương pháp phù hợp với môi trường tài nguyên hạn chế.
- *Kết quả cần có:* Biểu đồ F1 vs. thời gian suy luận; bảng so sánh RAM/GPU memory.

**RQ4 — Độ ổn định giữa các tập dữ liệu:**
Thứ hạng tương đối của các phương pháp có nhất quán trên ba bộ dữ liệu có đặc tính khác nhau (HDFS_v3, OpenStack, BGL) hay không?

- *Mục đích:* Phát hiện phương pháp nào "overfit" vào đặc trưng một loại log cụ thể; đánh giá khả năng tổng quát hóa qua hệ thống phân tán (HDFS_v3), đám mây (OpenStack) và siêu máy tính (BGL).
- *Kết quả cần có:* Phân tích rank correlation; trường hợp điển hình của sự không ổn định; so sánh hiệu quả trên fault injection có kiểm soát (HDFS_v3) vs. lỗi tự nhiên (BGL).

**RQ5 — Phân tích lỗi:**
Những kiểu bất thường nào thường bị bỏ sót hoặc gây cảnh báo sai, và các lỗi này liên quan đến đặc tính dữ liệu nào?

- *Mục đích:* Hiểu cơ chế thất bại của từng phương pháp, không chỉ quan sát điểm số tổng hợp.
- *Kết quả cần có:* Phân loại lỗi theo kiểu (unseen template, chuỗi ngắn, mất cân bằng lớp); case study minh họa.

---

## PHẦN V — ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU

### Phương pháp được đánh giá (Baselines)

Lựa chọn dựa trên: tính đại diện về kiến trúc, có mã nguồn công khai có thể cài đặt, công bố từ 2021–2024.

| STT | Phương pháp | Kiến trúc | Loại học | Paper |
|---|---|---|---|---|
| 1 | LogFormer | Transformer chia sẻ tham số | Giám sát | ASE 2023 |
| 2 | SemPCA | PCA + ngữ nghĩa | Không giám sát | ICSE 2023 |
| 3 | LightAD | KNN / DT / SLFN | ML cổ điển | ICSE 2024 |
| 4 | Logs2Graph | GNN đồ thị có hướng | Không giám sát | ICSE 2024 |
| 5 | LogRAG | DeepSVDD + RAG + LLM | Bán giám sát | ISSRE 2024 |
| 6 | CoLog | Collaborative Transformer | Giám sát | (tham khảo) |

> **Lưu ý:** Nếu trong quá trình tái lập một phương pháp không thể chạy được do phụ thuộc không tương thích hoặc dữ liệu không đủ, phương pháp đó sẽ được ghi nhận trong phụ lục với lý do cụ thể và loại khỏi một phần kết luận liên quan.

### Bộ dữ liệu

Ba bộ dữ liệu được chọn từ **LogHub** (https://github.com/logpai/loghub), đều có nhãn công khai, bao phủ ba loại môi trường hệ thống khác nhau và tạo ra các thách thức đánh giá đặc trưng riêng biệt.

| Dataset | Mô tả | Quy mô | Nhãn | Loại môi trường | Lý do chọn |
|---|---|---|---|---|---|
| **HDFS_v3** (TraceBench) | HDFS với fault injection qua MTracer trên môi trường IaaS thực tế | ~14.8M dòng, 2.96GiB | ✔️ Cấp trace; 17 loại fault | Hệ thống phân tán | Nhãn fault injection có kiểm soát, đa dạng loại lỗi (function & performance faults); phù hợp đánh giá phát hiện sớm theo trace |
| **OpenStack** | Log hạ tầng đám mây OpenStack sinh trên CloudLab với failure injection | ~207K dòng, 58.61MiB | ✔️ Cấp session; anomaly/normal | Hạ tầng đám mây | Đại diện cho môi trường cloud hiện đại; quy mô nhỏ-vừa giúp kiểm soát thực nghiệm; được dùng trong DeepLog gốc |
| **BGL** | Log siêu máy tính Blue Gene/L (LLNL), 131,072 processors | ~4.75M dòng, 708.76MiB | ✔️ Cấp dòng log (alert tag) | Siêu máy tính | Nhãn cấp dòng chi tiết; lỗi tự nhiên từ môi trường production; thường được dùng trong LogRAG, LightAD, SemPCA |

**Tóm tắt đặc tính đối chiếu:**

| Đặc tính | HDFS_v3 | OpenStack | BGL |
|---|---|---|---|
| Cơ chế nhãn | Fault injection có kiểm soát (17 loại) | Failure injection trên cloud | Lỗi tự nhiên production |
| Cấp độ nhãn | Trace-level | Session-level | Line-level (alert tag) |
| Quy mô | Trung bình-lớn (2.96GiB) | Nhỏ (58.61MiB) | Trung bình (708.76MiB) |
| Môi trường | Hệ thống phân tán | Đám mây (IaaS) | Siêu máy tính |
| Tỷ lệ bất thường | Có kiểm soát theo kịch bản | Cân bằng hơn do injection | ~7.3% (tự nhiên) |

### Phạm vi

- **Trong phạm vi:** phát hiện bất thường cấp trace/session/block; các phương pháp có mã nguồn công khai; 3 tập dữ liệu nêu trên từ LogHub.
- **Ngoài phạm vi:** phát hiện bất thường cấp dòng đơn lẻ (line-level) nếu pipeline không hỗ trợ; dữ liệu log ứng dụng web thương mại không công khai; đề xuất kiến trúc mô hình mới.

---

## PHẦN VI — PHƯƠNG PHÁP NGHIÊN CỨU VÀ THIẾT KẾ THỰC NGHIỆM

### 1. Quy trình tổng thể

```
Thu thập dữ liệu → Log Parsing (Drain) → Tiền xử lý thống nhất
→ Chia dữ liệu (Train/Val/Test theo thời gian)
→ Huấn luyện từng mô hình (siêu tham số từ bài báo gốc)
→ Đánh giá theo RQ1–RQ5
→ Phân tích lỗi → Kết luận và khuyến nghị
```

### 2. Tiền xử lý và log parsing

- Dùng **Drain** (chuẩn hóa từ LogPAI) làm log parser duy nhất cho tất cả phương pháp để loại bỏ biến động từ parser.
- Ghi lại tỷ lệ lỗi parsing cho từng dataset và phân tích tác động đến kết quả (liên quan RQ5).
- Chuẩn hóa timestamp; loại bỏ bản ghi thiếu trường bắt buộc theo tiêu chí được mô tả trước.

### 3. Chia dữ liệu

- **HDFS_v3 (TraceBench):** chia theo trace ID; sử dụng `normal_trace.csv` và `failure_trace.csv` đã được cung cấp sẵn; phân chia 80% train / 10% validation / 10% test, đảm bảo phân phối loại fault đa dạng trong test set.
- **OpenStack:** chia theo session (request/workflow); 80% train / 10% validation / 10% test; giữ tỷ lệ normal/anomaly nhất quán giữa các tập.
- **BGL:** chia theo thứ tự thời gian (chronological split) theo cửa sổ cố định (fixed-size window) để mô phỏng kịch bản vận hành thực tế; không dùng random shuffle để tránh data leakage.
- Ghi cố định random seed (42) cho mọi thành phần có tính ngẫu nhiên.

### 4. Hiệu chỉnh siêu tham số

- Dùng siêu tham số từ bài báo gốc làm điểm khởi đầu.
- Nếu bài báo không công bố đủ, dùng grid search giới hạn trên tập validation.
- Áp dụng cùng quy trình tuning cho TẤT CẢ phương pháp để đảm bảo công bằng.
- Ghi lại tất cả cấu hình cuối cùng trong phụ lục.

### 5. Chỉ số đánh giá

| Chỉ số | Mục đích | Áp dụng cho RQ |
|---|---|---|
| Precision, Recall, F1 | Hiệu quả phát hiện tổng thể | RQ1, RQ2, RQ4 |
| F1 tại các mức tiền tố (25/50/75/100%) | Phát hiện sớm | RQ2 |
| False Positive Rate (FPR) | Chi phí cảnh báo sai trong vận hành | RQ2, RQ5 |
| Thời gian huấn luyện (giây) | Chi phí triển khai | RQ3 |
| Độ trễ suy luận trung bình (ms/sample) | Chi phí thời gian thực | RQ3 |
| Bộ nhớ GPU/RAM (MB) | Yêu cầu phần cứng | RQ3 |
| Rank correlation (Spearman) | Độ ổn định thứ hạng | RQ4 |

### 6. Phân tích lỗi (RQ5)

- Lấy mẫu 50–100 false positive và 50–100 false negative từ mỗi mô hình trên mỗi dataset.
- Phân loại thủ công (với kiểm tra chéo) vào các nhóm: unseen log template, chuỗi quá ngắn, bất thường lặp lại, nhiễu nhãn.
- Tổng hợp tỷ lệ từng nhóm lỗi theo phương pháp.

### 7. Môi trường thực nghiệm

- **Phần cứng:** ghi rõ cấu hình GPU, RAM và CPU được dùng (ví dụ: NVIDIA RTX 3090, 32GB RAM).
- **Phần mềm:** Python 3.8/3.10, PyTorch 1.13+, transformers 4.x; ghi đầy đủ phiên bản thư viện trong `requirements.txt`.
- **Tái lập:** toàn bộ script xử lý dữ liệu, training và evaluation được lưu trong repository công khai.

---

## PHẦN VII — KẾT QUẢ DỰ KIẾN VÀ ĐÓNG GÓP

### Đầu ra dự kiến

1. **Bảng benchmark chéo** (6 phương pháp × 3 dataset: HDFS_v3 / OpenStack / BGL × Precision/Recall/F1) trong điều kiện giao thức thống nhất.
2. **Đường cong phát hiện sớm** cho mỗi phương pháp, thể hiện F1 theo tỷ lệ tiền tố chuỗi.
3. **Biểu đồ hiệu quả–chi phí** (F1 vs. latency; F1 vs. memory) giúp lựa chọn phương pháp theo ràng buộc tài nguyên.
4. **Bảng phân tích lỗi** phân loại false positive/false negative theo kiểu, kèm case study minh họa.
5. **Khuyến nghị lựa chọn phương pháp** theo điều kiện: loại log, tỷ lệ bất thường, yêu cầu phát hiện sớm, giới hạn tài nguyên.
6. **Mã nguồn pipeline benchmark** mã nguồn mở, chuẩn hóa việc chạy nhiều phương pháp log anomaly detection trên nhiều dataset.

### Đóng góp khoa học

- Bằng chứng thực nghiệm có kiểm soát về hiệu quả thực sự của các phương pháp SOTA 2022–2024 trong điều kiện so sánh công bằng.
- Phát hiện có căn cứ về mức độ suy giảm hiệu quả khi phát hiện sớm.
- Phân tích định lượng về sự đánh đổi giữa độ chính xác và chi phí tính toán.
- Nền tảng thực nghiệm cho các nghiên cứu cải tiến phương pháp ở mức độ cao hơn.

---

## PHẦN VIII — KẾ HOẠCH THỰC HIỆN

| Giai đoạn | Thời gian | Công việc | Đầu ra / Điều kiện hoàn thành |
|---|---|---|---|
| 1 | Tháng 1 | Tổng quan tài liệu chuyên sâu, xác định phạm vi, hoàn thiện RQ | Bảng tổng hợp 30+ bài báo; RQ được người hướng dẫn duyệt |
| 2 | Tháng 2 | Thu thập dataset, cài đặt và kiểm tra tái lập từng baseline | Tất cả code chạy được; pipeline tiền xử lý thống nhất hoàn tất |
| 3 | Tháng 3 | Chạy thực nghiệm RQ1 (benchmark chính) | Bảng kết quả thô RQ1; log thực nghiệm đầy đủ |
| 4 | Tháng 4 | Chạy thực nghiệm RQ2 (phát hiện sớm) và RQ3 (chi phí) | Đường cong tiền tố; bảng chi phí tính toán |
| 5 | Tháng 5 | Phân tích RQ4, RQ5; phân tích lỗi; kiểm tra tính ổn định | Báo cáo phân tích; case study lỗi; kiểm định độ tin cậy kết quả |
| 6 | Tháng 6 | Viết luận văn, hoàn thiện mã nguồn, chuẩn bị bảo vệ | Bản luận văn hoàn chỉnh; repository công khai; slide bảo vệ |

> **Dự phòng:** Nếu một baseline không thể tái lập sau 2 tuần cố gắng, ghi nhận lý do chi tiết và điều chỉnh phạm vi; không trì hoãn toàn bộ kế hoạch.

---

## PHẦN IX — CẤU TRÚC DỰ KIẾN CỦA LUẬN VĂN

```
Chương 1: Giới thiệu
  1.1. Bối cảnh và động lực nghiên cứu
  1.2. Vấn đề nghiên cứu và khoảng trống
  1.3. Mục tiêu và câu hỏi nghiên cứu
  1.4. Phạm vi và giới hạn
  1.5. Đóng góp dự kiến
  1.6. Cấu trúc luận văn

Chương 2: Cơ sở lý thuyết và tổng quan nghiên cứu
  2.1. Log hệ thống: đặc điểm, cấu trúc và vai trò
  2.2. Bài toán phát hiện bất thường log: định nghĩa và phân loại
  2.3. Quy trình log anomaly detection (parsing → grouping → detection)
  2.4. Tổng quan các phương pháp theo nhóm kiến trúc
  2.5. Bộ dữ liệu benchmark: HDFS_v3, OpenStack, BGL — đặc điểm và so sánh
  2.6. Chỉ số đánh giá và sự không đồng nhất trong tài liệu
  2.7. Khoảng trống nghiên cứu

Chương 3: Phương pháp nghiên cứu và thiết kế thực nghiệm
  3.1. Câu hỏi nghiên cứu chi tiết
  3.2. Lựa chọn và mô tả phương pháp được đánh giá
  3.3. Lựa chọn và mô tả bộ dữ liệu
  3.4. Quy trình tiền xử lý thống nhất
  3.5. Giao thức chia dữ liệu và kiểm soát data leakage
  3.6. Thiết lập huấn luyện và hiệu chỉnh siêu tham số
  3.7. Chỉ số đánh giá và định nghĩa chi tiết
  3.8. Thiết lập môi trường thực nghiệm
  3.9. Quy trình phân tích lỗi

Chương 4: Kết quả thực nghiệm
  4.1. RQ1: Hiệu quả phát hiện tổng thể
  4.2. RQ2: Khả năng phát hiện sớm
  4.3. RQ3: Chi phí tính toán
  4.4. RQ4: Độ ổn định giữa các tập dữ liệu
  4.5. RQ5: Phân tích lỗi

Chương 5: Thảo luận
  5.1. Tổng hợp phát hiện chính theo RQ
  5.2. Khuyến nghị lựa chọn phương pháp theo điều kiện thực tế
  5.3. Hạn chế của nghiên cứu
  5.4. Các mối đe dọa đối với giá trị kết luận (Threats to Validity)
  5.5. Hướng nghiên cứu tiếp theo

Chương 6: Kết luận

Tài liệu tham khảo

Phụ lục
  A. Bảng tổng hợp bài báo tham khảo
  B. Cấu hình siêu tham số chi tiết
  C. Kết quả thô đầy đủ
  D. Mô tả pipeline tái lập (hướng dẫn cài đặt và chạy)
  E. Danh sách trường hợp lỗi trong phân tích lỗi
```

---

## PHẦN X — TÀI LIỆU THAM KHẢO CHÍNH

1. **LogFormer** — *LogFormer: A Pre-train and Tuning Pipeline for Log Anomaly Detection*, ICASSP 2023.
3. **SemPCA** — *SemPCA: Integrating Semantic Information into PCA for Anomaly Detection on System Logs*, ICSE 2023.
4. **LightAD** — *Deep Learning or Classical Machine Learning? An Empirical Study on Log-Based Anomaly Detection*, ICSE 2024.
5. **Logs2Graph** — *Graph Neural Networks based Log Anomaly Detection and Explanation*, ICSE 2024 Companion.
6. **LogRAG** — *Leveraging RAG-Enhanced Large Language Model for Semi-Supervised Log Anomaly Detection*, ISSRE 2024.
7. **CoLog** — *Collaborative Transformer for Log Anomaly Detection*.
8. Du et al., *DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning*, CCS 2017.
9. Meng et al., *LogAnomaly: Unsupervised Detection of Sequential and Quantitative Anomalies in Unstructured Logs*, IJCAI 2019.
10. Zhang et al., *Robust Log-Based Anomaly Detection on Unstable Log Data*, FSE 2019.
11. Guo et al., *LogBERT: Log Anomaly Detection via BERT*, IJCNN 2021.
13. Zhu et al., *Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics*, ISSRE 2023. (Nguồn: https://github.com/logpai/loghub)
14. Zhou et al., *TraceBench: An Open Data Set for Trace-oriented Monitoring*, CloudCom 2014. (Nguồn HDFS_v3)
15. Oliner & Stearley, *What Supercomputers Say: A Study of Five System Logs*, DSN 2007. (Nguồn BGL)

---

> **Ghi chú:** Đề cương này theo hướng nghiên cứu Cấp độ 1 (đánh giá thực nghiệm/benchmarking). Tính mới nằm ở giao thức đánh giá thống nhất, phạm vi phương pháp mở rộng (bao gồm GNN và RAG+LLM), và phân tích phát hiện sớm chưa từng được thực hiện đồng thời trên nhóm phương pháp này. Có thể điều chỉnh theo biểu mẫu và yêu cầu của trường/khoa.
