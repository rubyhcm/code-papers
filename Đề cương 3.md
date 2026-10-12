# Cấp độ 1 trong nghiên cứu khoa học: Đánh giá thực nghiệm và benchmarking

Đối với đề tài luận văn **“Phát hiện sớm bất thường bằng phân tích dữ liệu log dựa trên trí tuệ nhân tạo”** (*Early Log Anomaly Detection using Artificial Intelligence*), cấp độ 1 không đơn thuần là lấy vài thuật toán có sẵn, chạy thử rồi so sánh xem thuật toán nào có F1-score cao nhất.

Nếu thực hiện một cách nghiêm túc, cấp độ 1 là một quá trình nghiên cứu có hệ thống nhằm trả lời câu hỏi:

> **Các phương pháp phát hiện bất thường log hiện có hoạt động như thế nào, phương pháp nào phù hợp với từng điều kiện, vì sao chúng hoạt động tốt hoặc kém, và chúng ta rút ra được những hiểu biết gì từ kết quả thực nghiệm?**

Bạn không nhất thiết phải tạo ra thuật toán mới. Giá trị chính của nghiên cứu nằm ở cách đặt câu hỏi, thiết kế thí nghiệm, kiểm soát điều kiện, phân tích kết quả và rút ra kết luận có căn cứ.

## 1. Bản chất của cấp độ 1

Có thể chia công việc thành ba mức thực hiện khác nhau. Đây là cách phân biệt thực hành để dễ hình dung, không phải hệ thống phân loại chính thức của giới học thuật.

### Mức A — Chạy thử các phương pháp

Chọn một vài thuật toán, chạy trên một hoặc hai tập dữ liệu, ghi nhận điểm số và xếp hạng kết quả.

Đây thường là bước khởi đầu để làm quen với bài toán, chưa nhất thiết đủ để tạo thành một nghiên cứu độc lập có đóng góp rõ ràng.

### Mức B — Benchmarking có hệ thống

Xây dựng bộ tiêu chí, chọn baseline phù hợp, kiểm soát điều kiện đánh giá, so sánh nhiều phương pháp và phân tích kết quả.

Mục tiêu là trả lời được phương pháp nào tốt hơn, trong điều kiện nào và kết quả có đáng tin cậy hay không. Đây là nền tảng của cấp độ 1.

### Mức C — Nghiên cứu thực nghiệm chuyên sâu

Ngoài benchmarking, tiến hành phân tích lỗi, khảo sát các yếu tố ảnh hưởng, kiểm tra khả năng tổng quát hóa và giải thích cơ chế khiến mô hình thành công hoặc thất bại.

Đây vẫn có thể là cấp độ 1, miễn là mục tiêu chính là tạo ra hiểu biết thực nghiệm chứ không nhất thiết đề xuất phương pháp mới.

**Điểm mấu chốt:** cấp độ 1 vẫn có thể tạo ra đóng góp khoa học mà không cần cải tiến thuật toán. Đóng góp đó có thể là bằng chứng thực nghiệm đáng tin cậy, phát hiện về giới hạn của các phương pháp, kết quả so sánh trong điều kiện mới hoặc hướng dẫn lựa chọn phương pháp phù hợp với từng loại dữ liệu.

## 2. Mục tiêu của một nghiên cứu cấp độ 1

Một nghiên cứu benchmarking nghiêm túc thường có bốn mục tiêu chính.

### 2.1. Xác định phương pháp nào thực sự hiệu quả

Bạn không chỉ muốn biết mô hình A đạt F1-score 0,95 còn mô hình B đạt 0,93. Bạn muốn biết liệu chênh lệch đó có đáng tin cậy hay không, liệu nó có lặp lại trên các tập dữ liệu khác không và liệu có đánh đổi nào giữa các tiêu chí không.

Ví dụ, một mô hình có Recall cao nhưng Precision thấp sẽ phát hiện được nhiều bất thường thực sự, nhưng cũng có thể tạo ra quá nhiều cảnh báo sai. Nếu hệ thống vận hành phải xử lý từng cảnh báo, điều này có thể làm tăng đáng kể khối lượng công việc của đội vận hành.

### 2.2. Xác định phương pháp phù hợp với từng điều kiện

Không nhất thiết có một phương pháp tốt nhất trong mọi trường hợp. Bạn có thể khảo sát các điều kiện như:

- Dữ liệu có nhiều hay ít mẫu bất thường.
- Log có cấu trúc ổn định hay thường xuyên xuất hiện mẫu mới.
- Có nhãn bất thường đầy đủ hay chỉ có dữ liệu bình thường để huấn luyện.
- Cần phát hiện theo từng dòng log, từng chuỗi sự kiện hay từng phiên xử lý.
- Có giới hạn về thời gian suy luận, bộ nhớ hoặc tài nguyên tính toán hay không.

