# Tiêu chí xây dựng đề cương luận văn thạc sĩ theo hướng nghiên cứu cấp độ 1

**Phạm vi:** Nghiên cứu thực nghiệm, đánh giá và so sánh các phương pháp đã có (*empirical evaluation / benchmarking*), chưa đặt mục tiêu chính là đề xuất một thuật toán mới.

**Bối cảnh minh họa:** Đề tài *Phát hiện sớm bất thường bằng phân tích dữ liệu log dựa trên trí tuệ nhân tạo* (*Early Log Anomaly Detection using Artificial Intelligence*).

> **Lưu ý về thuật ngữ:** “Cấp độ 1” trong tài liệu này là cách gọi thực hành để mô tả một hướng nghiên cứu lấy đánh giá thực nghiệm và benchmarking làm trọng tâm; đây không phải hệ thống phân cấp chính thức, phổ quát của nghiên cứu khoa học. Quy định về cấu trúc đề cương, số trang, biểu mẫu và tiêu chí chấm điểm của trường/khoa hoặc người hướng dẫn luôn được ưu tiên.

---

## 1. Mục đích của tài liệu

Tài liệu này giúp học viên chuẩn bị một đề cương luận văn thạc sĩ có thể thực hiện được, với câu hỏi nghiên cứu rõ ràng, phương pháp đánh giá hợp lý, dữ liệu phù hợp và kết quả dự kiến có giá trị học thuật.

Một đề cương theo hướng này không chỉ trả lời “sẽ chạy những mô hình nào?” mà còn phải giải thích:

1. **Vấn đề nghiên cứu là gì và vì sao đáng nghiên cứu?**
2. **Các công trình trước đây đã biết những gì, còn điểm nào chưa được làm rõ?**
3. **Những câu hỏi nào sẽ được trả lời bằng thực nghiệm?**
4. **Các phương pháp, dữ liệu, chỉ số và thiết kế thí nghiệm nào phù hợp để trả lời các câu hỏi đó?**
5. **Làm thế nào để kết quả công bằng, đáng tin cậy và có thể tái lập?**
6. **Kết quả có thể đóng góp điều gì dù không đề xuất thuật toán mới?**

## 2. Đặc trưng của nghiên cứu cấp độ 1

### 2.1. Mục tiêu chính

Mục tiêu chính là đánh giá một cách có hệ thống những phương pháp hiện có, làm rõ ưu điểm, hạn chế, phạm vi hiệu quả, chi phí và điều kiện hoạt động của chúng.

Các hoạt động phù hợp gồm:

- Tổng hợp có cấu trúc những phương pháp liên quan trong tài liệu khoa học.
- Tái lập hoặc chạy các phương pháp đại diện trong điều kiện được mô tả rõ.
- So sánh nhiều phương pháp trên bộ dữ liệu và giao thức đánh giá được xác định trước.
- Khảo sát tác động của các yếu tố như đặc tính dữ liệu, lượng thông tin đầu vào, ngưỡng quyết định hoặc chi phí suy luận.
- Phân tích lỗi, độ ổn định và nguy cơ mất khả năng tổng quát hóa.
- Rút ra kết luận có căn cứ về việc phương pháp nào phù hợp trong điều kiện nào.

### 2.2. Những gì không bắt buộc

Một nghiên cứu cấp độ 1 **không nhất thiết** phải:

- Đề xuất một kiến trúc mô hình hoàn toàn mới.
- Tạo một thuật toán mới hoặc công bố một component mới.
- Luôn vượt qua kết quả tốt nhất đã công bố.
- Sử dụng tất cả bộ dữ liệu công khai.
- Thực hiện mọi loại kiểm định thống kê có thể có.

Tuy nhiên, nghiên cứu cần có câu hỏi rõ ràng, thiết kế hợp lý, báo cáo minh bạch, phân tích nghiêm túc và kết luận gắn với bằng chứng. Việc chỉ chạy một vài mô hình, liệt kê điểm số và chọn mô hình đứng đầu thường chưa đủ để tạo ra một đóng góp thực nghiệm thuyết phục.

### 2.3. Phân biệt ba hoạt động

| Hoạt động | Đặc điểm | Mức độ đóng góp thường thấy |
|---|---|---|
| Chạy thử ban đầu | Chạy một vài mô hình để hiểu công cụ hoặc dữ liệu | Phù hợp giai đoạn thăm dò, chưa chắc đủ cho nghiên cứu độc lập |
| Benchmarking có hệ thống | Câu hỏi, giao thức, dữ liệu, chỉ số và điều kiện so sánh được xác định rõ | Có thể tạo ra bằng chứng so sánh đáng tin cậy |
| Nghiên cứu thực nghiệm chuyên sâu | Benchmarking cộng với phân tích lỗi, yếu tố ảnh hưởng, độ ổn định và giới hạn tổng quát hóa | Có khả năng tạo ra hiểu biết thực nghiệm rõ ràng hơn |

Đây là phân biệt thực hành, không phải các bậc học thuật chính thức.

---

## 3. Tiêu chí tổng quát của một đề cương tốt

Đề cương nên đáp ứng các nhóm tiêu chí dưới đây. Mỗi nhóm cần được thể hiện bằng nội dung cụ thể trong đề cương, không chỉ bằng một câu tuyên bố chung.

### 3.1. Vấn đề nghiên cứu và ý nghĩa

**Yêu cầu:**

- Mô tả được bối cảnh và bài toán cụ thể.
- Nêu rõ ai hoặc hệ thống nào có thể hưởng lợi từ hiểu biết thu được.
- Giải thích vì sao cần đánh giá thực nghiệm thay vì chỉ đọc và tổng hợp điểm số trong các bài báo.
- Phân biệt bài toán chung với phạm vi luận văn thực sự xử lý.

**Bằng chứng nên có:**

- Ví dụ thực tế hoặc kịch bản sử dụng có liên quan.
- Dẫn chứng từ các bài báo, khảo sát hoặc tài liệu đáng tin cậy.
- Mô tả hậu quả của vấn đề, chẳng hạn cảnh báo sai, bỏ sót bất thường, phát hiện muộn hoặc chi phí xử lý lớn.

**Không nên viết chung chung:** “Dữ liệu log ngày càng nhiều nên cần AI để phát hiện bất thường.” Hãy nêu rõ khó khăn mà đề tài muốn khảo sát, như hiệu quả thay đổi giữa các loại dữ liệu hay độ chính xác cuối chuỗi chưa phản ánh khả năng phát hiện sớm.

### 3.2. Khoảng trống nghiên cứu hoặc nhu cầu đánh giá

Ở cấp độ 1, khoảng trống không nhất thiết là “chưa có ai đề xuất phương pháp X”. Nó có thể là **chưa có đủ bằng chứng trong một phạm vi hoặc điều kiện cụ thể**.

Ví dụ về khoảng trống có thể khảo sát:

- Các phương pháp được đánh giá trên những giao thức khác nhau nên khó đối chiếu trực tiếp.
- Kết quả cuối cùng được báo cáo nhiều hơn khả năng phát hiện khi chỉ có một phần chuỗi log.
- Chi phí suy luận hoặc độ ổn định chưa được so sánh trong cùng môi trường.
- Chưa rõ kết quả có nhất quán giữa các bộ dữ liệu có đặc tính khác nhau hay không.
- Chưa có phân tích đủ chi tiết về các loại lỗi khiến mô hình bỏ sót hoặc cảnh báo sai.

Đây chỉ là **giả thuyết về khoảng trống**, không nên khẳng định đúng trước khi khảo sát tài liệu. Cần chỉ ra công trình nào đã nghiên cứu vấn đề gì, dùng thiết lập nào và phần nào còn chưa được trả lời.

### 3.3. Mục tiêu và câu hỏi nghiên cứu

Mục tiêu phải phù hợp với phạm vi thực nghiệm, có thể trả lời bằng dữ liệu và hoàn thành trong thời gian luận văn.

Một mục tiêu tổng quát có thể là:

> Đánh giá có hệ thống hiệu quả, khả năng phát hiện sớm, chi phí tính toán và mức độ ổn định của một nhóm phương pháp phát hiện bất thường log đại diện trên các bộ dữ liệu được lựa chọn, trong một giao thức thực nghiệm có thể mô tả và tái lập.

Mỗi câu hỏi nghiên cứu (*Research Question – RQ*) cần đi cùng phương pháp phân tích dự kiến. Không nên đặt câu hỏi mà dữ liệu hoặc thời gian thực hiện không thể trả lời.

### 3.4. Phương pháp nghiên cứu phù hợp

Đề cương cần nêu phương pháp nghiên cứu là đánh giá thực nghiệm/benchmarking, giải thích vì sao phù hợp và mô tả đủ chi tiết để người khác hiểu sẽ thực hiện những gì.

Cần làm rõ:

- Đối tượng được so sánh.
- Cách lựa chọn phương pháp và bộ dữ liệu.
- Cách tiền xử lý và xây dựng mẫu.
- Cách chia dữ liệu và hiệu chỉnh mô hình.
- Chỉ số đánh giá, phương pháp phân tích và cách xử lý tính ngẫu nhiên.
- Cách kiểm soát sai lệch, rò rỉ dữ liệu và các giới hạn khác.

### 3.5. Tính khả thi

Đề cương phải chứng minh rằng phạm vi công việc phù hợp với thời gian, kỹ năng, phần cứng, khả năng truy cập dữ liệu và năng lực triển khai của học viên.

Cần kiểm tra sớm:

- Mã nguồn có thể cài đặt và chạy được không?
- Dữ liệu có thể tải, xử lý và sử dụng theo điều khoản cho phép không?
- Có đủ nhãn và thông tin thời gian để đo khả năng phát hiện sớm không?
- Chi phí huấn luyện và suy luận có nằm trong giới hạn tài nguyên không?
- Nếu một baseline không thể tái lập, sẽ thay thế hoặc giới hạn kết luận như thế nào?

---

## 4. Cấu trúc đề cương luận văn được khuyến nghị

Cấu trúc dưới đây là khung tham khảo. Có thể điều chỉnh theo mẫu của trường hoặc yêu cầu của người hướng dẫn.

### Phần 1. Tên đề tài

Tên đề tài cần thể hiện đúng bài toán, phạm vi và loại đóng góp dự kiến; tránh khẳng định một kết quả chưa được chứng minh.

Ví dụ:

> **Đánh giá thực nghiệm các phương pháp phát hiện sớm bất thường dựa trên dữ liệu log hệ thống**
>
> *An Empirical Evaluation of Early Log-Based Anomaly Detection Methods*

Nếu giữ tên đề tài rộng hơn, phần mục tiêu và phạm vi phải giải thích rõ nghiên cứu sẽ tập trung vào nhóm phương pháp, bộ dữ liệu và tiêu chí nào.

### Phần 2. Đặt vấn đề / Giới thiệu

Nên có các nội dung:

1. Bối cảnh của hệ thống log và nhu cầu phát hiện bất thường.
2. Định nghĩa bài toán trong phạm vi luận văn.
3. Những khó khăn hiện có và hệ quả của chúng.
4. Lý do cần nghiên cứu bằng thực nghiệm có kiểm soát.
5. Mục tiêu tổng quát và mục tiêu cụ thể.
6. Các câu hỏi nghiên cứu.
7. Phạm vi, giả định và những nội dung nằm ngoài phạm vi.
8. Đóng góp dự kiến.
9. Cấu trúc dự kiến của luận văn.

### Phần 3. Cơ sở lý thuyết và tổng quan nghiên cứu

Cần tổng hợp, so sánh và phân tích tài liệu, không chỉ liệt kê từng bài báo.

Nội dung nên có:

- Khái niệm log hệ thống, mẫu log, chuỗi sự kiện và bất thường.
- Các loại bài toán: phân loại bất thường, phát hiện theo chuỗi, phát hiện không giám sát hoặc bán giám sát, phát hiện trực tuyến và phát hiện sớm.
- Các nhóm phương pháp phù hợp với câu hỏi nghiên cứu.
- Các bộ dữ liệu phổ biến, cách gán nhãn và các vấn đề của dữ liệu.
- Các chỉ số đánh giá và sự khác nhau trong cách tính.
- Bảng tổng hợp bài báo theo: phương pháp, dữ liệu, loại nhãn, chỉ số, giao thức, ưu điểm, hạn chế và mức độ phù hợp với luận văn.
- Khoảng trống hoặc câu hỏi còn chưa được giải đáp.

**Tiêu chí chất lượng:** Mỗi nhận định về ưu điểm, giới hạn hoặc hiệu quả của một phương pháp phải có nguồn dẫn hoặc được nêu rõ là giả thuyết sẽ kiểm tra bằng thực nghiệm.

Nếu thực hiện một tổng quan tài liệu có hệ thống, cần mô tả cơ sở dữ liệu tìm kiếm, từ khóa, thời gian tìm kiếm, tiêu chí đưa vào/loại ra, quy trình sàng lọc và cách trích xuất thông tin. PRISMA 2020 là hướng dẫn báo cáo cho systematic review; không phải mọi đề cương benchmarking đều bắt buộc áp dụng toàn bộ PRISMA.

### Phần 4. Câu hỏi nghiên cứu và phạm vi

Với mỗi RQ, đề cương nên nêu:

- Câu hỏi chính xác.
- Lý do cần trả lời.
- Dữ liệu cần dùng.
- Phương pháp hoặc phép phân tích.
- Chỉ số đầu ra.
- Dạng kết quả cần trình bày.
- Những giới hạn có thể ảnh hưởng đến kết luận.

Ví dụ chi tiết được trình bày tại Mục 5.

