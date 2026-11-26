#!/bin/bash
# Script để update tất cả references từ HDFS_v3 sang HDFS_v1

echo "🔄 Updating HDFS_v3 → HDFS_v1 in all documents..."

# List of files to update
files=(
    "literature/01_core_papers_summary.md"
    "literature/02_literature_review_30plus.md"
    "literature/03_log_data_characteristics.md"
    "methodology/04_empirical_standards_checklist.md"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "  Updating: $file"
        # Replace HDFS_v3 with HDFS_v1
        sed -i.bak 's/HDFS_v3/HDFS_v1/g' "$file"
        sed -i.bak 's/hdfs_v3/hdfs_v1/g' "$file"
        rm -f "${file}.bak"
    fi
done

echo "✅ Update completed!"
echo ""
echo "📊 Summary of changes:"
grep -r "HDFS_v1" literature/ methodology/ 2>/dev/null | wc -l | xargs echo "  Total HDFS_v1 references:"