Ví dụ, nghiên cứu về phát hiện bất thường log có thể phân biệt những phương pháp sử dụng thông tin tuần tự với những phương pháp khai thác ngữ nghĩa của log. Các phương pháp khác nhau có thể thể hiện ưu, nhược điểm khác nhau tùy thuộc dạng dữ liệu và điều kiện thực nghiệm.

### 2.3. Giải thích vì sao một phương pháp tốt hoặc kém

Đây là điểm phân biệt quan trọng giữa việc chạy thử nghiệm và nghiên cứu thực nghiệm.

Giả sử DeepLog hoạt động tốt trên HDFS nhưng không tốt trên BGL. Thay vì chỉ kết luận mô hình không phù hợp, bạn cần điều tra các khả năng:

- Bản chất dữ liệu và cách gán nhãn khác nhau.
- Số lượng mẫu bất thường, mức mất cân bằng lớp và độ phức tạp của chuỗi log khác nhau.
- Các mẫu trong tập kiểm thử có khác biệt so với dữ liệu huấn luyện hay không.
- Cách tiền xử lý, phân nhóm log hoặc chia tập dữ liệu ảnh hưởng đến kết quả như thế nào.

Các yếu tố trên là những giả thuyết để kiểm tra; chỉ khi có bằng chứng mới có thể kết luận chúng là nguyên nhân.

### 2.4. Rút ra kiến thức hữu ích cho nghiên cứu tiếp theo

Kết quả cuối cùng có thể là một tập hợp các phát hiện như:

- Phương pháp nào hoạt động ổn định hơn trên nhiều bộ dữ liệu.
- Những điều kiện khiến các mô hình học sâu suy giảm hiệu suất.
- Mức đánh đổi giữa độ chính xác và độ trễ phát hiện.
- Các thiết lập thực nghiệm dễ dẫn đến kết quả không đáng tin cậy.
- Những hạn chế còn tồn tại có thể trở thành hướng cải tiến ở nghiên cứu tiếp theo.

Đây là cách một nghiên cứu cấp độ 1 có thể trở thành nền tảng trực tiếp cho cấp độ 2.

## 3. Quy trình thực hiện một nghiên cứu cấp độ 1

Với đề tài của bạn, có thể dùng quy trình gồm tám bước. Điểm quan trọng là xác định câu hỏi nghiên cứu trước khi chạy mô hình, tránh việc chạy hàng loạt phương pháp rồi mới tìm một câu chuyện để giải thích kết quả.

### Bước 1 — Xác định phạm vi và câu hỏi nghiên cứu

Xác định rõ đối tượng nghiên cứu, loại bất thường, loại log và tiêu chí đánh giá.

Ví dụ, thay vì đặt câu hỏi quá rộng như “Phương pháp phát hiện bất thường log nào tốt nhất?”, có thể hỏi:

> Các phương pháp phát hiện bất thường dựa trên chuỗi log duy trì độ chính xác và khả năng phát hiện sớm như thế nào khi chỉ quan sát được một phần chuỗi sự kiện?

**Sản phẩm:** mục tiêu nghiên cứu và các câu hỏi nghiên cứu (*Research Questions — RQs*).

### Bước 2 — Tổng quan tài liệu và chọn các phương pháp đại diện

Khảo sát nghiên cứu liên quan, phân loại cách tiếp cận, xác định phương pháp nào phù hợp với câu hỏi nghiên cứu và tìm mã nguồn nếu có.

Ví dụ, có thể khảo sát DeepLog, LogAnomaly, LogRobust, LogBERT và một số phương pháp gần đây. Đây chỉ là danh sách khởi đầu, không phải danh sách bắt buộc hay khẳng định rằng các mô hình này đều là lựa chọn tốt nhất hiện nay.

**Sản phẩm:** bảng tổng hợp các phương pháp, cơ chế chính, yêu cầu dữ liệu và hạn chế được báo cáo.

### Bước 3 — Lựa chọn bộ dữ liệu và kiểm tra chất lượng dữ liệu

Xác định bộ dữ liệu có phù hợp với bài toán hay không, nhãn được gán ở cấp độ nào, cách nhóm log thành mẫu và liệu có đủ thông tin để đánh giá khả năng phát hiện sớm hay không.

Ví dụ, HDFS thường gán nhãn theo phiên xử lý hoặc block, trong khi BGL có nhãn ở cấp độ từng dòng log. Sự khác biệt này ảnh hưởng đến cách xây dựng mẫu và tính các chỉ số đánh giá.

