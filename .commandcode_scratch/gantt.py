import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# ---- Dữ liệu lịch (đơn vị: tháng, 0 = đầu T1, 6 = cuối T6) ----
# main: thực hiện chính; prep: thực hiện phụ / chuẩn bị
tasks = [
    {
        "label": "Nội dung 1\nTổng quan, tái lập & mở rộng pipeline",
        "color": "#1f77b4",
        "main":  [(0.0, 3.0)],
        "prep":  [],
    },
    {
        "label": "Nội dung 2\nBenchmark & phân tích RQ1–RQ5",
        "color": "#2ca02c",
        "main":  [(3.0, 2.0)],
        "prep":  [(2.0, 1.0)],
    },
    {
        "label": "Nội dung 3\nPhân tích lỗi & khuyến nghị",
        "color": "#ff7f0e",
        "main":  [(4.0, 2.0)],
        "prep":  [],
    },
    {
        "label": "Viết luận văn",
        "color": "#9467bd",
        "main":  [(5.0, 1.0)],
        "prep":  [(0.0, 1.0), (2.0, 1.0), (4.0, 1.0)],
    },
]

fig, ax = plt.subplots(figsize=(11.5, 5.4), dpi=200)
fig.patch.set_facecolor("white")

bar_height = 0.52
gap = 0.10

for i, t in enumerate(tasks):
    y = i
    color = t["color"]
    # thực hiện chính
    for start, dur in t["main"]:
        ax.barh(y, dur, left=start, height=bar_height,
                color=color, edgecolor="white", linewidth=0.6, zorder=3)
    # thực hiện phụ / chuẩn bị
    for start, dur in t["prep"]:
        ax.barh(y, dur, left=start, height=bar_height,
                color=color, alpha=0.32, hatch="///",
                edgecolor=color, linewidth=0.5, zorder=3)

# nhãn thời gian + trục
ax.set_xlim(0, 6)
ax.set_ylim(-0.55, len(tasks) - 0.45)
ax.invert_yaxis()

month_ticks = [0.5 + m for m in range(6)]
month_labels = [f"T{m+1}\nTháng {m+1}" for m in range(6)]
ax.set_xticks(month_ticks)
ax.set_xticklabels(month_labels, fontsize=10, color="#333333")
ax.tick_params(axis="x", length=0)
ax.xaxis.set_ticks_position("none")

# đường chia tháng
for m in range(7):
    ax.axvline(m, color="#cccccc", linewidth=0.8, zorder=1)

ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([t["label"] for t in tasks], fontsize=10.5, color="#1a1a1a",
                   va="center")
ax.tick_params(axis="y", length=0)
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

# mốc bảo vệ
ax.axvline(6, color="#d62728", linewidth=1.2, zorder=4)
ax.text(6.0, -0.02, "Bảo vệ", rotation=90, va="bottom", ha="center",
        fontsize=9, color="#d62728", fontweight="bold")

# chú giải
legend_elements = [
    Patch(facecolor="#555555", label="Thực hiện chính"),
    Patch(facecolor="#bbbbbb", hatch="///", edgecolor="#777777",
          label="Thực hiện phụ / chuẩn bị"),
    Line2D([0], [0], color="#d62728", linewidth=1.2, label="Mốc bảo vệ"),
]
ax.legend(handles=legend_elements, loc="lower center",
          bbox_to_anchor=(0.5, -0.26), ncol=3, frameon=False, fontsize=9.5)

ax.set_title("Kế hoạch thực hiện đề tài (6 tháng)", fontsize=14,
             fontweight="bold", color="#111111", pad=18)
ax.set_xlabel("", fontsize=1)

plt.tight_layout()
out = "/Users/ruby/dev/code-papers/ke_hoach_gantt.png"
plt.savefig(out, bbox_inches="tight", facecolor="white", dpi=200)
print("SAVED:", out)
