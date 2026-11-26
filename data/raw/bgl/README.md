# BGL dataset provenance

## Trạng thái hiện tại

Thư mục này chứa `BGL.log` (4.747.963 dòng). Mỗi dòng có nhãn alert trong
cột đầu tiên:

- `-`: non-alert/Normal.
- bất kỳ category khác `-`: alert/Anomaly.

Các category alert ví dụ gồm `KERNDTLB`, `APPSEV`, `KERNMNTF`.

Đây là ground-truth line-level do dataset mô tả. Parser gắn nhãn trực tiếp
từ cột đầu tiên; không suy nhãn từ `WARN`, `FATAL`, `SEVERE` hoặc template.

Trạng thái split mặc định: fixed windows 200 dòng, chronological 80/10/10.
Window được gắn nhãn Anomaly nếu chứa ít nhất một dòng alert.