### Phần 5. Thiết kế nghiên cứu và phương pháp thực nghiệm

Đây là phần cốt lõi của đề cương cấp độ 1. Không nên chỉ ghi “sử dụng Python để chạy các thuật toán và so sánh F1-score”. Cần mô tả tối thiểu các nội dung sau:

1. **Đối tượng thực nghiệm:** tên và phiên bản phương pháp, lý do lựa chọn, loại học, yêu cầu nhãn, trạng thái mã nguồn.
2. **Bộ dữ liệu:** nguồn, phiên bản, giấy phép/điều kiện sử dụng, quy mô, trường dữ liệu, cấu trúc nhãn và lý do phù hợp.
3. **Tiền xử lý:** chuẩn hóa, parsing, gom nhóm hoặc cửa sổ chuỗi, loại bản ghi, xử lý dữ liệu thiếu và các bước khác.
4. **Chia dữ liệu:** train/validation/test hoặc chia theo thời gian; cách bảo đảm không rò rỉ mẫu.
5. **Huấn luyện và hiệu chỉnh:** siêu tham số, ngưỡng quyết định, tiêu chí dừng và cách chọn cấu hình.
6. **Chỉ số đánh giá:** định nghĩa, đơn vị tính, cấp độ mẫu và lý do lựa chọn.
7. **Thiết kế so sánh:** điều kiện giống nhau, khác biệt bắt buộc giữa mô hình và cách báo cáo các khác biệt đó.
8. **Tính ngẫu nhiên và lặp lại:** seed, số lần chạy dự kiến, cách tổng hợp và báo cáo độ biến thiên.
9. **Phân tích lỗi:** cách lấy mẫu, phân nhóm và diễn giải false positive/false negative.
10. **Môi trường thực nghiệm:** phần cứng, hệ điều hành, ngôn ngữ, thư viện và phiên bản quan trọng.
11. **Quản lý kết quả:** lưu cấu hình, đầu ra thô, log thực nghiệm và script phân tích.

### Phần 6. Kết quả dự kiến và đóng góp

Đề cương không nên hứa rằng một mô hình chắc chắn sẽ tốt nhất hoặc rằng nghiên cứu chắc chắn tìm ra một nguyên nhân nào đó trước khi có kết quả.

Nên mô tả **loại đầu ra dự kiến**, chẳng hạn:

- Bảng benchmark có điều kiện so sánh rõ ràng.
- Phân tích sự khác nhau về hiệu quả giữa các bộ dữ liệu.
- Đường cong hiệu quả theo phần trăm tiền tố chuỗi log.
- Phân tích độ trễ, thông lượng và tài nguyên.
- Phân loại các kiểu lỗi thường gặp.
- Khuyến nghị lựa chọn phương pháp theo điều kiện sử dụng.
- Danh sách hạn chế và các vấn đề có thể nghiên cứu tiếp.

Đóng góp của nghiên cứu có thể là bằng chứng thực nghiệm và hiểu biết mới, không cần tuyên bố thuật toán mới. Tuy nhiên, đề cương vẫn phải giải thích kết quả dự kiến khác hoặc bổ sung gì so với các đánh giá đã có.

### Phần 7. Kế hoạch thực hiện

Mỗi giai đoạn cần có công việc, đầu ra và tiêu chí hoàn thành; không chỉ ghi tên tháng.

Một kế hoạch tham khảo cho luận văn khoảng 6 tháng:

| Giai đoạn | Công việc | Đầu ra / điều kiện hoàn thành |
|---|---|---|
| Tháng 1 | Xác định phạm vi, tổng quan tài liệu, xây dựng RQ | Bảng tổng hợp nghiên cứu, câu hỏi và phạm vi được thống nhất |
| Tháng 2 | Chọn baseline, dữ liệu và giao thức | Danh sách phương pháp/dataset, quy trình thí nghiệm được ghi lại |
| Tháng 3 | Chuẩn bị môi trường, tái lập pipeline cơ bản | Pipeline chạy được và kiểm tra chất lượng dữ liệu hoàn tất |
| Tháng 4 | Chạy benchmark chính | Kết quả thô, cấu hình, log và bảng kết quả ban đầu |
| Tháng 5 | Phân tích sâu, kiểm tra độ ổn định, hoàn thiện thí nghiệm | Phân tích RQ, kiểm tra độ tin cậy và giới hạn |
| Tháng 6 | Viết, rà soát, hoàn thiện mã và tài liệu tái lập | Bản luận văn, phụ lục thực nghiệm và gói tài liệu cần thiết |

Cần điều chỉnh lịch theo quy định thực tế, độ phức tạp mô hình và thời gian phản hồi của người hướng dẫn. Nên có khoảng dự phòng cho lỗi cài đặt, dữ liệu khó xử lý và thực nghiệm phải chạy lại.

### Phần 8. Tài liệu tham khảo và phụ lục dự kiến

- Tài liệu tham khảo dùng một chuẩn trích dẫn nhất quán theo yêu cầu của trường.
- Phụ lục có thể chứa truy vấn tìm kiếm, tiêu chí chọn bài báo, bảng dữ liệu, cấu hình, siêu tham số, định nghĩa chỉ số và checklist thực nghiệm.
- Nếu có thể chia sẻ, nên dự kiến công bố mã nguồn, script xử lý, cấu hình và kết quả ở dạng có thể tái sử dụng; nếu không thể chia sẻ dữ liệu, cần nêu rõ lý do và cung cấp mô tả/biện pháp thay thế phù hợp.

---

## 5. Bộ câu hỏi nghiên cứu tham khảo cho đề tài phát hiện sớm bất thường log

Không cần sử dụng tất cả RQ dưới đây. Chọn khoảng 3–4 câu hỏi có thể trả lời sâu và phù hợp với tài nguyên của luận văn.

### RQ1 — Hiệu quả phát hiện tổng thể

**Câu hỏi:** Các phương pháp đại diện đạt hiệu quả phát hiện bất thường như thế nào trên các bộ dữ liệu log được lựa chọn khi được đánh giá theo một giao thức thực nghiệm được mô tả rõ?

- **Dữ liệu:** 2–3 bộ dữ liệu có cấu trúc/nhãn phù hợp.
- **Đối tượng:** 3–5 baseline đại diện, nếu có thể chạy và so sánh hợp lý.
- **Chỉ số:** Precision, Recall, F1-score; PR-AUC nếu mô hình tạo ra điểm số/độ tin cậy phù hợp; False Positive Rate khi cách tính có ý nghĩa.
- **Phân tích:** bảng theo dataset và model; độ biến thiên; giải thích khác biệt về thiết lập.
- **Giới hạn:** không so sánh trực tiếp những số liệu được tính theo định nghĩa hoặc giao thức không tương thích mà không giải thích.

### RQ2 — Độ ổn định giữa các bộ dữ liệu

