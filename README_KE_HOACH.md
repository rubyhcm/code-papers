# HỆ THỐNG TÀI LIỆU LUẬN VĂN THẠC SĨ

## 📚 Cấu trúc Tài liệu

### 1. Đề cương chính thức (cho nhà trường)
**File:** `S01.QuiTrinh.Mẫu 2_De cuong LVThS.md`  
**Người đọc:** Giáo viên hướng dẫn, Hội đồng khoa  
**Mục đích:** Đăng ký đề tài, phê duyệt chính thức  
**Nội dung:**
- Giới thiệu đề tài
- Mục tiêu (3 mục tiêu chính)
- Nội dung nghiên cứu (ND1-ND3)
- Phương pháp thực hiện
- Kết quả dự kiến
- Kế hoạch 6 tháng (T1-T6) - tổng quan

**Format:** Theo mẫu chuẩn của trường

---

### 2. Kế hoạch thực hiện chi tiết (cho theo dõi tiến độ)
**File:** `ke_hoach_thuc_hien.md`  
**Người đọc:** Học viên, người hướng dẫn  
**Mục đích:** Quản lý tiến độ tuần, tracking deliverables  
**Nội dung:**
- Chia nhỏ mỗi tháng (T1-T6) thành 4 tuần
- Tasks cụ thể cho từng tuần
- Deliverables rõ ràng
- Risks & mitigations
- Checklist tổng thể

**Khác biệt với đề cương:**
- Chi tiết hơn (tuần instead of tháng)
- Có Gantt chart
- Có risk analysis
- Có mapping với đề cương

---

### 3. Kế hoạch thực thi cho AI Agents (executable plan)
**File:** `ke_hoach_agent_executable.md`  
**Người đọc:** AI agents/assistants  
**Mục đích:** Hướng dẫn bước-by-bước để tự động hóa thực hiện  
**Nội dung:** Cho MỖI task:

```
📋 TASK X.Y: <Task name>

Input:
- Cụ thể files/data cần
- URLs/links đến resources
- Dependencies từ tasks trước

Actions:
- Step-by-step commands
- Code blocks có thể chạy
- Chi tiết kỹ thuật

Output:
- Đường dẫn file cụ thể
- Format mong đợi
- Ví dụ output

Acceptance Criteria:
- [ ] Checklist để verify hoàn thành
- [ ] Quality gates
- [ ] Performance expectations

Estimated Time: X hours
Risk: Low/Medium/High
```

**So với kế hoạch chi tiết:**
- Có URLs và links cụ thể (papers, repos, datasets)
- Có code mẫu chạy được
- Có acceptance criteria chi tiết
- Có error handling instructions
- Có verification steps

---

### 4. Changelog
**File:** `CHANGELOG_ke_hoach.md`  
**Mục đích:** Ghi lại lịch sử thay đổi  
**Nội dung:** Các điều chỉnh đã làm để kế hoạch khớp với đề cương

---

## 🔄 Mối quan hệ giữa các file

```
┌─────────────────────────────────────┐
│  S01.QuiTrinh.Mẫu 2_De cuong...    │
│  (ĐỀ CƯƠNG CHÍNH THỨC)              │
│  - T1-T6 overview                   │
│  - RQ1-RQ4 definitions              │
│  - Deliverables tháng               │
└───────────────┬─────────────────────┘
                │
                │ chi tiết hóa
                ▼
┌─────────────────────────────────────┐
│  ke_hoach_thuc_hien.md              │
│  (KẾ HOẠCH CHI TIẾT)                │
│  - Chia thành tuần                  │
│  - Tasks + outputs                  │
│  - Risks                            │
└───────────────┬─────────────────────┘
                │
                │ executable hóa
                ▼
┌─────────────────────────────────────┐
│  ke_hoach_agent_executable.md       │
│  (AGENT EXECUTABLE PLAN)            │
│  - Input/Output cụ thể              │
│  - Code blocks                      │
│  - Acceptance criteria              │
│  - URLs/links                       │
└─────────────────────────────────────┘
```

**Nguyên tắc:**
1. Đề cương là nguồn chân lý (source of truth)
2. Kế hoạch chi tiết PHẢI khớp 100% với đề cương
3. Kế hoạch agent-executable bổ sung chi tiết kỹ thuật, không thay đổi nội dung

---

## ✅ Checklist đồng bộ

Khi cập nhật, đảm bảo:

- [ ] **RQ1-RQ4** giống nhau trong cả 3 files
- [ ] **Deliverables T1-T6** khớp giữa đề cương và 2 kế hoạch
- [ ] **Nội dung ND1-ND3** được map chính xác
- [ ] **Thời gian 6 tháng** nhất quán
- [ ] **3 phương pháp + 2 datasets** không đổi

---

## 🎯 Cách sử dụng

### Khi đăng ký đề tài:
→ Nộp `S01.QuiTrinh.Mẫu 2_De cuong LVThS.md`

### Khi họp tiến độ với giáo viên:
→ Xem `ke_hoach_thuc_hien.md` (section tương ứng)

### Khi làm việc với AI assistant:
→ Cung cấp `ke_hoach_agent_executable.md` + task cụ thể

### Khi cần kiểm tra mapping:
→ Xem bảng MAPPING trong `ke_hoach_thuc_hien.md`

---

## 📊 Tiến độ thực hiện

**Tracking:** Dùng checklist ở cuối mỗi file

```bash
# Kiểm tra deliverables tháng hiện tại
grep "\[ \]" ke_hoach_thuc_hien.md | head -20

# Verify files tồn tại
ls -la literature/ data/ thesis/chapters/
```

---

## 🚨 Troubleshooting

### ❓ Kế hoạch chi tiết khác với đề cương?
→ Xem `CHANGELOG_ke_hoach.md` để hiểu lịch sử thay đổi  
→ Nếu phát hiện mâu thuẫn mới: cập nhật kế hoạch để khớp đề cương

### ❓ Agent không thực hiện được task?
→ Kiểm tra xem có đủ:
- Input files/data?
- URLs/links working?
- Acceptance criteria rõ ràng?
→ Nếu thiếu: bổ sung vào `ke_hoach_agent_executable.md`

### ❓ Task mất nhiều thời gian hơn dự kiến?
→ Document trong `experiments/time_tracking.md`  
→ Điều chỉnh estimated time trong kế hoạch  
→ Re-assess risks

---

## 📝 Quy trình cập nhật

1. **Thay đổi xuất phát từ đề cương (chính thức):**
   ```
   S01 (đề cương) → ke_hoach_thuc_hien.md → ke_hoach_agent_executable.md
   ```

2. **Thay đổi phát hiện trong thực hiện:**
   ```
   Reality → Update agent-executable → Reflect in kế hoạch chi tiết
   → Nếu cần: đề xuất sửa đề cương
   ```

3. **Luôn document trong CHANGELOG:**
   ```bash
   echo "## $(date): Updated Task X.Y" >> CHANGELOG_ke_hoach.md
   echo "- Reason: ..." >> CHANGELOG_ke_hoach.md
   echo "- Changes: ..." >> CHANGELOG_ke_hoach.md
   ```

---

## 📞 Contacts & Resources

- **Giáo viên hướng dẫn:** [Tên], [Email]
- **GitHub Repository:** [URL when available]
- **Overleaf (thesis):** [URL when created]
- **Google Drive (backup):** [URL]

---

**Lần cập nhật cuối:** 2026-11-17  
**Trạng thái:** Đề cương approved ✓ | Kế hoạch chi tiết ready ✓ | Agent-executable WIP (70% done - Month 1-2 complete)
