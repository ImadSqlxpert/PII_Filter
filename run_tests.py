#!/usr/bin/env python
"""Run tests and report summary."""
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "pytest", "tests/unit/test_entity_coverage.py", "-q", "--tb=no"],
    cwd=".",
    capture_output=True,
    text=True
)
print(result.stdout)
print(result.stderr)
sys.exit(result.returncode)
