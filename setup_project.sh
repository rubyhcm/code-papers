#!/bin/bash

# Tạo cấu trúc thư mục cho luận văn
echo "🏗️  Tạo cấu trúc dự án..."

# Literature & Analysis
mkdir -p literature
mkdir -p methodology
mkdir -p analysis/figures

# Data
mkdir -p data/raw/{hdfs_v3,bgl}
mkdir -p data/parsed
mkdir -p data/splits

# Scripts
mkdir -p scripts
mkdir -p config

# Results
mkdir -p results/benchmark/{lightad,logformer,lograg}
mkdir -p models/pretrained

# Thesis
mkdir -p thesis/{chapters,tables,figures,appendices}
mkdir -p templates

# Experiments & Reviews
mkdir -p experiments
mkdir -p reviews

# Reproducibility
mkdir -p reproducibility_package
mkdir -p defense_slides
mkdir -p defense_preparation

# Repos (nếu chưa có)
mkdir -p repos

echo "✅ Cấu trúc thư mục đã được tạo"
tree -L 2 -d .
