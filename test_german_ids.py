#!/usr/bin/env python3
"""Test runner for German e-gov ID tests."""
import subprocess
import sys
import os

os.chdir(r"C:\Users\imadi\Desktop\projects\PII_Filter")
result = subprocess.run(
    [".venv\\Scripts\\python.exe", "-m", "pytest", "-q", "tests/unit/test_regex_patterns.py::test_german_gov_id_regex_positive", "-v"],
    capture_output=True,
    text=True
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
sys.exit(result.returncode)