**Câu hỏi:** Thứ hạng và hiệu quả của các phương pháp có thay đổi giữa các bộ dữ liệu hoặc điều kiện kiểm thử khác nhau không?

- **Dữ liệu:** các bộ dữ liệu có bối cảnh hoặc cấu trúc khác nhau.
- **Phân tích:** mức thay đổi chỉ số, sự nhất quán về thứ hạng, kiểu lỗi và đặc tính dữ liệu.
- **Bằng chứng:** mô tả dữ liệu và phân tích trường hợp; không suy luận nguyên nhân chỉ từ chênh lệch điểm số.
- **Kết luận phù hợp:** nêu rõ những điều kiện mà kết quả quan sát được hỗ trợ, không khẳng định tổng quát cho mọi hệ thống.

### RQ3 — Khả năng phát hiện sớm

**Câu hỏi:** Hiệu quả của các phương pháp thay đổi thế nào khi chỉ có thể quan sát một phần chuỗi log?

- **Thiết kế:** xác định trước các tỷ lệ tiền tố, ví dụ 10%, 25%, 50%, 75% và 100%, nếu phù hợp với cách tổ chức dữ liệu.
- **Điều kiện bắt buộc:** nhãn và cách chia chuỗi phải cho phép xác định dự đoán tại từng tiền tố. Cần tránh sử dụng thông tin xuất hiện sau thời điểm được giả định là đã phát hiện.
- **Chỉ số:** Precision/Recall/F1 tại từng tiền tố; tỷ lệ trường hợp phát hiện được trước mốc quy định; thời điểm hoặc độ trễ phát hiện khi dữ liệu có mốc thời gian đáng tin cậy.
- **Phân tích:** đồ thị chỉ số theo tỷ lệ tiền tố; mức đánh đổi giữa phát hiện sớm và cảnh báo sai.
- **Giới hạn:** nếu nhãn chỉ có ở cấp độ phiên/block mà không cho biết thời điểm bắt đầu bất thường, không nên tuyên bố đã đo chính xác độ trễ ở cấp sự kiện.

### RQ4 — Chi phí tính toán

**Câu hỏi:** Các phương pháp đánh đổi hiệu quả phát hiện với chi phí tính toán như thế nào?

- **Chỉ số:** thời gian huấn luyện, độ trễ suy luận, thông lượng và bộ nhớ; báo cáo phần cứng, batching và điều kiện đo.
- **Phân tích:** so sánh trong môi trường giống nhau hoặc giải thích rõ khác biệt phần cứng; phân biệt thời gian xử lý từng mẫu với thông lượng khi xử lý theo lô.
- **Giới hạn:** số đo trên một máy hoặc một bộ dữ liệu không tự động đại diện cho mọi môi trường triển khai.

### RQ5 — Phân tích lỗi

**Câu hỏi:** Những kiểu trường hợp nào thường bị bỏ sót hoặc tạo cảnh báo sai, và các lỗi quan sát được có liên quan đến đặc tính dữ liệu nào?

- **Dữ liệu:** các mẫu false positive và false negative của từng baseline.
- **Phân tích:** chọn các nhóm lỗi có tiêu chí rõ; xem xét mẫu log mới, chuỗi ngắn/dài, dữ liệu nhiễu hoặc mất cân bằng nếu những hiện tượng đó thực sự có trong dataset.
- **Bằng chứng:** ví dụ cụ thể, thống kê theo nhóm và quy tắc phân loại lỗi được mô tả.
- **Giới hạn:** không suy luận nhân quả chỉ từ việc hai hiện tượng cùng xuất hiện.

### Bảng liên kết RQ với thiết kế đánh giá

| RQ | Biến/hiện tượng cần quan sát | Phương pháp phân tích | Đầu ra dự kiến |
|---|---|---|---|
| RQ1 | Chỉ số phát hiện của từng baseline | So sánh định lượng theo dataset | Bảng chỉ số và kết quả tổng hợp |
| RQ2 | Mức thay đổi hiệu quả giữa dataset/điều kiện | So sánh theo điều kiện, phân tích độ biến thiên | Bảng/biểu đồ và phân tích khác biệt |
| RQ3 | Hiệu quả theo lượng tiền tố đã quan sát | Đánh giá tại các điểm tiền tố được định trước | Đường cong phát hiện sớm |
| RQ4 | Độ trễ, thời gian, thông lượng, bộ nhớ | Đo lặp trong điều kiện phần cứng được mô tả | Bảng hiệu năng và đánh đổi |
| RQ5 | Nhóm false positive/false negative | Phân tích lỗi định tính và định lượng | Taxonomy lỗi, ví dụ và nhận định có bằng chứng |

---

## 6. Tiêu chí chọn baseline

Không chọn baseline chỉ vì nổi tiếng, mới nhất hoặc có chỉ số cao nhất trong bài báo gốc. Mỗi phương pháp được chọn cần có lý do gắn với RQ.

### 6.1. Tiêu chí bắt buộc cần xem xét

- **Mức độ liên quan:** trực tiếp giải quyết bài toán hoặc làm đại diện cho một nhóm phương pháp cần khảo sát.
- **Khả năng tái lập:** có mã nguồn, mô tả đủ chi tiết hoặc đủ cơ sở để triển khai lại.
- **Tính tương thích dữ liệu:** định dạng log, cấu trúc chuỗi và dạng nhãn có phù hợp không.
- **Tính so sánh được:** có thể định nghĩa đầu vào/đầu ra và đơn vị đánh giá tương thích không.
- **Tính đại diện:** nhóm baseline có thể hiện những cơ chế khác nhau cần khảo sát không.
- **Tính khả thi:** chi phí cài đặt và huấn luyện phù hợp với tài nguyên hay không.
- **Tính công bằng:** không dùng thông tin gán nhãn hoặc dữ liệu mà phương pháp khác không được phép dùng theo thiết lập so sánh đã xác định.

### 6.2. Những thông tin nên ghi cho mỗi baseline

| Trường | Nội dung cần điền |
|---|---|
| Tên và trích dẫn | Tên phương pháp, bài báo gốc, năm công bố |
| Nhóm phương pháp | Thống kê, học máy, học chuỗi, Transformer, v.v. |
| Loại học | Supervised, semi-supervised, unsupervised hoặc cách phân loại phù hợp |
| Đầu vào | Dòng log, template, chuỗi sự kiện, đặc trưng hoặc biểu diễn khác |
| Đầu ra | Nhãn bất thường, điểm số, dự đoán theo chuỗi hoặc kiểu đầu ra khác |
| Dữ liệu cần cho huấn luyện | Nhãn nào được dùng, lượng dữ liệu và giả định |
| Mã nguồn/cấu hình | URL, phiên bản, commit hoặc mô tả triển khai |
| Tiền xử lý | Parser, nhóm chuỗi, cửa sổ, chuẩn hóa |
| Điểm mạnh/hạn chế đã báo cáo | Trích dẫn nguồn, không chỉ là nhận xét chủ quan |
| Lý do đưa vào benchmark | RQ nào cần baseline này và nó đại diện điều gì |
| Rủi ro tái lập | Thiếu mã nguồn, thiếu cấu hình, phụ thuộc môi trường |