**Sản phẩm:** bộ dữ liệu đã được kiểm tra, tài liệu mô tả dữ liệu và quy tắc tiền xử lý.

### Bước 4 — Thiết kế giao thức thực nghiệm

Xác định cách chia tập huấn luyện, xác thực và kiểm thử; cách lựa chọn siêu tham số; cấu hình phần cứng; số lần chạy và tiêu chí so sánh.

**Sản phẩm:** một giao thức mà người khác có thể đọc và thực hiện lại.

### Bước 5 — Triển khai và chạy các phương pháp

Sử dụng mã nguồn chính thức hoặc tái triển khai theo bài báo nếu cần. Kiểm tra rằng kết quả có hợp lý so với các kết quả tham chiếu, ghi lại lỗi thực nghiệm và cấu hình thực sự đã sử dụng.

**Sản phẩm:** mã nguồn, cấu hình, log chạy và kết quả thô.

### Bước 6 — Phân tích định lượng và định tính

Không dừng ở bảng F1-score. Hãy phân tích chênh lệch kết quả, kiểu lỗi, độ ổn định, tốc độ suy luận và ảnh hưởng của các điều kiện dữ liệu.

**Sản phẩm:** bảng kết quả, biểu đồ, phân tích các trường hợp mô hình phát hiện sai hoặc bỏ sót.

### Bước 7 — Kiểm tra tính hợp lệ và khả năng tái lập

Kiểm tra nguy cơ rò rỉ dữ liệu, tính nhất quán của các lần chạy, ảnh hưởng của thiết lập thực nghiệm và giới hạn của các bộ dữ liệu được chọn.

**Sản phẩm:** bằng chứng về độ tin cậy của kết quả, cùng những giới hạn còn lại.

### Bước 8 — Tổng hợp phát hiện và trả lời RQs

Viết kết luận dựa trên dữ liệu thực nghiệm, nêu phạm vi mà kết quả áp dụng được và tránh khái quát hóa quá mức.

**Sản phẩm:** các phát hiện khoa học có căn cứ, khuyến nghị lựa chọn phương pháp và những câu hỏi nghiên cứu còn mở.

Quy trình này phù hợp với các nguyên tắc cốt lõi của nghiên cứu thực nghiệm trong khoa học phần mềm: nêu rõ câu hỏi và động cơ, mô tả cách thu thập và phân tích dữ liệu, đưa ra kết luận gắn với bằng chứng, công khai giới hạn và đóng góp vào tri thức chung.

## 4. Xây dựng câu hỏi nghiên cứu như thế nào?

Câu hỏi nghiên cứu quyết định bạn cần thu thập loại dữ liệu nào, chạy những thực nghiệm gì và kết luận được điều gì. Với đề tài này, có thể bắt đầu bằng năm câu hỏi sau.

### RQ1 — Hiệu quả phát hiện

**Các phương pháp hiện có đạt hiệu quả phát hiện bất thường log như thế nào trên các bộ dữ liệu chuẩn?**

- **Thực nghiệm:** so sánh Precision, Recall, F1-score và PR-AUC nếu có điểm số dự đoán phù hợp.
- **Phân tích:** xem kết quả theo từng bộ dữ liệu và từng phương pháp.

### RQ2 — Tính nhất quán

**Hiệu quả của các phương pháp có ổn định giữa các bộ dữ liệu có đặc tính khác nhau hay không?**

- **Thực nghiệm:** so sánh mức thay đổi hiệu suất giữa các tập dữ liệu, khả năng xử lý mẫu log chưa gặp và ảnh hưởng của sự mất cân bằng lớp.

### RQ3 — Phát hiện sớm

**Hiệu quả phát hiện thay đổi như thế nào khi mô hình chỉ nhận được một phần của chuỗi log?**

- **Thực nghiệm:** đánh giá mô hình khi nhận 10%, 25%, 50%, 75% và 100% chuỗi log, nếu cách xây dựng mẫu và nhãn cho phép.
- **Mục tiêu:** đo độ nhạy phát hiện theo lượng thông tin đã quan sát.

### RQ4 — Hiệu năng tính toán

**Các phương pháp đánh đổi độ chính xác lấy chi phí tính toán như thế nào?**

- **Thực nghiệm:** đo thời gian huấn luyện, độ trễ suy luận, thông lượng xử lý và bộ nhớ trên cùng môi trường hoặc các môi trường được mô tả rõ ràng.

### RQ5 — Phân tích lỗi

**Những kiểu bất thường nào thường bị bỏ sót hoặc tạo ra cảnh báo sai, và các lỗi đó có liên quan đến đặc tính dữ liệu hay không?**

- **Thực nghiệm:** kiểm tra các mẫu False Positive và False Negative, phân nhóm lỗi và tìm mối liên hệ với cấu trúc log, độ dài chuỗi hoặc độ phổ biến của mẫu.

