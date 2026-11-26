#!/usr/bin/env python3
"""
Environment Verification Script
Checks all dependencies and system requirements for thesis experiments

Usage: python scripts/verify_environment.py
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check Python version >= 3.8"""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("✗ ERROR: Python 3.8+ required")
        return False
    return True

def check_library(name, min_version=None):
    """Check if library is installed with optional version check"""
    try:
        module = __import__(name)
        version = getattr(module, '__version__', 'unknown')
        status = "✓"
        
        if min_version and version != 'unknown':
            if version < min_version:
                status = "⚠️"
                
        print(f"{status} {name}: {version}")
        return True
    except ImportError:
        print(f"✗ {name}: NOT INSTALLED")
        return False

def check_cuda():
    """Check CUDA availability"""
    try:
        import torch
        cuda_available = torch.cuda.is_available()
        
        if cuda_available:
            device_count = torch.cuda.device_count()
            device_name = torch.cuda.get_device_name(0)
            cuda_version = torch.version.cuda
            print(f"✓ CUDA: Available")
            print(f"  - Version: {cuda_version}")
            print(f"  - Devices: {device_count}")
            print(f"  - GPU 0: {device_name}")
            
            # Check VRAM
            props = torch.cuda.get_device_properties(0)
            vram_gb = props.total_memory / (1024**3)
            print(f"  - VRAM: {vram_gb:.1f} GB")
            
            if vram_gb < 16:
                print("  ⚠️ WARNING: Less than 16GB VRAM, may struggle with LogFormer")
        else:
            print("⚠️ CUDA: Not available (CPU mode only)")
            print("  - LogFormer and LogRAG may be slow")
            
        return cuda_available
    except ImportError:
        print("✗ PyTorch not installed")
        return False

def check_repos():
    """Check if 3 repos are cloned"""
    repos = ['LightAD', 'LogFormer', 'LogRAG']
    all_present = True
    
    print("\n=== Repository Check ===")
    for repo in repos:
        path = Path(repo)
        if path.exists() and path.is_dir():
            print(f"✓ {repo}/: Present")
        else:
            print(f"✗ {repo}/: Missing")
            all_present = False
            
    return all_present

def check_data():
    """Check if datasets are present"""
    print("\n=== Dataset Check ===")
    all_present = True
    
    # HDFS
    hdfs_path = Path('data/raw/hdfs_v1')
    if hdfs_path.exists():
        print(f"✓ HDFS_v1: Present")
    else:
        print(f"✗ HDFS_v1: Missing")
        all_present = False
        
    # BGL
    bgl_path = Path('data/raw/bgl')
    if bgl_path.exists():
        print(f"✓ BGL: Present")
    else:
        print(f"✗ BGL: Missing")
        all_present = False
        
    # Parsed data
    parsed_hdfs = Path('data/parsed/hdfs_structured.jsonl')
    parsed_bgl = Path('data/parsed/bgl_structured.jsonl')
    
    if parsed_hdfs.exists():
        size = parsed_hdfs.stat().st_size / (1024**2)
        print(f"✓ HDFS parsed: {size:.1f} MB")
    else:
        print(f"⚠️ HDFS parsed: Not yet")
        
    if parsed_bgl.exists():
        size = parsed_bgl.stat().st_size / (1024**3)
        print(f"✓ BGL parsed: {size:.1f} GB")
    else:
        print(f"⚠️ BGL parsed: Not yet")
        
    return all_present

def check_disk_space():
    """Check available disk space"""
    import shutil
    
    print("\n=== Disk Space Check ===")
    total, used, free = shutil.disk_usage('.')
    
    free_gb = free / (1024**3)
    print(f"✓ Free space: {free_gb:.1f} GB")
    
    if free_gb < 100:
        print("⚠️ WARNING: Less than 100GB free, may run out during experiments")
        return False
    return True

def check_memory():
    """Check system RAM"""
    try:
        import psutil
        
        print("\n=== Memory Check ===")
        mem = psutil.virtual_memory()
        total_gb = mem.total / (1024**3)
        available_gb = mem.available / (1024**3)
        
        print(f"✓ Total RAM: {total_gb:.1f} GB")
        print(f"✓ Available RAM: {available_gb:.1f} GB")
        
        if total_gb < 32:
            print("⚠️ WARNING: Less than 32GB RAM, may struggle with large datasets")
            return False
        return True
    except ImportError:
        print("⚠️ psutil not installed, skipping memory check")
        return True

def main():
    """Run all checks"""
    print("=" * 60)
    print("ENVIRONMENT VERIFICATION - Log Anomaly Detection Thesis")
    print("=" * 60)
    
    checks = []
    
    # Python version
    print("\n=== Python Version ===")
    checks.append(('Python 3.8+', check_python_version()))
    
    # Core libraries
    print("\n=== Core Libraries ===")
    checks.append(('PyTorch', check_library('torch', '1.13.0')))
    checks.append(('Transformers', check_library('transformers', '4.30.0')))
    checks.append(('Scikit-learn', check_library('sklearn', '1.3.0')))
    
    # Data processing
    print("\n=== Data Processing ===")
    checks.append(('Pandas', check_library('pandas')))
    checks.append(('NumPy', check_library('numpy')))
    checks.append(('Drain3', check_library('drain3')))
    
    # Visualization
    print("\n=== Visualization ===")
    checks.append(('Matplotlib', check_library('matplotlib')))
    checks.append(('Seaborn', check_library('seaborn')))
    
    # System
    print("\n=== System ===")
    checks.append(('CUDA', check_cuda()))
    checks.append(('Memory', check_memory()))
    checks.append(('Disk Space', check_disk_space()))
    
    # Repos & Data
    checks.append(('Repositories', check_repos()))
    checks.append(('Datasets', check_data()))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in checks if result)
    total = len(checks)
    
    print(f"\nPassed: {passed}/{total} checks")
    
    if passed == total:
        print("\n✓ All checks passed! Ready for experiments.")
        return 0
    else:
        print(f"\n⚠️ {total - passed} checks failed or have warnings.")
        print("Please install missing dependencies or fix issues.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