Các mô hình như DeepLog, LogAnomaly, LogRobust hoặc LogBERT có thể được khảo sát ban đầu, nhưng danh sách cuối cùng phải được xác nhận qua tổng quan tài liệu và điều kiện triển khai thực tế. Không bắt buộc đưa tất cả vào benchmark.

---

## 7. Tiêu chí lựa chọn bộ dữ liệu

### 7.1. Các tiêu chí chính

1. **Mức độ phù hợp với RQ:** dữ liệu có cho phép đo hiệu quả hoặc phát hiện sớm đúng như dự kiến không?
2. **Nguồn và khả năng truy cập:** nguồn gốc rõ ràng, phiên bản xác định, điều khoản sử dụng phù hợp.
3. **Cấp độ nhãn:** nhãn ở cấp dòng log, chuỗi, phiên xử lý, block hoặc sự cố; cách tính metric phải phù hợp.
4. **Thông tin thời gian:** có timestamp và thứ tự sự kiện đủ tin cậy nếu cần đo độ trễ không?
5. **Độ đa dạng:** các dataset bổ sung bằng chứng về những bối cảnh khác nhau thay vì chỉ lặp lại dữ liệu rất giống nhau.
6. **Chất lượng dữ liệu:** dữ liệu thiếu, bản ghi trùng lặp, mẫu lặp lại giữa các tập và vấn đề parsing.
7. **Khả năng xử lý:** kích thước dữ liệu và chi phí tiền xử lý phù hợp với thời gian/tài nguyên.
8. **Khả năng so sánh:** xác định được quy tắc tạo mẫu, phân chia và đánh giá nhất quán.

### 7.2. Những bộ dữ liệu có thể khảo sát

HDFS, BGL, Thunderbird, OpenStack và các tập log hệ thống/ứng dụng khác có thể là ứng viên. Cần kiểm tra tài liệu gốc, nguồn tải, phiên bản và quy tắc gán nhãn của từng tập trước khi quyết định. Không nên mặc định rằng tất cả dữ liệu đều có nhãn ở cùng cấp độ hoặc đều phù hợp để đánh giá early detection.

### 7.3. Những điểm cần ghi trong đề cương

- Tên, nguồn, phiên bản và ngày truy cập/tải dữ liệu.
- Tổng số bản ghi/mẫu và số lượng bình thường/bất thường, theo cấp độ nhãn thích hợp.
- Đơn vị mẫu dùng để huấn luyện và đánh giá.
- Cách xử lý duplicate, dữ liệu thiếu và mẫu không hợp lệ.
- Cách chia train/validation/test hoặc chia theo thời gian.
- Các hạn chế có thể ảnh hưởng tính đại diện và khả năng khái quát hóa.

---

## 8. Tiêu chí đánh giá và chỉ số

Mỗi chỉ số phải được định nghĩa, chỉ rõ đơn vị tính và liên kết với một RQ. Không nên đưa nhiều chỉ số chỉ để bảng kết quả trông đầy đủ.

### 8.1. Chỉ số phân loại cơ bản

| Chỉ số | Ý nghĩa | Lưu ý báo cáo |
|---|---|---|
| Precision | Trong các mẫu được dự đoán bất thường, tỷ lệ dự đoán đúng | Đơn vị mẫu và cách xử lý các trường hợp không có dự đoán dương phải được nêu |
| Recall | Trong các mẫu bất thường thật, tỷ lệ được phát hiện | Đặc biệt quan trọng khi bỏ sót bất thường có chi phí cao |
| F1-score | Trung bình điều hòa giữa Precision và Recall | Cần nêu tính ở cấp mẫu, phiên, sự kiện hay cách khác |
| False Positive Rate | Tỷ lệ mẫu bình thường bị dự đoán bất thường | Định nghĩa mẫu dương/âm và đơn vị tính phải rõ |
| PR-AUC | Diện tích dưới đường Precision–Recall | Chỉ dùng khi đầu ra điểm số/ngưỡng của mô hình và cách tính phù hợp |
| Accuracy | Tỷ lệ dự đoán đúng tổng thể | Không nên dùng đơn độc khi dữ liệu mất cân bằng |

### 8.2. Đánh giá early detection

Đề cương phải định nghĩa “sớm” bằng một quy tắc có thể kiểm tra. Có thể cân nhắc:

- **Hiệu quả theo tỷ lệ tiền tố:** dự đoán khi chỉ quan sát một phần của chuỗi log, với các tỷ lệ được ấn định trước.
- **Vị trí phát hiện đầu tiên:** số sự kiện hoặc phần trăm tiền tố tại thời điểm mô hình lần đầu đưa ra cảnh báo đúng.
- **Độ trễ phát hiện:** thời gian từ một mốc bắt đầu được định nghĩa rõ đến lúc phát hiện.
- **Tỷ lệ phát hiện trước hạn:** tỷ lệ sự cố được cảnh báo trước một mốc đã xác định, nếu có căn cứ cho mốc đó.
- **Đánh đổi với cảnh báo sai:** độ sớm không được đánh giá tách rời khỏi false positive hoặc độ tin cậy cảnh báo.

Không phải dataset nào cũng hỗ trợ mọi phép đo. Nếu nhãn chỉ tồn tại ở cấp độ toàn bộ phiên/block, cần thận trọng khi tuyên bố đo độ trễ ở cấp từng sự kiện. Đề cương phải nêu rõ những metric nào có thể tính chính xác với nhãn hiện có và metric nào không khả thi.

### 8.3. Hiệu năng hệ thống

Nếu RQ liên quan triển khai thực tế, có thể báo cáo:

- Thời gian huấn luyện.
- Độ trễ suy luận (nêu đơn vị và cách tính).
- Thông lượng xử lý, chẳng hạn số mẫu hoặc sự kiện mỗi giây.
- Mức sử dụng bộ nhớ.
- Phần cứng, batching, kích thước đầu vào và cách đo.

Cần phân biệt hiệu năng xử lý từng mẫu với thông lượng khi xử lý theo lô. So sánh thời gian trên các máy khác nhau chỉ nên diễn giải có điều kiện.

---

## 9. Yêu cầu về tính công bằng, độ tin cậy và tái lập

### 9.1. Tránh rò rỉ dữ liệu

Đề cương cần nêu biện pháp ngăn thông tin từ test đi vào quá trình huấn luyện hoặc chọn mô hình. Ví dụ:

- Chỉ dùng train để học tham số mô hình.
- Dùng validation để chọn siêu tham số/ngưỡng khi thiết kế yêu cầu.
- Không tiếp tục điều chỉnh dựa trên kết quả test.
- Kiểm tra mẫu trùng lặp hoặc chuỗi chồng lấn qua các tập.
- Cân nhắc chia theo thời gian khi mô phỏng dự đoán tương lai hoặc xử lý log trực tuyến.
- Không dùng thông tin xuất hiện sau thời điểm dự đoán trong thí nghiệm early detection.