Bạn không nhất thiết phải giữ cả năm câu hỏi. Với một luận văn thạc sĩ, ba hoặc bốn câu hỏi được nghiên cứu sâu thường tốt hơn năm câu hỏi nhưng mỗi câu chỉ có một bảng kết quả.

Đặc biệt, RQ3 phù hợp trực tiếp với mục tiêu *Early Log Anomaly Detection*. Nó giúp nghiên cứu khác với một bài benchmarking chỉ đánh giá khả năng phân loại bình thường/bất thường trên toàn bộ chuỗi.

Một nguyên tắc hữu ích: **mỗi câu hỏi phải gắn với một thiết kế phân tích cụ thể, và mỗi kết luận phải trả lời trực tiếp câu hỏi đó**.

## 5. Chọn phương pháp và dữ liệu để so sánh

### 5.1. Không chọn mô hình chỉ vì chúng nổi tiếng

Bạn nên chọn một nhóm phương pháp đủ đại diện cho các cách tiếp cận khác nhau, nhưng vẫn có thể đánh giá công bằng.

| Nhóm phương pháp | Ví dụ minh họa | Điều cần khảo sát |
|---|---|---|
| Thống kê hoặc dựa trên tần suất | Ngưỡng tần suất, mô hình thống kê | Có thể phát hiện những bất thường đơn giản đến đâu? |
| Học máy truyền thống | Isolation Forest hoặc mô hình phân loại phù hợp | Hiệu quả khi sử dụng đặc trưng được trích xuất từ log |
| Mô hình học chuỗi | DeepLog, LogAnomaly | Vai trò của thứ tự sự kiện và ngữ cảnh chuỗi |
| Biểu diễn ngữ nghĩa hoặc Transformer | LogBERT, LogRobust và các phương pháp phù hợp khác | Lợi ích của biểu diễn ngữ nghĩa, khả năng tổng quát hóa và chi phí tính toán |

Các ví dụ trên không có nghĩa mọi mô hình đều có thể được so sánh trực tiếp trong một bảng duy nhất. Chúng có thể khác nhau về cách học, nhãn cần thiết, cách phân nhóm mẫu và định nghĩa bất thường.

Bạn nên ghi nhận tối thiểu các thông tin cho từng phương pháp: kiểu học (*supervised*, *semi-supervised* hoặc *unsupervised*), dữ liệu huấn luyện cần thiết, cách biểu diễn log, cơ chế phát hiện, mã nguồn và cấu hình có thể tái lập.

### 5.2. Chọn tập dữ liệu theo câu hỏi nghiên cứu

Một số bộ dữ liệu thường được dùng trong nghiên cứu phát hiện bất thường log gồm:

| Bộ dữ liệu | Ý nghĩa đối với thực nghiệm |
|---|---|
| HDFS | Phù hợp để khảo sát chuỗi log theo phiên xử lý hoặc block khi sử dụng đúng quy tắc gán nhãn. |
| BGL | Hữu ích khi khảo sát log hệ thống siêu máy tính và nhãn ở cấp độ dòng log. |
| Thunderbird | Có thể bổ sung một môi trường log khác để kiểm tra mức độ nhất quán của kết quả. |
| OpenStack hoặc các tập log ứng dụng khác | Có thể mở rộng đánh giá sang những bối cảnh hệ thống khác nếu dữ liệu, nhãn và cách phân nhóm phù hợp. |

Đây là danh sách gợi ý, không phải yêu cầu phải dùng tất cả các bộ dữ liệu trên. Bạn nên ưu tiên các bộ dữ liệu mà mình có thể tái lập việc tiền xử lý, hiểu rõ nhãn và thực hiện đúng phép đánh giá.

**Nhiều bộ dữ liệu không tự động làm nghiên cứu tốt hơn.** Ba bộ dữ liệu khác nhau về bản chất, được xử lý đúng và phân tích sâu thường có giá trị hơn nhiều bộ dữ liệu nhưng không đủ điều kiện so sánh công bằng.

### 5.3. Phân biệt kết quả đã công bố với benchmarking của chính bạn

Có hai cách làm chính:

- **So sánh từ tài liệu:** tổng hợp kết quả mà từng bài báo công bố. Cách này nhanh hơn nhưng số liệu có thể đến từ cách chia dữ liệu, tiền xử lý, nhãn, phần cứng và quy trình hiệu chỉnh siêu tham số khác nhau.
- **Benchmarking trực tiếp:** chạy lại các phương pháp theo một giao thức chung khi có thể. Cách này tốn công hơn nhưng thường giúp so sánh chặt chẽ hơn.

