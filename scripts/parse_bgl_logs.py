#!/usr/bin/env python3
"""
BGL Log Parsing with Drain3
Parse BGL logs into structured format for anomaly detection
"""

import re
import json
import pandas as pd
from pathlib import Path
from collections import Counter
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

# BGL log format regex
# Format: - <Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>
BGL_REGEX = r'^- (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (.+)$'

def parse_bgl_line(line):
    """Parse a single BGL log line"""
    match = re.match(BGL_REGEX, line.strip())
    if not match:
        return None
    
    return {
        'Label': match.group(1),
        'Timestamp': match.group(2),
        'Date': match.group(3),
        'Node': match.group(4),
        'Time': match.group(5),
        'NodeRepeat': match.group(6),
        'Type': match.group(7),
        'Component': match.group(8),
        'Level': match.group(9),
        'Content': match.group(9)  # Full content for Drain
    }

def extract_label(level):
    """Extract binary label from log level"""
    # Anomaly if level is FATAL, ERROR, SEVERE, FAILURE, etc.
    anomaly_levels = ['FATAL', 'ERROR', 'SEVERE', 'FAILURE', 'CRITICAL']
    return 1 if any(lvl in level.upper() for lvl in anomaly_levels) else 0

def parse_bgl_logs(input_file, output_dir):
    """Parse BGL logs with Drain"""
    print(f"🔍 Parsing BGL logs from: {input_file}")
    
    # Configure Drain
    config = TemplateMinerConfig()
    config.load({
        'DRAIN': {
            'sim_th': 0.4,  # Lower threshold for BGL (more diverse)
            'depth': 4,
            'max_children': 100
        }
    })
    
    template_miner = TemplateMiner(config=config)
    
    # Parse logs
    parsed_logs = []
    total_lines = 0
    parse_errors = 0
    
    print("📖 Reading and parsing...")
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            total_lines += 1
            
            # Progress indicator
            if line_num % 100000 == 0:
                print(f"  Processed {line_num:,} lines...")
            
            # Parse structured fields
            parsed = parse_bgl_line(line)
            if parsed is None:
                parse_errors += 1
                continue
            
            # Drain parsing on Content
            result = template_miner.add_log_message(parsed['Content'])
            
            # Store parsed log
            parsed_logs.append({
                'LineId': line_num,
                'Label': parsed['Label'],
                'Timestamp': parsed['Timestamp'],
                'Date': parsed['Date'],
                'Node': parsed['Node'],
                'Time': parsed['Time'],
                'Type': parsed['Type'],
                'Component': parsed['Component'],
                'Level': parsed['Level'],
                'Content': parsed['Content'],
                'EventTemplate': result['template_mined'],
                'EventId': f"E{result['cluster_id']}",
                'ParameterList': result.get('matched', []),
                'Anomaly': extract_label(parsed['Level'])
            })
    
    print(f"✅ Parsed {total_lines:,} lines ({parse_errors:,} errors)")
    
    # Save parsed logs
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Save structured logs (JSONL)
    parsed_file = output_dir / 'bgl_structured.jsonl'
    print(f"💾 Saving to {parsed_file}...")
    with open(parsed_file, 'w') as f:
        for log in parsed_logs:
            f.write(json.dumps(log) + '\n')
    
    # 2. Save templates
    templates = []
    for cluster in template_miner.drain.clusters:
        templates.append({
            'EventId': f"E{cluster.cluster_id}",
            'EventTemplate': ' '.join(cluster.log_template_tokens),
            'Occurrences': cluster.size
        })
    
    templates_file = output_dir / 'bgl_structured.jsonl.templates.json'
    print(f"💾 Saving templates to {templates_file}...")
    with open(templates_file, 'w') as f:
        json.dump(templates, f, indent=2)
    
    # 3. Generate statistics
    df = pd.DataFrame(parsed_logs)
    
    stats = {
        'total_logs': int(len(df)),
        'unique_templates': int(df['EventId'].nunique()),
        'anomaly_count': int(df['Anomaly'].sum()),
        'anomaly_rate': float(df['Anomaly'].mean()),
        'parse_errors': int(parse_errors),
        'date_range': {
            'start': str(df['Date'].min()),
            'end': str(df['Date'].max())
        },
        'top_10_templates': {k: int(v) for k, v in df['EventId'].value_counts().head(10).items()},
        'anomaly_by_level': {k: int(v) for k, v in df.groupby('Level')['Anomaly'].sum().items()}
    }
    
    stats_file = output_dir / 'bgl_statistics.json'
    print(f"💾 Saving statistics to {stats_file}...")
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("📊 BGL PARSING SUMMARY")
    print("="*60)
    print(f"Total logs:          {stats['total_logs']:,}")
    print(f"Unique templates:    {stats['unique_templates']:,}")
    print(f"Anomalies:           {stats['anomaly_count']:,} ({stats['anomaly_rate']:.2%})")
    print(f"Parse errors:        {stats['parse_errors']:,}")
    print(f"Date range:          {stats['date_range']['start']} to {stats['date_range']['end']}")
    print("\nTop 5 templates:")
    for i, (template_id, count) in enumerate(list(stats['top_10_templates'].items())[:5], 1):
        template_text = next(t['EventTemplate'] for t in templates if t['EventId'] == template_id)
        print(f"  {i}. {template_id}: {count:,} occurrences")
        print(f"     {template_text[:80]}...")
    print("="*60)
    
    return stats

def main():
    """Main function"""
    import sys
    
    # Paths
    input_file = 'data/raw/bgl/BGL.log'
    output_dir = 'data/parsed'
    
    # Check input exists
    if not Path(input_file).exists():
        print(f"❌ Error: Input file not found: {input_file}")
        sys.exit(1)
    
    # Parse
    try:
        stats = parse_bgl_logs(input_file, output_dir)
        print("\n✅ BGL parsing completed successfully!")
        return 0
    except Exception as e:
        print(f"\n❌ Error during parsing: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit(main())
