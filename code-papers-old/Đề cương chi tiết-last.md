# ĐỀ CƯƠNG CHI TIẾT LUẬN VĂN THẠC SĨ

## Đánh giá thực nghiệm các phương pháp phát hiện bất thường dựa trên dữ liệu log: Từ học máy cổ điển đến mô hình ngôn ngữ lớn

_An Empirical Evaluation of Log-Based Anomaly Detection Methods: From Classical Machine Learning to Large Language Models_

---

## 1. ĐẶT VẤN ĐỀ

### 1.1. Bối cảnh nghiên cứu

Các hệ thống phần mềm hiện đại (hệ phân tán, siêu máy tính, đám mây, hệ điều hành) sinh ra khối lượng log khổng lồ. Log là nguồn dữ liệu quan trọng bậc nhất để giám sát vận hành, phát hiện sự cố và bảo đảm an ninh hệ thống. Phát hiện bất thường dựa trên log (_log-based anomaly detection – LogAD_) là bài toán tự động phân loại hoặc gắn cờ những bản ghi/chuỗi sự kiện bất thường nhằm rút ngắn thời gian phát hiện lỗi, giảm thiểu thời gian dừng dịch vụ và cảnh báo sớm cho đội vận hành.

Trong vài năm gần đây, bài toán LogAD chứng kiến sự bùng nổ về số lượng phương pháp, đặc biệt từ năm 2024 trở lại đây, với các xu hướng rất khác nhau về mặt kỹ thuật:

- **Học máy cổ điển** được đánh giá lại và cho thấy hiệu quả đáng ngạc nhiên so với học sâu (LightAD – ICSE'24).
- **Học sâu tuần tự** tiếp tục được cải tiến bằng kỹ thuật pre-train + fine-tune (LogFormer – AAAI'24).
- **Transformer đa phương thức** phối hợp nhiều khía cạnh của log (CoLog – Scientific Reports 2025).
- **Mạng nơ-ron đồ thị** biểu diễn log thành đồ thị có hướng, có trọng số (Logs2Graph – ICSE'24 Companion).
- **Mô hình ngôn ngữ lớn (LLM) kết hợp RAG** được đưa vào bài toán LogAD bán giám sát (LogRAG – ISSRE'24).
- **Phương pháp thống kê đơn giản hóa** (PCA cải tiến) vẫn là baseline quan trọng (SemPCA).

Mỗi phương pháp thường được công bố với một bộ dữ liệu, một giao thức đánh giá, một môi trường và một cách tiền xử lý riêng, dẫn đến khó khăn trong việc đối chiếu trực tiếp kết quả giữa chúng.

### 1.2. Vấn đề nghiên cứu

Hiện nay chưa có một đánh giá thực nghiệm thống nhất đặt **đồng thời sáu phương pháp SOTA giai đoạn 2024–2025 nêu trên** lên cùng một nền tảng so sánh: cùng bộ dữ liệu, cùng quy trình tiền xử lý, cùng phép chia dữ liệu và cùng bộ chỉ số đánh giá. Các công bố gốc chỉ so sánh từng nhóm nhỏ phương pháp trong phạm vi bài báo của mình, vì vậy chưa trả lời được một cách có hệ thống các câu hỏi:

- Liệu những kết quả cao được báo cáo có còn giữ vững khi tái lập trên môi trường độc lập và so sánh chéo giữa các họ phương pháp?
- Đâu là sự đánh đổi thực sự giữa độ chính xác, chi phí tính toán và khả năng triển khai giữa các họ kỹ thuật?
- Một họ phương pháp có ưu thế trong điều kiện dữ liệu nào (log hệ phân tán, log siêu máy tính, log đám mây)?

### 1.3. Ý nghĩa khoa học và thực tiễn

**Về khoa học:** cung cấp một bằng chứng so sánh đáng tin cậy, có thể tái lập cho cộng đồng nghiên cứu LogAD, giúp chuẩn hóa giao thức đánh giá và chỉ ra hướng nghiên cứu tiếp theo.

**Về thực tiễn:** đưa ra khuyến nghị lựa chọn phương pháp có điều kiện (theo loại dữ liệu, ràng buộc tài nguyên, yêu cầu về độ trễ và khả năng giải thích), giúp kỹ sư vận hành quyết định nhanh nên triển khai công cụ nào.

### 1.4. Mục tiêu nghiên cứu

**Mục tiêu tổng quát:** Đánh giá một cách có hệ thống và công bằng hiệu quả phát hiện bất thường, chi phí tính toán, tính ổn định và khả năng giải thích của sáu phương pháp LogAD đại diện cho năm họ kỹ thuật, trên các bộ dữ liệu log chuẩn, trong một giao thức thực nghiệm mô tả rõ và có thể tái lập.

**Mục tiêu cụ thể:**

1. Tái lập thành công mã nguồn của sáu phương pháp trong môi trường chung.
2. Xây dựng một pipeline tiền xử lý và đánh giá thống nhất cho các bộ dữ liệu dùng chung; mở rộng pipeline đầu vào để cả sáu phương pháp chạy được trên HDFS_v3, BGL và OpenStack.
3. Đo lường và so sánh hiệu quả phát hiện (P/R/F1/PR-AUC) và chi phí tính toán (thời gian huấn luyện, suy luận, bộ nhớ).
4. Phân tích độ ổn định giữa các bộ dữ liệu, phân tích lỗi và khả năng phát hiện sớm.
5. Rút ra khuyến nghị lựa chọn phương pháp theo điều kiện sử dụng.

### 1.5. Câu hỏi nghiên cứu

- **RQ1 (Hiệu quả phát hiện tổng thể):** Sáu phương pháp đạt hiệu quả phát hiện bất thường (Precision, Recall, F1, PR-AUC) như thế nào trên các bộ dữ liệu log được lựa chọn khi được đánh giá theo cùng một giao thức?
- **RQ2 (Tính ổn định giữa các bộ dữ liệu):** Thứ hạng và hiệu quả của các phương pháp có thay đổi giữa các bộ dữ liệu có đặc tính khác nhau (hệ phân tán, siêu máy tính, đám mây) hay không?
- **RQ3 (Đánh đổi hiệu năng – chi phí tính toán):** Các phương pháp đánh đổi độ chính xác với chi phí tính toán (thời gian huấn luyện, độ trễ suy luận, bộ nhớ) như thế nào, đặc biệt giữa nhóm ML cổ điển, học sâu, GNN và LLM/RAG?
- **RQ4 (Khả năng phát hiện sớm):** Hiệu quả của các phương pháp thay đổi như thế nào khi chỉ quan sát được một phần chuỗi log (10%, 25%, 50%, 75%, 100%)?
- **RQ5 (Phân tích lỗi và khả năng giải thích):** Những kiểu trường hợp nào thường bị bỏ sót (false negative) hoặc gây cảnh báo sai (false positive), và các lỗi đó liên hệ thế nào với đặc tính dữ liệu; phương pháp nào hỗ trợ giải thích quyết định?

### 1.6. Phạm vi và giả định

- **Phạm vi phương pháp:** sáu phương pháp có sẵn mã nguồn trong dự án: CoLog, LightAD, LogFormer, LogRAG, Logs2Graph, SemPCA. Không đề xuất thuật toán mới.
- **Phạm vi dữ liệu:** ba bộ dữ liệu chính từ LogHub: HDFS_v3, BGL và OpenStack (xem Mục 3.2).
- **Ngoài phạm vi:** không đánh giá các phương pháp LogAD khác không có mã nguồn trong dự án; không so sánh số liệu lấy trực tiếp từ bài báo gốc mà không tái lập; không tinh chỉnh mô hình bằng tập kiểm thử.

### 1.7. Đóng góp dự kiến

1. Một **benchmark có thể tái lập** gồm mã nguồn, cấu hình, script tiền xử lý và đánh giá thống nhất cho sáu phương pháp trên HDFS_v3, BGL và OpenStack, bao gồm phần mở rộng pipeline đầu vào cho các phương pháp chưa hỗ trợ sẵn.
2. **Bảng kết quả và phân tích định lượng** so sánh hiệu quả phát hiện và chi phí tính toán.
3. **Đường cong phát hiện sớm** theo tỷ lệ tiền tố chuỗi log.
4. **Phân tích lỗi có cấu trúc** (taxonomy của false positive/false negative) gắn với đặc tính dữ liệu.
5. **Khuyến nghị thực tiễn** lựa chọn phương pháp theo loại dữ liệu, ràng buộc tài nguyên và yêu cầu vận hành.

---

## 2. CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN NGHIÊN CỨU

### 2.1. Khái niệm cơ bản

- Log hệ thống, mẫu log (_log template/event_), chuỗi sự kiện, phiên/session/block.
- Bất thường điểm (_point anomaly_) và bất thường tập thể (_collective anomaly_).
- Các dạng bài toán LogAD: phân loại, phát hiện tuần tự, không giám sát/bán giám sát, trực tuyến và phát hiện sớm.
- Vai trò của log parsing (Drain) và ảnh hưởng của lỗi parsing tới downstream task.

### 2.2. Phân loại các họ phương pháp

| Họ kỹ thuật                | Đại diện trong dự án | Ý tưởng cốt lõi                                                         |
| -------------------------- | -------------------- | ----------------------------------------------------------------------- |
| Thống kê / học máy cổ điển | SemPCA, LightAD      | Biểu diễn đặc trưng (PCA/đếm) + phân loại đơn giản (KNN, DT, SLFN)      |
| Học sâu tuần tự            | LogFormer            | Pre-train + fine-tune trên chuỗi sự kiện log                            |
| Transformer đa phương thức | CoLog                | Mã hóa cộng tác nhiều modality của log, học tương tác liên phương thức  |
| Mạng nơ-ron đồ thị         | Logs2Graph           | Biểu diễn nhóm log thành đồ thị có hướng/trọng số, phát hiện cấp đồ thị |
| LLM + RAG bán giám sát     | LogRAG               | One-class (DeepSVDD) phát hiện sơ bộ, LLM+RAG tái đánh giá để giảm FP   |

### 2.3. Tổng quan sáu phương pháp được đánh giá

| #   | Phương pháp    | Công bố                 | Kiến trúc / cơ chế                                                                                                                 | Kiểu học                   | Dữ liệu hỗ trợ (theo mã nguồn)                                       |
| --- | -------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------- |
| 1   | **CoLog**      | Scientific Reports 2025 | Collaborative Transformers + Multi-head Impressed Attention + Modality Adaptation Layer; phát hiện cả point lẫn collective anomaly | Giám sát (phân loại)       | Casper-RW, DFRWS (Jhuisi, Nssal), Honeynet 7, Zookeeper, Hadoop, BGL |
| 2   | **LightAD**    | ICSE 2024               | KNN, Decision Tree, SLFN + tiền xử lý đơn giản + tự chọn mô hình                                                                   | Giám sát (ML cổ điển)      | HDFS, BGL, Spirit, Liberty, Thunderbird                              |
| 3   | **LogFormer**  | AAAI 2024               | Pre-train + tuning pipeline trên Transformer                                                                                       | Tự giám sát + tinh chỉnh   | LogHub (HDFS, BGL, Thunderbird, Spirit, OpenStack, …)                |
| 4   | **LogRAG**     | ISSRE 2024              | DeepSVDD/DeepOC (one-class) + RAG + LLM tái đánh giá                                                                               | Bán giám sát               | BGL, Spirit                                                          |
| 5   | **Logs2Graph** | ICSE 2024 Companion     | OCDiGCN (One-Class Digraph Inception GCN), phát hiện cấp đồ thị + giải thích cấp node                                              | Không giám sát (one-class) | HDFS, Hadoop, Spirit, BGL, Thunderbird                               |
| 6   | **SemPCA**     | Empirical study         | PCA++ (PCA cải tiến) trên biểu diễn log                                                                                            | Không giám sát             | HDFS, BGL, Spirit                                                    |

> _Ghi chú: thông tin "kiểu học" được tổng hợp từ README/kiến trúc mã nguồn; cần đối chiếu chính xác với bài báo gốc khi viết tổng quan chính thức._

### 2.4. Các bộ dữ liệu đánh giá

Ba bộ dữ liệu chính được chọn từ LogHub, bao phủ ba bối cảnh hệ thống khác nhau:

| Bộ dữ liệu    | Loại hệ thống                | Đặc điểm                                          |
| ------------- | ---------------------------- | ------------------------------------------------- |
| **HDFS_v3**   | Hệ phân tán (Hadoop HDFS)    | Log namenode, nhãn theo block, chuỗi sự kiện ngắn |
| **BGL**       | Siêu máy tính (BlueGene/L)   | Log hệ thống, nhãn theo dòng log, chuỗi dài       |
| **OpenStack** | Nền tảng đám mây (OpenStack) | Log ứng dụng/đám mây, nhãn theo instance          |

Ma trận hỗ trợ giữa các phương pháp và bộ dữ liệu (theo mã nguồn hiện tại):

| Phương pháp | HDFS_v3                          | BGL | OpenStack |
| ----------- | -------------------------------- | --- | --------- |
| CoLog       | – (dùng Hadoop, không phải HDFS) | ✓   | ✗         |
| LightAD     | ✓                                | ✓   | ✗         |
| LogFormer   | ✓                                | ✓   | ✓         |
| LogRAG      | ✗                                | ✓   | ✗         |
| Logs2Graph  | ✓                                | ✓   | ✗         |
| SemPCA      | ✓                                | ✓   | ✗         |

> **Quyết định thiết kế:** để so sánh đủ sáu phương pháp trên cả ba bộ dữ liệu, luận văn sẽ **mở rộng pipeline đầu vào** cho các phương pháp chưa hỗ trợ OpenStack (CoLog, LightAD, LogRAG, Logs2Graph, SemPCA), đồng thời bổ sung HDFS_v3 cho LogRAG và ánh xạ Hadoop→HDFS cho CoLog. Chi tiết tại Mục 3.3.

### 2.5. Các chỉ số đánh giá

- **Hiệu quả phát hiện:** Precision, Recall, F1-score, PR-AUC (khi mô hình cho điểm số/ngưỡng), False Positive Rate.
- **Chi phí tính toán:** thời gian huấn luyện, độ trễ suy luận, thông lượng, bộ nhớ đỉnh.
- **Phát hiện sớm:** F1/Recall tại các tiền tố 10%, 25%, 50%, 75%, 100%.
- **Khả năng giải thích:** đánh giá định tính đối với Logs2Graph (giải thích cấp node) và LogRAG (lý do tái phân loại qua LLM).

### 2.6. Khoảng trống nghiên cứu

- Các công bố gốc dùng giao thức, môi trường và tiền xử lý không đồng nhất nên không đối chiếu trực tiếp được.
- Chưa có đánh giá nào đặt đồng thời cả năm họ kỹ thuật (cổ điển, học sâu, transformer đa phương thức, GNN, LLM/RAG) lên cùng một benchmark.
- Vấn đề đánh đổi giữa chi phí của LLM/RAG so với phương pháp nhẹ (LightAD, SemPCA) chưa được làm rõ trong cùng điều kiện.
- Khả năng phát hiện sớm và khả năng giải thích thường bị bỏ qua hoặc đo không nhất quán giữa các công bố.
- Bộ dữ liệu đám mây OpenStack ít được các phương pháp hỗ trợ và đánh giá so với HDFS/BGL, để lại khoảng trống về tính tổng quát hóa trên log đám mây.

---

## 3. PHƯƠNG PHÁP NGHIÊN CỨU VÀ THIẾT KẾ THỰC NGHIỆM

### 3.1. Loại hình nghiên cứu

Nghiên cứu đánh giá thực nghiệm / benchmarking (Cấp độ 1), tuân theo nguyên tắc của _ACM SIGSOFT Empirical Standards_ cho loại nghiên cứu đánh giá kỹ thuật phần mềm: câu hỏi rõ ràng, giao thức mô tả được, kiểm soát sai lệch, công khai giới hạn và bảo đảm tái lập.

### 3.2. Tiêu chí lựa chọn baseline

Sáu phương pháp được chọn vì thỏa mãn đồng thời:

1. **Tính đại diện:** bao phủ năm họ kỹ thuật khác biệt về cơ chế.
2. **Tính thời sự:** đều là công bố 2024–2025 (SOTA gần nhất).
3. **Khả năng tái lập:** có mã nguồn mở đầy đủ trong dự án.
4. **Tính so sánh:** có giao thoa bộ dữ liệu (HDFS_v3, BGL, OpenStack) để đánh giá chung.

Mỗi baseline được ghi nhận đầy đủ: trích dẫn gốc, nhóm phương pháp, kiểu học, yêu cầu nhãn, đầu vào/đầu ra, tiền xử lý, mã nguồn/commit, điểm mạnh – hạn chế đã báo cáo, rủi ro tái lập.

### 3.3. Lựa chọn và mô tả bộ dữ liệu

- **Nguồn:** LogHub (logpai/loghub) cho HDFS_v3, BGL và OpenStack; ghi nhận đúng phiên bản/commit dataset khi tải.
- **Ghi nhận:** số bản ghi, tỷ lệ bất thường, cấp độ nhãn (dòng/chuỗi/block/instance).
- **Cấp độ nhãn được chú ý đặc biệt** vì ảnh hưởng tới cách tính metric và khả năng đo phát hiện sớm: HDFS_v3 theo block, BGL theo dòng log, OpenStack theo instance.
- **Đồng bộ hóa pipeline đầu vào (mở rộng mã nguồn):** để bảo đảm cả sáu phương pháp chạy được trên cả ba bộ dữ liệu, luận văn bổ sung module tiền xử lý/xây dựng mẫu cho OpenStack (CoLog, LightAD, LogRAG, Logs2Graph, SemPCA) và HDFS_v3 (LogRAG; ánh xạ Hadoop→HDFS cho CoLog). Phần mở rộng này được mô tả rõ, đối chiếu với giao thức gốc của từng phương pháp và ghi nhận như một phần của gói tái lập.

### 3.4. Tiền xử lý và xây dựng mẫu

- Log parsing bằng **Drain** cho các phương pháp cần template (nhất quán với LogFormer, LogRAG, Logs2Graph, SemPCA).
- Đối với các phương pháp có tiền xử lý riêng (CoLog dùng embedding sentence-transformer thay vì log template), tôn trọng thiết kế gốc nhưng **ghi rõ khác biệt** để tránh so sánh bất công.
- Gom nhóm log thành chuỗi/session theo quy tắc được mô tả rõ; xử lý dữ liệu trùng lặp, thiếu và mẫu không hợp lệ.

### 3.5. Chiến lược chia dữ liệu

- Tách **train / validation / test**; ưu tiên chia theo thời gian để mô phỏng triển khai thực tế và hạn chế rò rỉ.
- Chỉ dùng train để học tham số, validation để chọn siêu tham số/ngưỡng, test để đánh giá cuối cùng.
- Kiểm tra mẫu trùng lặp/chuỗi chồng lấn giữa các tập; không dùng thông tin xuất hiện sau thời điểm dự đoán trong thí nghiệm phát hiện sớm.

### 3.6. Cấu hình, huấn luyện và hiệu chỉnh

- Cố định **seed ngẫu nhiên** chung cho mọi phương pháp; chạy lặp nhiều lần khi có yếu tố ngẫu nhiên và báo cáo trung bình ± độ lệch chuẩn.
- Lựa chọn siêu tham số/ngưỡng theo quy trình định trước (grid/random search) áp dụng công bằng trên mọi baseline; ngưỡng chỉ chọn trên validation.
- Ghi lại đầy đủ cấu hình, lệnh chạy, phiên bản thư viện và phần cứng.

### 3.7. Chỉ số đánh giá

Mỗi chỉ số được định nghĩa rõ đơn vị tính và gắn với RQ tương ứng:

| Chỉ số                          | Đơn vị / cách tính                     | RQ liên quan |
| ------------------------------- | -------------------------------------- | ------------ |
| Precision, Recall, F1           | Cấp mẫu (block/chuỗi/dòng tùy dataset) | RQ1          |
| PR-AUC                          | Khi mô hình cho điểm số                | RQ1          |
| False Positive Rate             | Tỷ lệ mẫu thường bị báo bất thường     | RQ1, RQ5     |
| Thời gian huấn luyện / suy luận | giây (trên cùng phần cứng)             | RQ3          |
| Bộ nhớ đỉnh                     | MB/GB                                  | RQ3          |
| F1/Recall theo tiền tố          | Tại 10%, 25%, 50%, 75%, 100% chuỗi     | RQ4          |
| Taxonomy lỗi FP/FN              | Phân nhóm có tiêu chí rõ               | RQ5          |

### 3.8. Thiết kế đánh giá phát hiện sớm (RQ4)

- Định nghĩa "sớm" bằng tỷ lệ tiền tố được quan sát (10%, 25%, 50%, 75%, 100%).
- Chỉ áp dụng với dataset có nhãn và cấu trúc cho phép xác định dự đoán tại từng tiền tố; tránh dùng thông tin xuất hiện sau thời điểm giả định phát hiện.
- Vẽ đường cong hiệu quả theo tiền tố và phân tích đánh đổi giữa phát hiện sớm và cảnh báo sai.

### 3.9. Phân tích lỗi và khả năng giải thích (RQ5)

- Trích xuất các mẫu FP/FN của từng phương pháp; phân nhóm theo: mẫu log chưa gặp, chuỗi ngắn/dài, dữ liệu nhiễu, mất cân bằng lớp.
- Đối chiếu với đặc tính dữ liệu; dùng ví dụ cụ thể và thống kê theo nhóm.
- Đánh giá định tính khả năng giải thích của Logs2Graph (node quan trọng) và LogRAG (lý do tái phân loại từ LLM).

### 3.10. Môi trường thực nghiệm và quản lý kết quả

- Thống nhất phần cứng (GPU/CUDA), hệ điều hành, Python, PyTorch và các thư viện quan trọng cho mọi phương pháp khi có thể; ghi rõ ngoại lệ (ví dụ LogRAG cần API LLM, SemPCA giới hạn scikit-learn ≤ 0.24).
- Lưu trữ kết quả thô, cấu hình, seed, log chạy và script tính metric/tạo biểu đồ; báo cáo cả lần chạy thất bại.

### 3.11. Kiểm soát sai lệch, độ tin cậy và tái lập

- Ngăn rò rỉ dữ liệu giữa train/validation/test.
- So sánh công bằng: giữ giống nhau điều kiện có thể; tôn trọng yêu cầu đầu vào riêng và ghi rõ khác biệt.
- Báo cáo tính ngẫu nhiên và độ biến thiên; tránh khẳng định nhân quả khi thiết kế chỉ cho thấy mối liên hệ.
- Cung cấp gói tái lập: mã, cấu hình, script, tài liệu; nêu rõ giới hạn chia sẻ (API key, giấy phép dữ liệu).

---

## 4. KẾT QUẢ VÀ ĐÓNG GÓP DỰ KIẾN

### 4.1. Kết quả thực nghiệm dự kiến

- Bảng benchmark hiệu quả phát hiện (P/R/F1/PR-AUC) theo dataset × phương pháp.
- Bảng chi phí tính toán (thời gian huấn luyện, suy luận, bộ nhớ).
- Đường cong phát hiện sớm theo tỷ lệ tiền tố.
- Taxonomy lỗi FP/FN kèm ví dụ và thống kê theo nhóm.
- So sánh định tính khả năng giải thích giữa Logs2Graph và LogRAG.

### 4.2. Các câu hỏi mà kết quả dự kiến trả lời

| RQ  | Đầu ra dự kiến                                  |
| --- | ----------------------------------------------- |
| RQ1 | Bảng chỉ số và xếp hạng hiệu quả phát hiện      |
| RQ2 | Phân tích thay đổi thứ hạng giữa các bộ dữ liệu |
| RQ3 | Bảng đánh đổi độ chính xác – chi phí tính toán  |
| RQ4 | Đường cong hiệu quả theo tiền tố chuỗi log      |
| RQ5 | Taxonomy lỗi và đánh giá khả năng giải thích    |

### 4.3. Đóng góp thực nghiệm dự kiến

1. Bằng chứng so sánh đáng tin cậy trên giao thức minh bạch, có thể tái lập.
2. Hiểu biết về điều kiện mà từng họ phương pháp phát huy hoặc suy giảm hiệu quả.
3. Làm rõ sự khác biệt giữa hiệu quả trên toàn chuỗi và hiệu quả khi chỉ có tiền tố (phát hiện sớm).
4. Phân tích đánh đổi chi phí giữa LLM/RAG và phương pháp nhẹ.
5. Khuyến nghị lựa chọn phương pháp theo loại dữ liệu và ràng buộc vận hành.

### 4.4. Giới hạn dự kiến

- Kết quả chỉ đại diện cho sáu phương pháp và ba bộ dữ liệu được đánh giá, không suy rộng cho mọi hệ thống.
- Số đo hiệu năng trên một môi trường phần cứng không đại diện cho mọi môi trường triển khai.
- Một số phương pháp có yêu cầu đặc thù (API LLM cho LogRAG, giới hạn scikit-learn cho SemPCA) có thể làm giảm mức độ đồng nhất của môi trường.
- Các phép đo phát hiện sớm chỉ áp dụng khi nhãn và cấu trúc dữ liệu cho phép.
- Việc mở rộng pipeline cho các phương pháp chưa hỗ trợ OpenStack/HDFS_v3 có thể tạo khác biệt tiền xử lý so với thiết kế gốc; cần ghi rõ và kiểm chứng để tránh so sánh thiếu công bằng.

---

## 5. KẾ HOẠCH THỰC HIỆN (dự kiến 6 tháng)

| Giai đoạn | Công việc                                                             | Đầu ra / điều kiện hoàn thành                                   |
| --------- | --------------------------------------------------------------------- | --------------------------------------------------------------- |
| Tháng 1   | Tổng quan tài liệu, xác định phạm vi, xây dựng RQ                     | Bảng tổng hợp 6 phương pháp + RQ được chốt                      |
| Tháng 2   | Chọn dataset, chuẩn hóa tiền xử lý và giao thức                       | Pipeline tiền xử lý + giao thức được ghi lại                    |
| Tháng 3   | Tái lập 6 phương pháp; mở rộng pipeline đầu vào cho OpenStack/HDFS_v3 | Từng baseline chạy được trên cả 3 dataset, kết quả sơ bộ hợp lệ |
| Tháng 4   | Chạy benchmark chính                                                  | Kết quả thô, cấu hình, log, bảng kết quả ban đầu                |
| Tháng 5   | Phân tích sâu (RQ2–RQ5), kiểm tra độ ổn định                          | Phân tích RQ, kiểm tra độ tin cậy và giới hạn                   |
| Tháng 6   | Viết, rà soát, hoàn thiện mã và tài liệu tái lập                      | Bản luận văn + phụ lục thực nghiệm                              |

---

## 6. TÀI LIỆU THAM KHẢO (dự kiến)

1. Nasirzadeh, M., Tahmoresnezhad, J., & Rashidi-Khazaee, P. (2025). _A unified framework for detecting point and collective anomalies in operating system logs via collaborative transformers._ Scientific Reports, 15, Article 27693. (CoLog)
2. Yu, B., Yao, J., Fu, Q., et al. (2024). _Deep Learning or Classical Machine Learning? An Empirical Study on Log-Based Anomaly Detection._ ICSE 2024. (LightAD)
3. Guo, H., Yang, J., Liu, J., et al. (2024). _LogFormer: A Pre-train and Tuning Pipeline for Log Anomaly Detection._ AAAI 2024.
4. _Leveraging RAG-Enhanced Large Language Model for Semi-Supervised Log Anomaly Detection._ (2024). ISSRE 2024. (LogRAG)
5. Li, Z., Shi, J., & van Leeuwen, M. (2024). _Graph Neural Networks based Log Anomaly Detection and Explanation._ ICSE-Companion 2024. (Logs2Graph)
6. _Try with Simpler – An Evaluation of Improved Principal Component Analysis in Log-based Anomaly Detection._ (SemPCA)
7. He, P., Zhu, J., Zheng, Z., & Lyu, M. R. (2017). _Drain: An Online Log Parsing Approach with Fixed Depth Tree._ ICWS 2017.
8. LogPAI. _LogHub — A Large Collection of System Log Datasets._ https://github.com/logpai/loghub (bộ dữ liệu HDFS_v3, BGL, OpenStack).
9. ACM SIGSOFT Empirical Standards (dùng cho thiết kế và báo cáo nghiên cứu thực nghiệm).

---

## 7. PHỤ LỤC DỰ KIẾN

- Bảng trích xuất đặc điểm 6 phương pháp (kiến trúc, kiểu học, dữ liệu, metric, hạn chế).
- Bảng mô tả bộ dữ liệu (nguồn, quy mô, tỷ lệ bất thường, cấp độ nhãn, giấy phép).
- Cấu hình chi tiết, siêu tham số, seed và lệnh chạy từng baseline.
- Bảng kết quả thô và script tạo biểu đồ.
- Checklist thực nghiệm và các mối đe dọa tới tính hợp lệ.