Bạn có thể sử dụng kết quả đã công bố để xây dựng bảng tổng quan tài liệu và tham khảo mức hiệu quả dự kiến. Tuy nhiên, không nên mặc định rằng mô hình đạt F1-score cao nhất trong một bài báo chắc chắn sẽ tốt nhất trên thiết lập của bạn.

## 6. Thiết kế thực nghiệm sao cho đáng tin cậy

Đây là phần quyết định sự khác nhau giữa một thử nghiệm kỹ thuật thông thường và một nghiên cứu thực nghiệm nghiêm túc.

### 6.1. Kiểm soát cách chia dữ liệu

Với mỗi tập dữ liệu, bạn cần xác định rõ dữ liệu nào dùng để huấn luyện, dữ liệu nào dùng để điều chỉnh mô hình và dữ liệu nào chỉ dùng để đánh giá cuối cùng.

Một quy trình phổ biến là:

1. **Train:** học tham số mô hình.
2. **Validation:** chọn siêu tham số và ngưỡng.
3. **Test:** đánh giá cuối cùng.

Không sử dụng nhãn tập kiểm thử để điều chỉnh mô hình hoặc lựa chọn ngưỡng.

Chia ngẫu nhiên có thể không phù hợp nếu dữ liệu có thứ tự thời gian hoặc các mẫu chồng lấn. Nếu mục tiêu là đánh giá khi triển khai thực tế, chia theo thời gian thường là lựa chọn đáng cân nhắc: huấn luyện trên dữ liệu trước, kiểm thử trên dữ liệu về sau.

Trong nghiên cứu phát hiện bất thường log, một số thiết kế chia dữ liệu theo thứ tự thời gian nhằm hạn chế rò rỉ dữ liệu giữa tập huấn luyện và kiểm thử. Mẫu trùng lặp cũng cần được xem xét vì các mẫu giống nhau có thể xuất hiện ở cả hai tập.

Không có một cách chia tập đúng cho tất cả bài toán. Bạn cần lựa chọn theo giả định triển khai và giải thích lý do.

### 6.2. Kiểm soát công bằng giữa các phương pháp

Bạn cần xác định rõ điều gì được giữ giống nhau và điều gì được phép khác nhau.

Các yếu tố nên kiểm soát hoặc báo cáo gồm:

- Cách chia tập dữ liệu.
- Tiền xử lý và cách xây dựng mẫu.
- Tiêu chí dừng huấn luyện.
- Quy tắc hiệu chỉnh ngưỡng.
- Tài nguyên tính toán và phiên bản thư viện.
- Siêu tham số và ngân sách tìm kiếm siêu tham số.

Không phải lúc nào cũng ép các mô hình dùng cùng một cách tiền xử lý nếu điều đó mâu thuẫn với thiết kế gốc của mô hình. Khi cần sử dụng các thiết lập đặc thù, hãy ghi rõ chúng, tránh tạo lợi thế không công bằng cho một phương pháp.

Tương tự, nếu một mô hình được phép sử dụng nhãn bất thường trong huấn luyện còn mô hình kia chỉ học từ dữ liệu bình thường, cần báo cáo rõ khác biệt đó. Hai phương pháp không hoạt động dưới cùng giả định nên kết quả không thể diễn giải như một phép so sánh hoàn toàn tương đương.

### 6.3. Kiểm tra tính ổn định

Nếu mô hình có yếu tố ngẫu nhiên, bạn nên chạy nhiều lần với những seed khác nhau khi tài nguyên cho phép. Báo cáo giá trị trung bình và độ biến thiên, thay vì chỉ lấy lần chạy tốt nhất.

Nếu phù hợp với câu hỏi nghiên cứu, bạn có thể sử dụng khoảng tin cậy hoặc kiểm định thống kê. Không nhất thiết phải dùng kiểm định phức tạp trong mọi trường hợp; hãy chọn phương pháp phân tích phù hợp với dạng dữ liệu và thiết kế so sánh.

## 7. Đánh giá bằng những chỉ số nào?

Đây là phần đặc biệt quan trọng với đề tài của bạn, vì **phát hiện bất thường chính xác và phát hiện bất thường sớm là hai mục tiêu liên quan nhưng không giống nhau**.

### 7.1. Các chỉ số phát hiện bất thường cơ bản

