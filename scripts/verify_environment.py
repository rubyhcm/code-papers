#!/usr/bin/env python3
"""
Environment verification script for LogAD benchmark.
Run: python scripts/verify_environment.py
"""
import sys
import os


def check(label, condition, info=""):
    status = "✓" if condition else "✗"
    print(f"  {status} {label}: {info}")
    return condition


def verify():
    print("=== Environment Verification ===\n")
    results = []

    # Python
    v = sys.version_info
    results.append(check("Python", v.major == 3, sys.version.split()[0]))

    # PyTorch
    try:
        import torch
        results.append(check("PyTorch", True, torch.__version__))
        results.append(check("CUDA available", torch.cuda.is_available(),
                             f"{torch.cuda.device_count()} device(s)" if torch.cuda.is_available() else "CPU only (OK on macOS)"))
    except ImportError:
        results.append(check("PyTorch", False, "not installed"))

    # Transformers
    try:
        import transformers
        results.append(check("Transformers", True, transformers.__version__))
    except ImportError:
        results.append(check("Transformers", False, "not installed"))

    # Scikit-learn
    try:
        import sklearn
        results.append(check("Scikit-learn", True, sklearn.__version__))
    except ImportError:
        results.append(check("Scikit-learn", False, "not installed"))

    # Drain3
    try:
        import drain3
        version = getattr(drain3, "__version__", "installed")
        results.append(check("Drain3", True, version))
    except ImportError:
        results.append(check("Drain3", False, "not installed"))

    # Pandas / Numpy
    try:
        import pandas as pd
        results.append(check("Pandas", True, pd.__version__))
    except ImportError:
        results.append(check("Pandas", False, "not installed"))

    try:
        import numpy as np
        results.append(check("NumPy", True, np.__version__))
    except ImportError:
        results.append(check("NumPy", False, "not installed"))

    # Repos (in project root)
    print()
    for repo in ["LightAD", "LogFormer", "LogRAG"]:
        exists = os.path.isdir(repo)
        results.append(check(f"Repo {repo}", exists, repo if exists else "NOT FOUND"))

    # Data directories
    print()
    for d in ["data/raw", "data/parsed", "analysis", "thesis/chapters"]:
        results.append(check(f"Dir {d}", os.path.isdir(d), d))

    # Summary
    passed = sum(results)
    total = len(results)
    print(f"\n{'='*34}")
    print(f"  {passed}/{total} checks passed", "✅" if passed == total else "⚠️")
    if passed < total:
        print("  See docs/environment_setup.md for help.")
    return passed == total


if __name__ == "__main__":
    success = verify()
    sys.exit(0 if success else 1)
