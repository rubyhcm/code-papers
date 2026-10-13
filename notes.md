Seed (random seed — hạt giống ngẫu nhiên)

Nhiều phương pháp học máy có yếu tố ngẫu nhiên: khởi tạo trọng số mạng nơ-ron, shuffle dữ liệu, random sampling... Nếu chạy 2 lần không cố định seed, kết quả sẽ khác 
nhau mỗi lần, không ai biết số nào là đúng.

Cố định seed (ví dụ seed = 42) có nghĩa: buộc tất cả phương pháp dùng cùng một chuỗi số ngẫu nhiên → đảm bảo kết quả có thể tái lập (reproducible). Người khác chạy lại
code của bạn với cùng seed sẽ ra đúng con số đó.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


std (standard deviation — độ lệch chuẩn)

Dù đã cố định seed, một số phương pháp vẫn có biến thiên giữa các lần chạy (ví dụ: random sampling trong LogRAG, khởi tạo khác nhau). Vì vậy cần chạy lặp nhiều lần (v
í dụ 5 lần) rồi báo cáo:

│ F1 = 0.923 ± 0.008

Con số sau ± chính là std — cho biết kết quả ổn định hay bất ổn. Std nhỏ = phương pháp ổn định; std lớn = kết quả phụ thuộc nhiều vào may rủi khởi tạo, cần thận trọng 
khi kết luận.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Tại sao quan trọng với luận văn này?

Vì bạn so sánh 6 phương pháp — nếu phương pháp A đạt F1 = 0.91 và phương pháp B đạt F1 = 0.90, kết luận A tốt hơn B chỉ có giá trị khi std của cả hai đủ nhỏ (ví dụ ±
0.003). Nếu std của B là ±0.02 thì hai phương pháp thực chất không khác nhau có ý nghĩa thống kê.

8% > std và seed trong phần đánh giá là gì?

> std (standard deviation — độ lệch chuẩn) và seed là hai khái niệm kiểm soát chất lượng thực nghiệm:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Seed (random seed — hạt giống ngẫu nhiên)

Nhiều phương pháp học máy có yếu tố ngẫu nhiên: khởi tạo trọng số mạng nơ-ron, shuffle dữ liệu, random sampling... Nếu chạy 2 lần không cố định seed, kết quả sẽ khác 
nhau mỗi lần, không ai biết số nào là đúng.

Cố định seed (ví dụ seed = 42) có nghĩa: buộc tất cả phương pháp dùng cùng một chuỗi số ngẫu nhiên → đảm bảo kết quả có thể tái lập (reproducible). Người khác chạy lại
code của bạn với cùng seed sẽ ra đúng con số đó.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


std (standard deviation — độ lệch chuẩn)

Dù đã cố định seed, một số phương pháp vẫn có biến thiên giữa các lần chạy (ví dụ: random sampling trong LogRAG, khởi tạo khác nhau). Vì vậy cần chạy lặp nhiều lần (v
í dụ 5 lần) rồi báo cáo:

│ F1 = 0.923 ± 0.008

Con số sau ± chính là std — cho biết kết quả ổn định hay bất ổn. Std nhỏ = phương pháp ổn định; std lớn = kết quả phụ thuộc nhiều vào may rủi khởi tạo, cần thận trọng 
khi kết luận.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Tại sao quan trọng với luận văn này?

Vì bạn so sánh 6 phương pháp — nếu phương pháp A đạt F1 = 0.91 và phương pháp B đạt F1 = 0.90, kết luận A tốt hơn B chỉ có giá trị khi std của cả hai đủ nhỏ (ví dụ ±
0.003). Nếu std của B là ±0.02 thì hai phương pháp thực chất không khác nhau có ý nghĩa thống kê.

 ▸ Credits: 0.34 • Time: 10s

9% > có nên đặt seed cố định không?

> Có, và đây là thực hành bắt buộc trong nghiên cứu thực nghiệm. Nhưng cần hiểu đúng vai trò của nó.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Seed cố định để làm gì

Để tái lập được (reproducibility) — người khác chạy lại code của bạn với cùng seed ra đúng con số đó. Đây là yêu cầu tối thiểu của ACM SIGSOFT Empirical Standards mà 
luận văn bạn đã cam kết tuân theo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Nhưng seed cố định không đủ một mình

Seed cố định chỉ đảm bảo cùng một người chạy lại được kết quả giống nhau. Nó không trả lời câu hỏi: "kết quả này có ổn định không, hay chỉ may mắn với seed đó?"

Vì vậy cần làm thêm: chạy lặp với nhiều seed khác nhau (ví dụ 5 lần với seed = 0, 1, 2, 3, 4), rồi báo cáo trung bình ± std. Đây mới là bằng chứng thống kê thuyết phụ
c.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Thực tế với 6 phương pháp của bạn

| Phương pháp | Yếu tố ngẫu nhiên | Cần chạy lặp? |
|---|---|---|
| LightAD (KNN/DT) | Gần như không có | Ít cần, nhưng vẫn nên |
| SemPCA | PCA xác định, seed ảnh hưởng nhỏ | Ít cần |
| LogFormer | Khởi tạo trọng số, dropout | Cần |
| CoLog | Khởi tạo trọng số | Cần |
| Logs2Graph | Khởi tạo GNN | Cần |
| LogRAG | DeepSVDD + sampling LLM | Rất cần — LLM không deterministc |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Khuyến nghị thực tế

Cố định seed = 42 (hoặc bộ seed 42, 0, 1, 2, 3) cho tất cả. Chạy ít nhất 3 lần cho các phương pháp có học sâu. Với LightAD/SemPCA chạy 1 lần cũng chấp nhận được nếu 
ghi rõ lý do.

Riêng LogRAG cần ghi chú thêm rằng phần LLM có thể không hoàn toàn deterministic dù cố định seed phía Python — đây là giới hạn kỹ thuật cần nêu trong phần Threats to 
Validity.

 ▸ Credits: 0.35 • Time: 10s

9% > làm sao biết chọn seed bao nhiêu?

> Không có quy tắc khoa học nào để chọn con số cụ thể. Seed chỉ là một số nguyên bất kỳ để khởi tạo bộ sinh số ngẫu nhiên — bản thân con số không có ý nghĩa gì.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Tại sao 42 phổ biến đến vậy?

Đây là truyền thống trong cộng đồng ML/research, xuất phát từ cuốn tiểu thuyết khoa học viễn tưởng The Hitchhiker's Guide to the Galaxy của Douglas Adams — trong đó 42
là "câu trả lời cho mọi câu hỏi trong vũ trụ". Không có lý do thống kê nào cả, chỉ là quy ước không chính thức.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Điều thực sự quan trọng

Không phải chọn seed bao nhiêu, mà là:

1. Chọn trước khi chạy, không phải sau khi thấy kết quả. Nếu bạn thử seed 1, 2, 3... rồi chọn seed nào cho kết quả đẹp nhất để báo cáo — đó là gian lận thực nghiệm (*
seed hacking*), tương tự p-hacking trong thống kê.

2. Ghi rõ seed đã dùng trong phụ lục để người khác tái lập được.

3. Dùng nhiều seed nếu muốn kết quả đáng tin — chạy với seed = 0, 1, 2, 3, 4 rồi lấy trung bình ± std. Lúc này con số cụ thể của từng seed không còn quan trọng nữa.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


Kết luận thực tế cho luận văn

Chọn seed = 42 cho đơn giản, nhất quán, dễ giải thích. Quan trọng hơn là dùng nó nhất quán cho tất cả 6 phương pháp — không phải mỗi phương pháp một seed khác nhau.