| Chỉ số | Ý nghĩa | Câu hỏi được trả lời |
|---|---|---|
| Precision | Tỷ lệ dự đoán bất thường đúng trong số các dự đoán bất thường | Cảnh báo của mô hình đáng tin đến đâu? |
| Recall | Tỷ lệ bất thường thực sự được phát hiện | Mô hình bỏ sót bao nhiêu bất thường? |
| F1-score | Trung bình điều hòa của Precision và Recall | Cân bằng giữa khả năng phát hiện và cảnh báo đúng ra sao? |
| PR-AUC | Diện tích dưới đường cong Precision–Recall | Khả năng phân biệt bất thường ở các ngưỡng khác nhau như thế nào? |
| False Positive Rate | Tỷ lệ mẫu bình thường bị dự đoán thành bất thường | Mô hình gây ra bao nhiêu cảnh báo sai trên dữ liệu bình thường? |

Các chỉ số này thường được sử dụng trong nghiên cứu log anomaly detection, nhưng ý nghĩa của chúng phụ thuộc vào cách xây dựng mẫu và định nghĩa một dự đoán đúng.

Đặc biệt, dữ liệu log thường có tỷ lệ bất thường thấp. Vì vậy, Accuracy cao không nhất thiết có nghĩa mô hình tốt. Chẳng hạn, một mô hình luôn dự đoán mọi mẫu là bình thường có thể đạt Accuracy cao nếu hầu hết dữ liệu đều bình thường, nhưng lại không phát hiện được bất thường nào.

### 7.2. Những chỉ số liên quan trực tiếp đến phát hiện sớm

Với luận văn này, chỉ số F1-score trên toàn bộ chuỗi log là chưa đủ. Bạn cần định nghĩa rõ thế nào là “sớm” và đánh giá hiệu quả dưới các điều kiện quan sát khác nhau.

#### Hiệu quả tại các tiền tố chuỗi log

Đánh giá mô hình khi chỉ quan sát một phần chuỗi sự kiện. Ví dụ, đo F1-score và Recall ở các mức 10%, 25%, 50%, 75% và 100% chuỗi.

Mục đích là kiểm tra mô hình cần bao nhiêu thông tin mới phát hiện được bất thường. Đây là phép đo phù hợp khi nhãn và cách xây dựng mẫu cho phép xác định đúng kết quả tại mỗi tiền tố.

#### Độ trễ phát hiện

Đo khoảng thời gian từ thời điểm bất thường bắt đầu hoặc có thể quan sát được, đến lần đầu mô hình phát hiện chính xác bất thường đó.

Cần định nghĩa rõ mốc bắt đầu bất thường. Nếu bộ dữ liệu chỉ có nhãn cho cả phiên xử lý mà không xác định thời điểm bất thường bắt đầu, bạn không thể mặc nhiên tính độ trễ ở cấp độ sự kiện một cách chính xác.

#### Hiệu năng phát hiện trong điều kiện thời gian thực

Đo độ trễ suy luận, số log xử lý mỗi giây và tài nguyên sử dụng khi mô hình nhận dữ liệu liên tục.

Một mô hình có Recall cao nhưng xử lý dữ liệu quá chậm có thể không phù hợp với mục tiêu phát hiện sớm trong hệ thống vận hành.

Không nhất thiết phải có một chỉ số tổng hợp duy nhất cho tất cả các mục tiêu. Nên báo cáo riêng hiệu quả phân loại, mức độ phát hiện sớm và chi phí tính toán để tránh che giấu các đánh đổi quan trọng.

## 8. Phân tích kết quả thế nào để tạo ra đóng góp khoa học?

Giả sử bạn đã chạy bốn phương pháp trên ba bộ dữ liệu. Bảng kết quả dưới đây là **ví dụ giả định để minh họa cách phân tích**, không phải kết quả thực nghiệm được công bố.

| Phương pháp | HDFS F1 | BGL F1 | Dataset C F1 | Thời gian suy luận |
|---|---:|---:|---:|---:|
| Phương pháp A | 0,95 | 0,72 | 0,84 | 8 ms |
| Phương pháp B | 0,93 | 0,89 | 0,87 | 14 ms |
| Phương pháp C | 0,96 | 0,84 | 0,80 | 5 ms |

Nếu chỉ báo cáo rằng A tốt nhất trên HDFS, B tốt nhất trên BGL và C nhanh nhất, đó mới là tóm tắt kết quả.

Một phân tích có chiều sâu sẽ tiếp tục đặt câu hỏi:

- Tại sao A có kết quả cao trên HDFS nhưng thấp hơn B trên BGL?
- Mô hình C có ưu thế về tốc độ nhưng phải đánh đổi những gì về Recall hay khả năng phát hiện sớm?
- Thứ hạng có giữ nguyên khi đánh giá trên một tập dữ liệu khác không?
- Các mô hình có ưu thế riêng đối với một kiểu bất thường nhất định không?
- Kết quả khác biệt có ổn định qua các lần chạy không?

