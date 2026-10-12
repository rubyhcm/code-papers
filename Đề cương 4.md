# Phân tích Chi tiết Cấp độ 1: Đánh giá Thực nghiệm (Empirical Study) & Benchmarking

Trong nghiên cứu khoa học, đặc biệt ở lĩnh vực Khoa học Máy tính và Dữ liệu, Cấp độ 1 thường bị hiểu lầm là "quá dễ" hoặc "không có tính hàn lâm". Tuy nhiên, một nghiên cứu đánh giá thực nghiệm (Empirical Study) xuất sắc đòi hỏi sự tỉ mỉ, khách quan và tư duy phân tích sâu sắc.

Dưới đây là mô tả chi tiết về Cấp độ 1, lấy bối cảnh bài toán phân tích và xử lý dữ liệu Log hệ thống.

---

## 1. Bản chất của Nghiên cứu Cấp độ 1
Ở cấp độ này, bạn **không** tạo ra một phương pháp, thuật toán hay kiến trúc mới. Trọng tâm của bạn là **đặt các phương pháp ĐÃ CÓ lên bàn cân** dưới một lăng kính hệ thống, khoa học và công bằng.

Câu hỏi nghiên cứu cốt lõi thường là:
*   *Thuật toán A, B, C hoạt động như thế nào trên các loại dữ liệu D, E, F?*
*   *Đâu là điểm mạnh, điểm yếu thực sự của từng phương pháp khi triển khai thực tế?*
*   *Phương pháp nào phù hợp nhất cho bối cảnh/ràng buộc nào (ví dụ: cần tốc độ nhanh vs. cần độ chính xác tuyệt đối)?*

## 2. Quy trình thực hiện (Workflow) tiêu chuẩn
Để một nghiên cứu Cấp độ 1 đạt chuẩn xuất bản (ví dụ: một bài Survey hoặc Benchmark paper), bạn cần trải qua các bước nghiêm ngặt sau:

### Bước 1: Xác định không gian đánh giá (Scope & Baseline)
*   **Chọn phương pháp (Baselines):** Bạn phải chọn ra các phương pháp tiêu biểu nhất (State-of-the-Art) hoặc phổ biến nhất. *Ví dụ: Để đánh giá Log Parsing, bạn chọn Drain, Spell, AEL và MoLFI.*
*   **Xác định độ đo (Metrics):** Không chỉ đo 1-2 tiêu chí. Cần đo toàn diện. *Ví dụ: Parsing Accuracy (Độ chính xác), Robustness (Tính bền vững khi log thay đổi), Efficiency (Thời gian chạy, RAM tiêu thụ).*

### Bước 2: Chuẩn bị Dữ liệu (Datasets)
*   Nghiên cứu Cấp độ 1 sẽ vô giá trị nếu chỉ chạy trên 1 tập dữ liệu nhỏ.
*   Bạn cần thu thập nhiều tập dữ liệu mang các đặc tính khác nhau. *Ví dụ: Log từ Hệ thống phân tán (HDFS), Siêu máy tính (BGL, Thunderbird), Hệ điều hành (Linux, Windows) hay Ứng dụng (Apache, Nginx).*

### Bước 3: Thiết lập Môi trường & Tái tạo (Reproducibility)
*   Đây là bước "đau khổ" nhất. Bạn phải cài đặt lại mã nguồn của các tác giả khác (thường thiếu tài liệu hoặc bị lỗi).
*   Đảm bảo cấu hình môi trường phần cứng/phần mềm giống hệt nhau cho tất cả các phương pháp để đảm bảo tính công bằng (Fair comparison).

### Bước 4: Thực thi và Thu thập kết quả
*   Chạy thử nghiệm nhiều lần (cross-validation, random seed) để lấy giá trị trung bình và độ lệch chuẩn, tránh yếu tố may rủi.

### Bước 5: Phân tích sâu (In-depth Analysis) - Nơi tạo ra giá trị Khoa học
Đây là bước phân biệt một báo cáo kỹ thuật thông thường và một bài báo khoa học Cấp độ 1. Bạn không chỉ lập bảng kết quả, mà phải giải thích **TẠI SAO**:
*   Tại sao thuật toán A chạy tốt trên HDFS nhưng lại thất bại thảm hại trên BGL? (Phân tích đặc thù cấu trúc log).
*   Tại sao thuật toán B nhanh nhưng tốn nhiều RAM?
*   Phát hiện ra các trường hợp sai số điển hình (Error analysis/Case studies).

---

## 3. Giá trị đóng góp (Contribution) của Cấp độ 1
Dù không đề xuất cái mới, Cấp độ 1 đóng góp cực lớn cho cộng đồng:
1.  **Thiết lập Baseline chuẩn mực:** Tạo ra một bộ khung đo lường chuẩn (Benchmark) để các nhà nghiên cứu đi sau (Cấp độ 2 & 3) có cơ sở so sánh đáng tin cậy. (Ví dụ tiêu biểu: Dự án *LogPAI* đã tạo ra benchmark rất nổi tiếng cho log parsing).
2.  **Hướng dẫn Thực hành (Practical Guidelines):** Giúp các kỹ sư trong ngành công nghiệp quyết định nhanh chóng nên dùng công cụ nào cho hệ thống của họ.
3.  **Vạch trần "Góc khuất":** Nhiều thuật toán công bố kết quả rất cao trong bài báo gốc vì họ chỉ chọn bộ dữ liệu "quen thuộc". Nghiên cứu Cấp độ 1 sẽ thử nghiệm chéo và chỉ ra giới hạn thực sự của chúng.
4.  **Chỉ ra hướng nghiên cứu tương lai:** Từ việc phân tích các nhược điểm chung của các phương pháp hiện tại, tác giả vạch ra con đường cho các nghiên cứu Cấp độ 2 và 3.

---

## 4. Những cạm bẫy cần tránh (Pitfalls)
*   **So sánh không công bằng (Unfair Comparison):** Tối ưu hóa tham số (hyperparameters) cho phương pháp A nhưng lại để tham số mặc định cho phương pháp B.
*   **Thiếu phân tích sâu:** Bài báo chỉ có toàn bảng biểu và biểu đồ, kết luận kiểu "A lớn hơn B" mà không giải thích nguyên nhân đằng sau lớp thuật toán.
*   **Độ đo thiên lệch:** Sử dụng các độ đo chỉ có lợi cho một loại thuật toán cụ thể.

## 5. Kết luận
Cấp độ 1 là **bước đệm bắt buộc**. Rất khó để làm tốt Cấp độ 2 (Cải tiến) hoặc Cấp độ 3 (Đột phá) nếu bạn chưa tự tay thực hiện các đánh giá thực nghiệm Cấp độ 1 để thực sự "cảm" được dữ liệu và hiểu tận gốc rễ những khiếm khuyết của các phương pháp hiện hành.