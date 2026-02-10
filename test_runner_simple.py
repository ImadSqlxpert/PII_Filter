#!/usr/bin/env python
"""
Generate test report by running a quick per-file analysis.
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime

def run_test_file(test_file):
    """Run a single test file and parse results."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=line"],
        capture_output=True,
        text=True,
        cwd="."
    )
    
    output = result.stdout + "\n" + result.stderr
    
    # Parse output for counts
    lines = output.split('\n')
    passed = 0
    failed = 0
    skipped = 0
    
    for line in reversed(lines):
        if ' passed' in line or ' failed' in line:
            import re
            if 'passed' in line:
                m = re.search(r'(\d+)\s+passed', line)
                if m:
                    passed = int(m.group(1))
            if 'failed' in line:
                m = re.search(r'(\d+)\s+failed', line)
                if m:
                    failed = int(m.group(1))
            if 'skipped' in line:
                m = re.search(r'(\d+)\s+skipped', line)
                if m:
                    skipped = int(m.group(1))
            break
    
    return {
        'file': test_file.name,
        'passed': passed,
        'failed': failed,
        'skipped': skipped,
        'total': passed + failed + skipped,
        'output': output
    }

def main():
    # Find all test files
    test_dir = Path("tests/unit")
    test_files = sorted(test_dir.glob("test_*.py"))
    
    if not test_files:
        print("No test files found in tests/unit/")
        return 1
    
    print(f"Found {len(test_files)} test files")
    print("=" * 80)
    print()
    
    # Run each test file
    results = []
    total_passed = 0
    total_failed = 0
    total_skipped = 0
    failed_tests = []
    
    for i, test_file in enumerate(test_files, 1):
        print(f"[{i}/{len(test_files)}] Running {test_file.name}...", end=" ", flush=True)
        result = run_test_file(test_file)
        results.append(result)
        
        total_passed += result['passed']
        total_failed += result['failed']
        total_skipped += result['skipped']
        
        status = "✓" if result['failed'] == 0 else "✗"
        print(f"{status} ({result['passed']} passed, {result['failed']} failed)")
        
        # Extract failed test names
        if result['failed'] > 0:
            lines = result['output'].split('\n')
            for line in lines:
                if 'FAILED' in line and '::' in line:
                    failed_tests.append((test_file.name, line.strip()))
    
    # Write detailed report
    report_path = Path("TEST_REPORT_SUMMARY.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Test Execution Report\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Summary
        total_tests = total_passed + total_failed + total_skipped
        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total Tests | {total_tests} |\n")
        f.write(f"| Passed | {total_passed} |\n")
        f.write(f"| Failed | {total_failed} |\n")
        f.write(f"| Skipped | {total_skipped} |\n")
        if total_tests > 0:
            f.write(f"| Pass Rate | {100*total_passed/total_tests:.1f}% |\n")
        f.write("\n")
        
        # Per-file results
        f.write("## Per-File Results\n\n")
        for result in results:
            f.write(f"### {result['file']}\n")
            f.write(f"- Passed: {result['passed']}\n")
            f.write(f"- Failed: {result['failed']}\n")
            f.write(f"- Skipped: {result['skipped']}\n")
            f.write("\n")
        
        # Failed tests section
        if failed_tests:
            f.write(f"## Failed Tests ({len(failed_tests)})\n\n")
            for test_file, test_line in failed_tests:
                f.write(f"- **{test_file}**: {test_line}\n")
            f.write("\n")
    
    # Print summary
    print()
    print("=" * 80)
    print(f"TEST EXECUTION COMPLETE")
    print("=" * 80)
    print(f"Total: {total_tests} tests")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Skipped: {total_skipped}")
    print(f"\nReport saved to: {report_path.absolute()}")
    print()
    
    return 0 if total_failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