Từ đó, bạn có thể rút ra các phát hiện có điều kiện, chẳng hạn: một mô hình có chi phí suy luận thấp nhưng khả năng tổng quát hóa kém hơn trong điều kiện kiểm thử nhất định.

Tuy nhiên, bảng điểm số tự nó không chứng minh nguyên nhân. Để giải thích vì sao kết quả khác nhau, bạn cần phân tích thêm các mẫu lỗi, dữ liệu đầu vào, cấu hình thực nghiệm hoặc các yếu tố liên quan.

### Ví dụ về một phát hiện có thể thu được

Giả sử thực nghiệm cho thấy phần lớn các mô hình đều có F1-score cao khi nhận đủ chuỗi log, nhưng Recall giảm mạnh khi chỉ quan sát 25% đầu chuỗi.

Phát hiện này có thể dẫn đến một kết luận quan trọng: hiệu quả phân loại cuối chuỗi không phản ánh đầy đủ khả năng phát hiện sớm.

Bạn chưa cần cải tiến thuật toán để có phát hiện đó. Nhưng bạn đã xác định được một vấn đề cụ thể, có bằng chứng định lượng và có thể tiếp tục nghiên cứu ở cấp độ 2.

Đó là một trong những cách mà cấp độ 1 tạo ra giá trị khoa học.

## 9. Những sai lầm thường gặp khi thực hiện cấp độ 1

### Sai lầm 1 — Chỉ chạy mô hình và xếp hạng F1-score

**Vấn đề:** chưa có câu hỏi nghiên cứu rõ ràng, phân tích nguyên nhân hoặc hiểu biết mới từ kết quả.

**Cách khắc phục:** xác định trước các RQ và phân tích sâu ít nhất những yếu tố trực tiếp liên quan đến chúng.

### Sai lầm 2 — So sánh điểm số từ nhiều bài báo như thể chúng được đo trong cùng điều kiện

**Vấn đề:** các tác giả có thể sử dụng cách tiền xử lý, chia tập và đánh giá khác nhau.

**Cách khắc phục:** phân biệt rõ tổng hợp tài liệu với benchmark chạy trực tiếp, và chỉ thực hiện đối chiếu định lượng khi điều kiện đủ tương thích.

### Sai lầm 3 — Chọn ngưỡng dựa trên tập kiểm thử

**Vấn đề:** mô hình được điều chỉnh dựa trên dữ liệu dùng để đánh giá cuối cùng, khiến kết quả lạc quan hơn thực tế.

**Cách khắc phục:** dùng tập validation để chọn ngưỡng và siêu tham số, sau đó đánh giá trên test mà không tiếp tục điều chỉnh dựa trên kết quả test.

### Sai lầm 4 — Kết luận mô hình không tốt chỉ từ một bộ dữ liệu

**Vấn đề:** kết quả có thể phản ánh đặc tính riêng của dữ liệu, chứ không phải hạn chế tổng quát của phương pháp.

**Cách khắc phục:** kiểm tra trên nhiều bộ dữ liệu hoặc các điều kiện kiểm thử khác nhau, đồng thời giới hạn phạm vi của kết luận.

### Sai lầm 5 — Xem mọi cải thiện nhỏ là có ý nghĩa khoa học

**Vấn đề:** chênh lệch điểm số có thể không ổn định, không tái lập được hoặc không đáng kể trong thực tế.

**Cách khắc phục:** đo độ biến thiên, đánh giá mức độ bất định khi phù hợp và xem xét chi phí, độ trễ cùng những tiêu chí khác ngoài F1-score.

Các vấn đề về tái lập, rò rỉ dữ liệu, lựa chọn phép thử và khái quát hóa quá mức đều thuộc phạm vi chất lượng của nghiên cứu thực nghiệm.

## 10. Sản phẩm cuối cùng của một nghiên cứu cấp độ 1

Một dự án thực nghiệm tốt nên tạo ra nhiều hơn một bảng so sánh kết quả.

| Sản phẩm | Nội dung |
|---|---|
| Tổng quan tài liệu | Phân loại phương pháp, giả định, điểm mạnh, hạn chế và khoảng trống kiến thức |
| Benchmark có thể tái lập | Mã nguồn, cấu hình, cách chia dữ liệu và quy trình chạy các mô hình |
| Báo cáo kết quả | Bảng chỉ số, biểu đồ, độ biến thiên, chi phí tính toán |
| Phân tích lỗi | Các trường hợp bỏ sót, cảnh báo sai và những điều kiện ảnh hưởng đến hiệu quả |
| Bộ phát hiện thực nghiệm | Các kết luận được hỗ trợ bằng dữ liệu và giới hạn áp dụng được nêu rõ |
| Định hướng nghiên cứu tiếp theo | Những vấn đề còn tồn tại có thể được khảo sát sâu hoặc dùng làm cơ sở cho một cải tiến |

