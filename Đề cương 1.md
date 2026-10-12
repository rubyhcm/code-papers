# Tiêu chí & Cấu trúc Đề cương Luận văn Thạc sĩ: Nghiên cứu Thực nghiệm (Cấp độ 1)

Đối với bậc Thạc sĩ, hội đồng đánh giá sẽ yêu cầu rất cao về **độ sâu của phân tích** và **quy mô của thực nghiệm** nếu bạn chọn làm nghiên cứu Cấp độ 1 (không đề xuất phương pháp mới). Đề cương của bạn cần phải thể hiện được tính hệ thống, sự khách quan và khả năng tư duy phản biện.

Dưới đây là các tiêu chí chi tiết cho từng phần trong một đề cương luận văn chuẩn:

## 1. Tên đề tài (Thesis Title)
*   **Tiêu chí:** Phải thể hiện rõ bản chất là một nghiên cứu đánh giá, so sánh. Tránh các từ ngữ gây hiểu lầm là đề xuất hệ thống mới.
*   **Từ khóa khuyên dùng:** *Đánh giá thực nghiệm (Empirical Study), Khảo sát và đánh giá (Evaluation), Phân tích so sánh (Comparative Analysis), Benchmarking...*
*   **Ví dụ:** *"Đánh giá thực nghiệm các mô hình học sâu trong việc phát hiện bất thường trên dữ liệu log chuỗi thời gian."*

## 2. Tính cấp thiết của đề tài (Motivation)
Hội đồng sẽ hỏi: *"Tại sao phải mất công đi đánh giá lại những thứ người ta đã làm?"*
*   **Tiêu chí:** Cần chỉ ra được **"Khoảng trống nghiên cứu" (Research Gap)** trong các đánh giá hiện tại:
    *   Các phương pháp hiện có báo cáo kết quả tốt nhưng chưa từng được đánh giá trên một loại dữ liệu mới/môi trường thực tế mới.
    *   Các nghiên cứu trước đây đánh giá thiếu khách quan (sử dụng sai độ đo, chưa bao phủ hết các trường hợp).
    *   Có quá nhiều công cụ mới ra đời nhưng chưa có một hệ thống benchmark chuẩn mực nào để so sánh chúng.

## 3. Câu hỏi nghiên cứu (Research Questions - RQs)
Đây là **linh hồn** của nghiên cứu Cấp độ 1. Không có RQs rõ ràng, luận văn sẽ trở thành một bài báo cáo kỹ thuật.
*   **Tiêu chí:** Phải có từ 2-4 câu hỏi cụ thể, sâu sắc.
*   **Ví dụ chuẩn:**
    *   *RQ1:* Hiệu năng (độ chính xác, thời gian thực thi) của các phương pháp A, B, C thay đổi như thế nào khi đối mặt với dữ liệu nhiễu?
    *   *RQ2:* Đâu là nguyên nhân cốt lõi khiến phương pháp A thất bại trong bối cảnh X?
    *   *RQ3:* Mức tiêu thụ tài nguyên phần cứng (CPU, RAM) của các thuật toán đánh đổi ra sao với độ chính xác?

## 4. Đối tượng và Phạm vi nghiên cứu (Scope)
*   **Tiêu chí:** Giới hạn rõ ràng để nghiên cứu khả thi nhưng vẫn đủ lớn để mang tầm Thạc sĩ.
    *   *Đối tượng:* Xác định rõ họ thuật toán/phương pháp nào sẽ được đưa lên bàn cân (Baselines). Phải giải thích được **tại sao lại chọn những phương pháp này** (ví dụ: vì đây là State-of-the-Art từ 2020-2023).
    *   *Phạm vi dữ liệu:* Liệt kê cụ thể các tập dữ liệu (Datasets) sẽ dùng. Yêu cầu bắt buộc là dữ liệu phải đa dạng (nhiều kích thước, nhiều đặc thù).

## 5. Phương pháp nghiên cứu & Thiết kế thực nghiệm (Methodology & Design)
Phần này quyết định đề cương có được duyệt hay không. Cần trình bày rõ **cách thức thực hiện sự công bằng** trong so sánh.
*   **Tiêu chí thiết lập môi trường:** Cấu hình phần cứng/phần mềm thế nào? Cách chia tập Train/Test/Validation ra sao? (Phải dùng chung 1 bộ sinh hạt giống ngẫu nhiên - random seed).
*   **Tiêu chí lựa chọn độ đo (Metrics):** 
    *   Không chỉ dùng các độ đo cơ bản như F1-score hay Accuracy.
    *   Cần các độ đo về Robustness (tính bền vững), Efficiency (Hiệu quả tài nguyên), Scalability (Khả năng mở rộng khi dữ liệu tăng tỷ lệ thuận).
*   **Quy trình tinh chỉnh tham số (Hyperparameter Tuning):** Cần nêu rõ phương pháp (ví dụ: Grid Search, Random Search) áp dụng đồng đều cho TẤT CẢ các baselines để không thiên vị.

## 6. Dự kiến kết quả đạt được (Expected Contributions)
*   **Tiêu chí:** Nêu bật được giá trị mang lại cho cộng đồng khoa học và thực tiễn.
    *   Một báo cáo phân tích toàn diện chỉ ra ưu/khuyết điểm của các SOTA.
    *   Một bộ Framework/Pipeline mã nguồn mở giúp tự động hóa việc Benchmark cho các nghiên cứu sau này (Đây là một điểm cộng cực lớn cho luận văn Thạc sĩ).
    *   Một tập hợp các "Khuyến nghị thực tiễn" (Practical Guidelines/Lessons learned) dành cho kỹ sư khi triển khai thực tế.

## 7. Lời khuyên để bảo vệ thành công đề cương
1.  **Chuẩn bị sẵn câu trả lời cho tính mới:** Tính mới của bạn không nằm ở thuật toán, mà nằm ở *góc nhìn mới, bộ dữ liệu mới, hoặc hệ thống độ đo toàn diện hơn*.
2.  **Minh chứng tính khả thi:** Hội đồng thường e ngại việc sinh viên không thể cài đặt lại (reproduce) source code của các bài báo cũ. Hãy đảm bảo bạn đã chạy thử thành công ít nhất 1-2 phương pháp trước khi bảo vệ đề cương.