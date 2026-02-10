#!/usr/bin/env python
"""
Run all unit tests in tests/unit/ directory.
"""
import subprocess
import sys

def main():
    """Run all tests and show output."""
    print("=" * 80)
    print("Running ALL Unit Tests from tests/unit/...")
    print("=" * 80)
    print()
    
    # Run tests with pytest
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/unit/", "-v", "--tb=short"],
        cwd="."
    )
    
    print()
    print("=" * 80)
    print(f"Tests completed with exit code: {result.returncode}")
    print("=" * 80)
    
    sys.exit(result.returncode)

if __name__ == '__main__':
    main()