Không phải lúc nào chia ngẫu nhiên cũng sai; cách chia phải phù hợp với đơn vị dữ liệu, giả định triển khai và câu hỏi nghiên cứu. Điều quan trọng là nêu rõ lựa chọn và rủi ro còn lại.

### 9.2. Cách so sánh công bằng

- Ghi rõ những điều kiện giữ giống nhau giữa các phương pháp.
- Tôn trọng yêu cầu đầu vào và quy trình của từng phương pháp, không ép cùng tiền xử lý nếu việc đó làm thay đổi bản chất mô hình.
- Nêu rõ khác biệt trong nhãn huấn luyện, ngưỡng, parser và cấu hình.
- Định nghĩa trước cách lựa chọn siêu tham số và ngưỡng.
- Không dùng thông tin gán nhãn mà một baseline không được phép sử dụng theo thiết lập đã xác định.
- Báo cáo các lần chạy thất bại hoặc phương pháp không thể tái lập, thay vì âm thầm loại bỏ.

### 9.3. Sự ngẫu nhiên và độ ổn định

Nếu phương pháp có thành phần ngẫu nhiên, nên thực hiện nhiều lần chạy khi tài nguyên cho phép. Đề cương cần dự kiến số lần chạy và cách báo cáo kết quả. Nếu chỉ có thể chạy ít lần do giới hạn tài nguyên, hãy nêu lý do và giới hạn diễn giải.

Có thể báo cáo trung bình và độ lệch chuẩn, trung vị và khoảng tứ phân vị, hoặc khoảng tin cậy nếu phù hợp với thiết kế. Không cần dùng kiểm định thống kê phức tạp một cách máy móc; phải chọn phép phân tích phù hợp với dữ liệu, số lần chạy và câu hỏi nghiên cứu.

### 9.4. Khả năng tái lập

Tối thiểu cần dự kiến lưu giữ:

- Mã nguồn và cấu hình.
- Phiên bản thư viện, môi trường thực thi và phần cứng chính.
- Seed và lệnh chạy.
- Script tiền xử lý và chia tập.
- Kết quả thô cùng log chạy.
- Script tính metric và tạo bảng/biểu đồ.
- Tài liệu mô tả các bước cần thiết để tái lập.

Nếu không thể chia sẻ dữ liệu hoặc mã nguồn vì giấy phép, bảo mật hoặc lý do khác, cần nêu rõ và cân nhắc cung cấp script, metadata hoặc bộ ví dụ được phép chia sẻ.

---

## 10. Đe dọa đến tính hợp lệ và giới hạn nghiên cứu

Đề cương nên chỉ ra các rủi ro có thể ảnh hưởng đến kết luận và cách giảm thiểu. Không cần tuyên bố sẽ loại bỏ hoàn toàn tất cả rủi ro.

| Loại rủi ro | Ví dụ trong benchmark log | Cách giảm thiểu/báo cáo |
|---|---|---|
| Tính hợp lệ của phép đo (*construct validity*) | F1-score cuối chuỗi không phản ánh đầy đủ việc phát hiện sớm | Dùng metric phù hợp với RQ; định nghĩa đơn vị đánh giá và “sớm” |
| Tính hợp lệ nội tại (*internal validity*) | Rò rỉ dữ liệu, ngưỡng được chọn bằng test, cấu hình khác nhau | Tách train/validation/test; ghi lại quy trình hiệu chỉnh; kiểm soát cấu hình |
| Tính hợp lệ ngoại tại (*external validity*) | Chỉ đánh giá một dataset hoặc một hệ thống | Dùng nhiều bối cảnh nếu khả thi; giới hạn kết luận đúng theo dữ liệu đã kiểm tra |
| Tính hợp lệ của kết luận (*conclusion validity*) | Chênh lệch nhỏ hoặc không ổn định bị diễn giải quá mức | Chạy lặp khi cần; báo cáo độ biến thiên; tránh khẳng định vượt quá bằng chứng |
| Khả năng tái lập | Thiếu mã nguồn, phiên bản hoặc cấu hình | Lưu cấu hình, lệnh chạy, phiên bản và dữ liệu đầu ra |
| Sai lệch lựa chọn | Chỉ chọn baseline thuận lợi hoặc dataset dễ | Nêu tiêu chí chọn trước; giải thích các trường hợp loại trừ |
| Sai lệch báo cáo | Chỉ báo cáo lần chạy/kết quả tốt | Lưu kết quả thô; báo cáo thất bại và giới hạn |

### 10.1. Quy tắc kết luận

- Phân biệt kết quả quan sát được, diễn giải và suy đoán.
- Không khẳng định quan hệ nhân quả nếu thiết kế chỉ cho thấy mối liên hệ.
- Không tuyên bố “tốt nhất” ngoài phạm vi dataset, giao thức và metric đã đánh giá.
- Nêu rõ những phương pháp hoặc điều kiện chưa đánh giá.
- Báo cáo kết quả âm hoặc không có khác biệt nếu đó là kết quả thực nghiệm trung thực.

---

## 11. Đóng góp dự kiến ở cấp độ 1

Một đề cương nên nêu rõ đóng góp dự kiến, dù đóng góp đó không phải thuật toán mới. Có thể bao gồm:

1. **Bằng chứng so sánh:** kết quả benchmark được thực hiện theo một giao thức minh bạch.
2. **Hiểu biết về điều kiện hoạt động:** xác định điều kiện mà một nhóm phương pháp có hiệu quả hoặc suy giảm.
3. **Đánh giá phát hiện sớm:** làm rõ sự khác nhau giữa hiệu quả trên toàn bộ chuỗi và hiệu quả khi chỉ có tiền tố.
4. **Phân tích lỗi có cấu trúc:** mô tả các nhóm lỗi và các tình huống quan trọng.
5. **Bằng chứng về chi phí và đánh đổi:** so sánh hiệu quả phát hiện với độ trễ và tài nguyên.
6. **Tài liệu hoặc gói tái lập:** mã nguồn, cấu hình, script và kết quả nếu điều kiện cho phép.
7. **Khuyến nghị sử dụng có điều kiện:** giúp người khác lựa chọn phương pháp theo yêu cầu dữ liệu và vận hành.

Để chứng minh tính cần thiết, đề cương cần so sánh dự kiến đóng góp của mình với các nghiên cứu gần nhất. Nếu đã có một benchmark tương tự, hãy xác định điểm khác biệt cụ thể (chẳng hạn RQ về early detection, dataset mới, giao thức khác hoặc phân tích lỗi sâu hơn), thay vì chỉ nói “chưa có nghiên cứu nào”.

---

## 12. Ma trận đánh giá chất lượng đề cương