Một nghiên cứu cấp độ 1 vẫn phải có đóng góp đủ rõ so với tri thức đã công bố. Việc lặp lại các phép thử đã biết mà không tạo ra phân tích hoặc bằng chứng mới có thể chưa đủ để trở thành một bài báo độc lập. Tuy nhiên, nghiên cứu tái lập vẫn có thể có giá trị; điều quan trọng là giá trị, độ tin cậy và tính minh bạch của kết quả.

## 11. Áp dụng cấp độ 1 vào luận văn của bạn

Với chủ đề *Early Log Anomaly Detection*, có thể bắt đầu bằng thiết kế thực nghiệm sau.

### Dữ liệu

Chọn khoảng 2–3 bộ dữ liệu có cấu trúc và cách gán nhãn phù hợp; có thể bắt đầu với HDFS và BGL, sau đó chọn thêm một bộ khác nếu cần kiểm chứng khả năng tổng quát hóa.

### Phương pháp

Chọn khoảng 3–5 baseline đại diện cho các cách tiếp cận khác nhau. Ưu tiên mã nguồn có thể chạy, thiết lập có thể tái lập và phương pháp trực tiếp liên quan đến mục tiêu phát hiện sớm.

### Chỉ số chính

Precision, Recall, F1-score và False Positive Rate; bổ sung chỉ số dựa trên tiền tố chuỗi hoặc độ trễ phát hiện khi dữ liệu cho phép. Đo chi phí suy luận để đánh giá tính khả thi thực tế.

### Phân tích sâu

Kiểm tra sự khác biệt giữa các dữ liệu, độ nhạy theo độ dài chuỗi, những kiểu lỗi thường gặp và tính ổn định của kết quả. Không chỉ dừng ở việc xếp hạng mô hình.

### Đầu ra nghiên cứu

Một giao thức benchmark có thể tái lập, các kết quả thực nghiệm, câu trả lời cho RQs và một tập hợp những vấn đề còn tồn tại có bằng chứng hỗ trợ.

Sau khi hoàn thành bước này, bạn có thể đưa ra một quyết định dựa trên dữ liệu: dừng ở nghiên cứu đánh giá thực nghiệm nếu đó là mục tiêu của dự án, hoặc chuyển sang cấp độ 2 nếu một vấn đề cụ thể đủ quan trọng và khả thi để giải quyết.

## Kết luận

**Cấp độ 1 không phải là “chưa có đóng góp vì chưa tạo ra thuật toán mới”. Đó là nghiên cứu lấy bằng chứng thực nghiệm làm trung tâm.** Chất lượng của nó phụ thuộc vào câu hỏi nghiên cứu, độ chặt chẽ của thiết kế, khả năng tái lập và những hiểu biết mới mà kết quả mang lại.

Với luận văn của bạn, hướng hợp lý nhất là dùng cấp độ 1 để xác định *baseline nào thực sự phù hợp, điểm mạnh và hạn chế của nó là gì, và vấn đề nào đủ bằng chứng để trở thành mục tiêu cải tiến*. Điều đó giúp bước sang cấp độ 2 có cơ sở rõ ràng hơn, thay vì chọn một component để bổ sung chỉ vì nó đang được quan tâm.

## Tài liệu và chuẩn tham khảo nên tra cứu

Để sử dụng nội dung này trong luận văn hoặc phát triển thành một nghiên cứu chính thức, nên tra cứu và trích dẫn trực tiếp các nguồn gốc phù hợp, chẳng hạn:

- **ACM SIGSOFT Empirical Standards** — hướng dẫn về chất lượng, minh bạch và khả năng tái lập của các loại nghiên cứu thực nghiệm trong kỹ thuật phần mềm.
- **Các bài tổng quan về log-based anomaly detection** — dùng để kiểm tra cách phân loại phương pháp, các bộ dữ liệu chuẩn và chỉ số đánh giá.
- **Các bài báo gốc của DeepLog, LogAnomaly, LogRobust và LogBERT** — dùng để xác minh cơ chế, yêu cầu dữ liệu, giao thức đánh giá và giới hạn mà từng công trình thực sự báo cáo.
- **Tài liệu gốc của các bộ dữ liệu HDFS, BGL, Thunderbird và OpenStack** — dùng để xác minh nguồn dữ liệu, cách gán nhãn và các quy tắc tiền xử lý.

Lưu ý: ví dụ, tên phương pháp, bộ dữ liệu và các RQ trong tài liệu này là gợi ý để thiết kế nghiên cứu; cần kiểm tra bài báo gốc và điều kiện cụ thể trước khi đưa ra kết luận khoa học.
