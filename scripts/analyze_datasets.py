#!/usr/bin/env python3
"""
Dataset Statistics Analysis
Analyze HDFS_v1 and BGL datasets comprehensively
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from collections import Counter

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def analyze_hdfs():
    """Analyze HDFS_v1 dataset"""
    print("=" * 60)
    print("📊 ANALYZING HDFS_v1 DATASET")
    print("=" * 60)
    
    # Load data
    base_path = Path('data/raw/hdfs_v1/preprocessed')
    
    # 1. Load labels
    labels = pd.read_csv(base_path / 'anomaly_label.csv')
    print(f"\n✓ Loaded labels: {len(labels):,} blocks")
    
    # 2. Load templates
    templates = pd.read_csv(base_path / 'HDFS.log_templates.csv')
    print(f"✓ Loaded templates: {len(templates)} unique templates")
    
    # 3. Load event occurrence matrix
    occurrences = pd.read_csv(base_path / 'Event_occurrence_matrix.csv')
    print(f"✓ Loaded event occurrences: {len(occurrences):,} blocks")
    
    # Statistics
    stats = {
        'dataset': 'HDFS_v1',
        'total_blocks': int(len(labels)),
        'unique_templates': int(len(templates)),
        'anomaly_count': int(labels['Label'].value_counts().get('Anomaly', 0)),
        'normal_count': int(labels['Label'].value_counts().get('Normal', 0)),
        'anomaly_rate': float(labels['Label'].value_counts().get('Anomaly', 0) / len(labels)),
        'imbalance_ratio': f"1:{int(labels['Label'].value_counts().get('Normal', 0) / labels['Label'].value_counts().get('Anomaly', 1))}"
    }
    
    # Sequence length statistics (from event counts)
    event_cols = [f'E{i}' for i in range(1, 30)]  # E1-E29
    occurrences['total_events'] = occurrences[event_cols].sum(axis=1)
    stats['sequence_length'] = {
        'mean': float(occurrences['total_events'].mean()),
        'median': float(occurrences['total_events'].median()),
        'min': int(occurrences['total_events'].min()),
        'max': int(occurrences['total_events'].max()),
        'std': float(occurrences['total_events'].std())
    }
    
    # Template frequency
    template_freq = {}
    for idx, row in templates.iterrows():
        event_id = row['EventId']
        # Sum occurrences across all blocks
        col_name = event_id
        if col_name in occurrences.columns:
            count = int(occurrences[col_name].sum())
        else:
            count = 0
        template_freq[event_id] = {
            'template': row['EventTemplate'],
            'occurrences': count
        }
    
    # Sort by frequency
    sorted_templates = sorted(template_freq.items(), key=lambda x: x[1]['occurrences'], reverse=True)
    stats['top_10_templates'] = {k: v for k, v in sorted_templates[:10]}
    
    print("\n" + "=" * 60)
    print("HDFS_v1 STATISTICS")
    print("=" * 60)
    print(f"Total blocks:        {stats['total_blocks']:,}")
    print(f"Unique templates:    {stats['unique_templates']}")
    print(f"Normal blocks:       {stats['normal_count']:,}")
    print(f"Anomaly blocks:      {stats['anomaly_count']:,}")
    print(f"Anomaly rate:        {stats['anomaly_rate']:.2%}")
    print(f"Imbalance ratio:     {stats['imbalance_ratio']}")
    print(f"\nSequence Length:")
    print(f"  Mean:   {stats['sequence_length']['mean']:.1f}")
    print(f"  Median: {stats['sequence_length']['median']:.0f}")
    print(f"  Min:    {stats['sequence_length']['min']}")
    print(f"  Max:    {stats['sequence_length']['max']}")
    print(f"  Std:    {stats['sequence_length']['std']:.1f}")
    print(f"\nTop 5 templates:")
    for i, (tid, info) in enumerate(list(stats['top_10_templates'].items())[:5], 1):
        print(f"  {i}. {tid}: {info['occurrences']:,} occurrences")
        print(f"     {info['template'][:70]}...")
    
    return stats, occurrences, labels, templates

def analyze_bgl():
    """Analyze BGL dataset"""
    print("\n" + "=" * 60)
    print("📊 ANALYZING BGL DATASET")
    print("=" * 60)
    
    # Load data
    parsed_file = Path('data/parsed/bgl_structured.jsonl')
    templates_file = Path('data/parsed/bgl_structured.jsonl.templates.json')
    
    print(f"\n✓ Loading {parsed_file.name}...")
    logs = []
    with open(parsed_file) as f:
        for i, line in enumerate(f):
            logs.append(json.loads(line))
            if (i + 1) % 500000 == 0:
                print(f"  Loaded {i+1:,} logs...")
    
    df = pd.DataFrame(logs)
    print(f"✓ Loaded {len(df):,} logs")
    
    # Load templates
    with open(templates_file) as f:
        templates = json.load(f)
    print(f"✓ Loaded {len(templates)} templates")
    
    # Statistics
    stats = {
        'dataset': 'BGL',
        'total_logs': int(len(df)),
        'unique_templates': int(df['EventId'].nunique()),
        'anomaly_count': int(df['Anomaly'].sum()),
        'normal_count': int((df['Anomaly'] == 0).sum()),
        'anomaly_rate': float(df['Anomaly'].mean()),
        'imbalance_ratio': f"1:{int((df['Anomaly'] == 0).sum() / max(df['Anomaly'].sum(), 1))}"
    }
    
    # Date range
    stats['date_range'] = {
        'start': str(df['Date'].min()),
        'end': str(df['Date'].max())
    }
    
    # Template distribution
    template_counts = df['EventId'].value_counts()
    stats['template_distribution'] = {
        'mean': float(template_counts.mean()),
        'median': float(template_counts.median()),
        'min': int(template_counts.min()),
        'max': int(template_counts.max()),
        'std': float(template_counts.std())
    }
    
    # Top templates
    top_templates = []
    for tid, count in template_counts.head(10).items():
        template_text = next((t['EventTemplate'] for t in templates if t['EventId'] == tid), 'Unknown')
        top_templates.append({
            'EventId': tid,
            'template': template_text,
            'occurrences': int(count)
        })
    stats['top_10_templates'] = top_templates
    
    # Anomaly distribution by level
    stats['anomaly_by_level'] = df.groupby('Level')['Anomaly'].agg(['sum', 'count', 'mean']).to_dict()
    
    print("\n" + "=" * 60)
    print("BGL STATISTICS")
    print("=" * 60)
    print(f"Total logs:          {stats['total_logs']:,}")
    print(f"Unique templates:    {stats['unique_templates']:,}")
    print(f"Normal logs:         {stats['normal_count']:,}")
    print(f"Anomaly logs:        {stats['anomaly_count']:,}")
    print(f"Anomaly rate:        {stats['anomaly_rate']:.2%}")
    print(f"Imbalance ratio:     {stats['imbalance_ratio']}")
    print(f"Date range:          {stats['date_range']['start']} to {stats['date_range']['end']}")
    print(f"\nTemplate Distribution:")
    print(f"  Mean:   {stats['template_distribution']['mean']:.0f}")
    print(f"  Median: {stats['template_distribution']['median']:.0f}")
    print(f"  Min:    {stats['template_distribution']['min']}")
    print(f"  Max:    {stats['template_distribution']['max']:,}")
    print(f"\nTop 5 templates:")
    for i, t in enumerate(stats['top_10_templates'][:5], 1):
        print(f"  {i}. {t['EventId']}: {t['occurrences']:,} occurrences")
        print(f"     {t['template'][:70]}...")
    
    return stats, df, templates

def create_visualizations(hdfs_stats, hdfs_occurrences, hdfs_labels, bgl_stats, bgl_df):
    """Create visualization plots"""
    print("\n" + "=" * 60)
    print("📈 CREATING VISUALIZATIONS")
    print("=" * 60)
    
    output_dir = Path('analysis/figures')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Anomaly rate comparison
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    datasets = ['HDFS_v1', 'BGL']
    anomaly_rates = [hdfs_stats['anomaly_rate'] * 100, bgl_stats['anomaly_rate'] * 100]
    colors = ['#2ecc71', '#e74c3c']
    
    bars = ax.bar(datasets, anomaly_rates, color=colors, alpha=0.7)
    ax.set_ylabel('Anomaly Rate (%)', fontsize=12)
    ax.set_title('Anomaly Rate Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(anomaly_rates) * 1.2)
    
    # Add value labels
    for bar, rate in zip(bars, anomaly_rates):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.2f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'anomaly_rate_comparison.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_dir / 'anomaly_rate_comparison.png'}")
    plt.close()
    
    # 2. HDFS sequence length distribution
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.hist(hdfs_occurrences['total_events'], bins=50, color='#3498db', alpha=0.7, edgecolor='black')
    ax.set_xlabel('Sequence Length (number of events)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('HDFS_v1: Sequence Length Distribution', fontsize=14, fontweight='bold')
    ax.axvline(hdfs_occurrences['total_events'].mean(), color='red', linestyle='--', 
               label=f'Mean: {hdfs_occurrences["total_events"].mean():.1f}')
    ax.axvline(hdfs_occurrences['total_events'].median(), color='green', linestyle='--',
               label=f'Median: {hdfs_occurrences["total_events"].median():.0f}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'hdfs_sequence_length.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_dir / 'hdfs_sequence_length.png'}")
    plt.close()
    
    # 3. Template diversity comparison
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    datasets = ['HDFS_v1', 'BGL']
    template_counts = [hdfs_stats['unique_templates'], bgl_stats['unique_templates']]
    colors = ['#9b59b6', '#f39c12']
    
    bars = ax.bar(datasets, template_counts, color=colors, alpha=0.7)
    ax.set_ylabel('Number of Unique Templates', fontsize=12)
    ax.set_title('Template Diversity Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(template_counts) * 1.2)
    
    for bar, count in zip(bars, template_counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{count:,}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'template_diversity.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_dir / 'template_diversity.png'}")
    plt.close()
    
    print(f"\n✓ All visualizations saved to {output_dir}/")

def save_results(hdfs_stats, bgl_stats):
    """Save combined statistics"""
    output_file = Path('analysis/dataset_statistics.json')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    combined_stats = {
        'hdfs_v1': hdfs_stats,
        'bgl': bgl_stats,
        'generated_at': '2026-11-26T16:20:00'
    }
    
    with open(output_file, 'w') as f:
        json.dump(combined_stats, f, indent=2)
    
    print(f"\n✓ Statistics saved to {output_file}")
    return output_file

def main():
    """Main analysis pipeline"""
    print("\n" + "=" * 70)
    print("🔬 DATASET COMPREHENSIVE ANALYSIS")
    print("=" * 70)
    
    try:
        # Analyze HDFS
        hdfs_stats, hdfs_occurrences, hdfs_labels, hdfs_templates = analyze_hdfs()
        
        # Analyze BGL
        bgl_stats, bgl_df, bgl_templates = analyze_bgl()
        
        # Create visualizations
        create_visualizations(hdfs_stats, hdfs_occurrences, hdfs_labels, bgl_stats, bgl_df)
        
        # Save results
        output_file = save_results(hdfs_stats, bgl_stats)
        
        print("\n" + "=" * 70)
        print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print(f"\nOutputs:")
        print(f"  - Statistics: {output_file}")
        print(f"  - Figures: analysis/figures/")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit(main())