Có thể dùng ma trận này để tự đánh giá hoặc thảo luận với người hướng dẫn. Đây là công cụ tham khảo, **không phải rubric chính thức của mọi trường**.

| Tiêu chí | Chưa đạt | Đạt tối thiểu | Tốt |
|---|---|---|---|
| Vấn đề nghiên cứu | Bối cảnh chung chung, chưa có vấn đề cụ thể | Bài toán và ý nghĩa được mô tả | Vấn đề cụ thể, có bằng chứng và phạm vi rõ |
| Tổng quan tài liệu | Liệt kê bài báo rời rạc | Phân nhóm phương pháp và tổng hợp hạn chế | So sánh có cấu trúc, xác định khoảng trống gắn với bằng chứng |
| RQs và mục tiêu | Quá rộng hoặc không thể kiểm chứng | Có câu hỏi trả lời được bằng thực nghiệm | Mỗi RQ gắn rõ với dữ liệu, phép phân tích và đầu ra |
| Chọn baseline | Chọn theo độ nổi tiếng hoặc điểm số trên bài báo | Có lý do và tiêu chí chọn | Đại diện cho các nhóm phù hợp, có cân nhắc tính so sánh và khả năng tái lập |
| Chọn dữ liệu | Không mô tả nhãn hoặc nguồn | Nguồn và lý do chọn được nêu | Đánh giá được cấu trúc nhãn, tính đại diện, dữ liệu trùng lặp và khả năng đo early detection |
| Thiết kế thực nghiệm | Chỉ nói sẽ chạy mô hình | Có chia tập, chỉ số và quy trình chính | Có kiểm soát rò rỉ, quy trình hiệu chỉnh, môi trường và xử lý tính ngẫu nhiên |
| Metric | Chỉ dùng một chỉ số không giải thích | Metric phù hợp với RQ | Định nghĩa đơn vị đo, đánh đổi và giới hạn diễn giải rõ |
| Phân tích | Chỉ dự kiến xếp hạng điểm số | Có so sánh theo dataset | Có phân tích độ ổn định, lỗi, chi phí và điều kiện ảnh hưởng |
| Độ tin cậy/tái lập | Không dự kiến lưu cấu hình hoặc kết quả thô | Có lưu mã và cấu hình cơ bản | Có kế hoạch lưu pipeline, seed, log, script đánh giá và giới hạn chia sẻ |
| Tính khả thi | Phạm vi vượt tài nguyên/thời gian | Có kế hoạch và tài nguyên cơ bản | Có kiểm tra rủi ro, mốc đầu ra và phương án dự phòng |
| Đóng góp | Chỉ nói “so sánh các thuật toán” | Nêu đầu ra đánh giá và hiểu biết dự kiến | Chỉ rõ đóng góp mới so với benchmark/công trình gần nhất |
| Giới hạn | Không nêu rủi ro | Nêu các giới hạn chính | Gắn từng rủi ro với biện pháp giảm thiểu và giới hạn kết luận |

Một đề cương có thể đạt hình thức đầy đủ nhưng vẫn yếu về khoa học nếu RQ không rõ hoặc không tạo ra hiểu biết nào vượt quá việc tổng hợp điểm số. Ngược lại, kết quả dự kiến không nhất thiết phải là “mô hình A thắng”; một benchmark có thiết kế tốt vẫn có giá trị khi cho thấy không có mô hình nào tốt nhất trong mọi điều kiện.

---

## 13. Checklist trước khi nộp đề cương

Đánh dấu từng mục sau khi đã có nội dung cụ thể trong bản đề cương.

### A. Vấn đề và mục tiêu

- [ ] Tên đề tài thể hiện đúng bài toán và không phóng đại đóng góp.
- [ ] Bối cảnh, vấn đề và ý nghĩa được nêu bằng lập luận có nguồn.
- [ ] Phạm vi nghiên cứu và các nội dung không thực hiện được nêu rõ.
- [ ] Mục tiêu tổng quát và mục tiêu cụ thể có thể kiểm chứng.
- [ ] Có khoảng 3–4 RQ rõ ràng, phù hợp nguồn lực.
- [ ] Mỗi RQ được liên kết với dữ liệu, phép phân tích và đầu ra.

### B. Tổng quan tài liệu

- [ ] Có chiến lược tìm kiếm tài liệu phù hợp.
- [ ] Có tiêu chí đưa vào/loại ra nếu tiến hành sàng lọc có hệ thống.
- [ ] Tài liệu được phân nhóm và tổng hợp, không chỉ liệt kê.
- [ ] Có bảng so sánh phương pháp, dữ liệu, metric và hạn chế.
- [ ] Khoảng trống được hỗ trợ bằng tài liệu hoặc được xác định là câu hỏi cần kiểm tra.
- [ ] Đóng góp dự kiến được đối chiếu với các nghiên cứu gần nhất.

### C. Baseline và dữ liệu

- [ ] Mỗi baseline có lý do được lựa chọn.
- [ ] Biết loại học, đầu vào, đầu ra và yêu cầu nhãn của từng baseline.
- [ ] Kiểm tra nguồn, phiên bản và điều khoản sử dụng dataset.
- [ ] Hiểu rõ cấp độ nhãn và đơn vị đánh giá.
- [ ] Xác định được dữ liệu có cho phép đo early detection hay không.
- [ ] Có kế hoạch xử lý duplicate, missing data và mẫu không hợp lệ.
- [ ] Có phương án thay thế nếu một baseline không chạy được.

### D. Thiết kế thực nghiệm

- [ ] Quy trình tiền xử lý được mô tả.
- [ ] Cách chia train/validation/test hoặc chia theo thời gian được nêu và giải thích.
- [ ] Có biện pháp hạn chế rò rỉ dữ liệu.
- [ ] Cách chọn siêu tham số/ngưỡng được định trước.
- [ ] Metric được định nghĩa và gắn với RQ.
- [ ] “Phát hiện sớm” được định nghĩa thao tác rõ ràng.
- [ ] Có kế hoạch đo hiệu quả, độ trễ hoặc chi phí nếu phù hợp.
- [ ] Nêu số lần chạy dự kiến và cách báo cáo độ biến thiên.
- [ ] Nêu môi trường, phần cứng và thông tin phiên bản quan trọng.
- [ ] Có kế hoạch phân tích false positive/false negative.

### E. Tính tin cậy và tái lập

- [ ] Lưu kết quả thô, cấu hình, seed và log thực nghiệm.
- [ ] Dự kiến script để tính metric và tạo biểu đồ.
- [ ] Có cách ghi nhận các lần chạy thất bại và thay đổi cấu hình.
- [ ] Nhận diện các mối đe dọa đến tính hợp lệ.
- [ ] Kết luận dự kiến không vượt quá phạm vi dữ liệu và giao thức.
- [ ] Có phương án chia sẻ tài liệu/mã nguồn phù hợp điều kiện pháp lý và bảo mật.

### F. Tính khả thi và hình thức

- [ ] Nguồn lực tính toán và thời gian được ước lượng.
- [ ] Lịch trình có đầu ra cụ thể theo từng giai đoạn.
- [ ] Có khoảng thời gian dự phòng cho rủi ro kỹ thuật.
- [ ] Danh mục tài liệu tham khảo được chuẩn hóa.
- [ ] Tuân thủ biểu mẫu, cấu trúc, quy định trích dẫn và yêu cầu của trường/khoa.

---

## 14. Dàn ý mẫu có thể dùng để bắt đầu viết đề cương

Có thể sao chép và điền nội dung vào mẫu này.

```text
TÊN ĐỀ TÀI:

1. ĐẶT VẤN ĐỀ
   1.1. Bối cảnh nghiên cứu
   1.2. Vấn đề nghiên cứu
   1.3. Ý nghĩa khoa học và thực tiễn
   1.4. Mục tiêu nghiên cứu
   1.5. Câu hỏi nghiên cứu
   1.6. Phạm vi và giả định
   1.7. Đóng góp dự kiến

2. TỔNG QUAN NGHIÊN CỨU
   2.1. Khái niệm và cơ sở lý thuyết
   2.2. Phân loại các phương pháp hiện có
   2.3. Các bộ dữ liệu và chỉ số đánh giá
   2.4. So sánh các công trình liên quan
   2.5. Khoảng trống/câu hỏi chưa được giải đáp

3. PHƯƠNG PHÁP NGHIÊN CỨU
   3.1. Thiết kế nghiên cứu thực nghiệm
   3.2. Tiêu chí lựa chọn baseline
   3.3. Lựa chọn và mô tả bộ dữ liệu
   3.4. Tiền xử lý và xây dựng mẫu
   3.5. Chiến lược chia dữ liệu
   3.6. Cấu hình, huấn luyện và hiệu chỉnh
   3.7. Chỉ số đánh giá
   3.8. Thiết kế đánh giá phát hiện sớm (nếu áp dụng)
   3.9. Phương pháp phân tích kết quả
   3.10. Kiểm soát sai lệch và bảo đảm tái lập

4. KẾT QUẢ VÀ ĐÓNG GÓP DỰ KIẾN
   4.1. Các kết quả thực nghiệm dự kiến
   4.2. Các câu hỏi mà kết quả sẽ trả lời
   4.3. Đóng góp thực nghiệm dự kiến
   4.4. Giới hạn dự kiến

5. KẾ HOẠCH THỰC HIỆN

6. TÀI LIỆU THAM KHẢO

PHỤ LỤC (nếu cần)
   - Bảng trích xuất tài liệu
   - Danh sách baseline/dataset
   - Bảng metric và quy tắc tính
   - Thiết lập thực nghiệm dự kiến
```

---

## 15. Các dấu hiệu cho thấy đề cương chưa đủ mạnh

Cần xem xét lại nếu đề cương có một hoặc nhiều vấn đề sau:

- Chỉ nêu “so sánh một số thuật toán” mà không có RQ.
- Chọn mô hình và dataset chỉ vì chúng phổ biến, không giải thích sự phù hợp.
- Khoảng trống nghiên cứu được khẳng định nhưng không có bằng chứng từ tài liệu.
- Lấy F1-score từ các bài báo có thiết lập khác nhau rồi xếp hạng trực tiếp.
- Không mô tả đơn vị đánh giá và cấp độ nhãn.
- Đặt mục tiêu “early detection” nhưng chỉ đánh giá khi có toàn bộ chuỗi.
- Dùng test để chọn ngưỡng hoặc điều chỉnh mô hình.
- Không có kế hoạch phân tích lỗi, độ ổn định hoặc chi phí tính toán dù các yếu tố này liên quan trực tiếp đến RQ.
- Phạm vi quá rộng: quá nhiều mô hình, dataset, RQ hoặc kỹ thuật trong thời gian hạn chế.
- Tuyên bố sẽ chứng minh một phương pháp tốt nhất trước khi tiến hành thực nghiệm.
- Không nêu giới hạn, rủi ro và phương án xử lý khi không thể tái lập baseline.
- Không xác định được đóng góp nào mới hơn hoặc bổ sung gì so với các benchmark đã có.

---

## 16. Tài liệu hướng dẫn phương pháp nên tham khảo

Các nguồn dưới đây là tài liệu phương pháp luận hỗ trợ thiết kế và báo cáo nghiên cứu. Chúng không thay thế quy định của cơ sở đào tạo.

1. **ACM SIGSOFT Empirical Standards for Software Engineering** — tiêu chuẩn và checklist về mục tiêu/câu hỏi nghiên cứu, phương pháp, phân tích dữ liệu, kết luận, giới hạn và khả năng tái lập:  
   <https://www2.sigsoft.org/EmpiricalStandards/>
2. **ACM SIGSOFT Empirical Standards — Standards** — mô tả các thuộc tính thiết yếu, mong muốn và tiêu chí chất lượng theo loại nghiên cứu:  
   <https://www2.sigsoft.org/EmpiricalStandards/docs/standards>
3. **PRISMA 2020** — hướng dẫn báo cáo systematic review nếu đề tài có thực hiện tổng quan tài liệu có hệ thống; không phải yêu cầu bắt buộc cho mọi nghiên cứu benchmarking:  
   <https://www.prisma-statement.org/prisma-2020>

Khi dùng các hướng dẫn này, hãy chọn đúng phần tương ứng với thiết kế của mình. Không áp dụng máy móc một checklist của loại nghiên cứu khác.

---

## 17. Kết luận

Một đề cương luận văn thạc sĩ theo hướng nghiên cứu cấp độ 1 cần cho thấy rõ **vấn đề đáng nghiên cứu, câu hỏi có thể trả lời, thiết kế thực nghiệm công bằng, dữ liệu và chỉ số phù hợp, kế hoạch phân tích có chiều sâu, giới hạn được nhận diện và đầu ra khả thi**.

Đối với đề tài phát hiện sớm bất thường log, nên đặc biệt bảo đảm ba điều:

1. Không đồng nhất hiệu quả phân loại cuối chuỗi với khả năng phát hiện sớm.
2. Không đưa ra so sánh thiếu công bằng giữa các mô hình hoặc dataset có định nghĩa nhãn và giao thức khác nhau.
3. Không xem một bảng F1-score là toàn bộ kết quả nghiên cứu; cần giải thích điều kiện hoạt động, lỗi, độ ổn định và chi phí khi chúng liên quan đến RQ.

Nếu đề cương đáp ứng được các tiêu chí này, nghiên cứu cấp độ 1 có thể tạo ra một nền tảng thực nghiệm vững chắc. Nó cũng giúp xác định những hạn chế cụ thể cần được khảo sát tiếp, mà không phải cam kết trước rằng luận văn nhất định phải đề xuất một thuật toán mới.
