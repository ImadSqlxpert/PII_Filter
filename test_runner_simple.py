#!/usr/bin/env python
"""
Reliable test runner:
- Runs each test file with pytest --junitxml
- Parses structured results from XML (not fragile stdout scraping)
- Extracts ORIGINAL / EXPECTED / ACTUAL even if the test does not print them
- Writes a clear Markdown debug report
"""

from __future__ import annotations

import subprocess
import sys
import re
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional


# =============================================================================
# XML PARSER — extracts structured pass/fail data
# =============================================================================
def parse_junit(xml_path: Path) -> Dict:
    tree = ET.parse(str(xml_path))
    root = tree.getroot()

    testcases = root.findall(".//testcase")

    passed = failed = skipped = 0
    failures = []

    for tc in testcases:
        classname = tc.get("classname", "") or ""
        name      = tc.get("name", "") or ""
        file_attr = tc.get("file", "") or ""

        nodeid = f"{file_attr}::{classname.split('.')[-1]}::{name}" if classname else f"{file_attr}::{name}"

        if tc.find("failure") is not None:
            failed += 1
            fail = tc.find("failure")
            message = (fail.get("message") or "").strip()
            details = (fail.text or "").strip()

            failures.append({
                "node": nodeid,
                "message": message,
                "details": details,
            })

        elif tc.find("skipped") is not None:
            skipped += 1
        else:
            passed += 1

    return {
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "total": passed + failed + skipped,
        "failures": failures,
    }


# =============================================================================
# ORIGINAL / EXPECTED / ACTUAL extraction
# =============================================================================

# Explicit markers (rare in your tests but supported)
PAT_ORIG = [r"ORIGINAL:\s*(.*)"]
PAT_EXP  = [r"EXPECTED:\s*(.*)"]
PAT_ACT  = [r"ACTUAL:\s*(.*)"]


def first_match(patterns: List[str], text: str) -> Optional[str]:
    for p in patterns:
        m = re.search(p, text, flags=re.MULTILINE)
        if m:
            return m.group(1).strip()
    return None


def parse_assert_in(text: str):
    """
    Extract from:
        assert '<API_KEY>' in 'google_api_key=ABC...'
    """
    m = re.search(r"assert\s+(['\"].+?['\"])\s+in\s+(['\"].+?['\"])", text)
    if m:
        expected = m.group(1).strip("'\"")
        actual   = m.group(2).strip("'\"")
        original = actual
        return original, expected, actual
    return None


def parse_assert_eq(text: str):
    """
    Extract from:
        assert 'abc' == 'xyz'
    """
    m = re.search(r"assert\s+(['\"].+?['\"])\s*==\s*(['\"].+?['\"])", text)
    if m:
        left  = m.group(1).strip("'\"")
        right = m.group(2).strip("'\"")
        # left = actual, right = expected
        return left, right, left
    return None


def parse_diff(text: str):
    """For pytest auto-diff output: - expected / + actual"""
    exp = "\n".join(re.findall(r"(?m)^\- (.*)", text)) or None
    act = "\n".join(re.findall(r"(?m)^\+ (.*)", text)) or None
    if exp or act:
        return None, exp, act
    return None


def extract_triplet(text: str):
    """
    BEST-EFFORT extraction of:
        original, expected, actual
    """
    # 1) Explicit markers
    o = first_match(PAT_ORIG, text)
    e = first_match(PAT_EXP,  text)
    a = first_match(PAT_ACT,  text)
    if o or e or a:
        return o, e, a

    # 2) "assert <X> in <Y>"
    parsed = parse_assert_in(text)
    if parsed:
        return parsed

    # 3) "assert left == right"
    parsed = parse_assert_eq(text)
    if parsed:
        return parsed

    # 4) diff block
    parsed = parse_diff(text)
    if parsed:
        return parsed

    # 5) Nothing worked
    return None, None, None


# =============================================================================
# RUN SINGLE TEST FILE
# =============================================================================
def run_test_file(test_file: Path, xml_dir: Path) -> Dict:
    xml_path = xml_dir / f"{test_file.stem}.xml"

    cmd = [
        sys.executable, "-m", "pytest",
        str(test_file),
        "-q", "--tb=long",
        "-o", "junit_family=xunit2",
        f"--junitxml={xml_path}",
        "--disable-warnings",
    ]

    subprocess.run(cmd, capture_output=True, text=True)

    if not xml_path.exists():
        # safety fallback
        return {
            "file": test_file.name,
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "total": 0,
            "failures": [],
        }

    parsed = parse_junit(xml_path)

    enriched = []
    for f in parsed["failures"]:
        full = f["details"] or f["message"] or ""
        o, e, a = extract_triplet(full)

        enriched.append({
            "node": f["node"],
            "original": o,
            "expected": e,
            "actual": a,
            "full_block": full,
        })

    parsed["failures"] = enriched
    parsed["file"] = test_file.name
    return parsed


# =============================================================================
# WRITE MARKDOWN REPORT
# =============================================================================
def write_report(path: Path, results: List[Dict]):
    total_passed = sum(r["passed"] for r in results)
    total_failed = sum(r["failed"] for r in results)
    total_skipped = sum(r["skipped"] for r in results)
    total_tests = sum(r["total"] for r in results)

    with path.open("w", encoding="utf-8") as out:
        out.write("# Test Execution Report\n\n")
        out.write(f"Generated: **{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**\n\n")

        # Summary
        out.write("## Summary\n\n")
        out.write("| Metric | Count |\n|--------|-------|\n")
        out.write(f"| Total Tests | {total_tests} |\n")
        out.write(f"| Passed | {total_passed} |\n")
        out.write(f"| Failed | {total_failed} |\n")
        out.write(f"| Skipped | {total_skipped} |\n")
        if total_tests:
            out.write(f"| Pass Rate | {total_passed / total_tests * 100:.1f}% |\n")
        out.write("\n")

        # Per-file
        out.write("## Per‑File Results\n\n")
        for r in results:
            out.write(f"### {r['file']}\n")
            out.write(f"- Passed: {r['passed']}\n")
            out.write(f"- Failed: {r['failed']}\n")
            out.write(f"- Skipped: {r['skipped']}\n\n")

        # Failures
        out.write("## Failure Details\n\n")
        for r in results:
            if not r["failures"]:
                continue

            out.write(f"### ❌ {r['file']}\n\n")

            for f in r["failures"]:
                out.write(f"#### {f['node']}\n\n")

                out.write("**Original:**\n```\n" + (f["original"] or "(not found)") + "\n```\n\n")
                out.write("**Expected:**\n```\n" + (f["expected"] or "(not found)") + "\n```\n\n")
                out.write("**Actual:**\n```\n" + (f["actual"] or "(not found)") + "\n```\n\n")

                out.write("<details><summary>Full Failure Block</summary>\n\n")
                out.write("```\n" + (f["full_block"] or "") + "\n```\n")
                out.write("</details>\n\n")


# =============================================================================
# MAIN
# =============================================================================
def main() -> int:
    test_dir = Path("tests/unit")
    test_files = sorted(test_dir.glob("test_*.py"))

    if not test_files:
        print("No test files found in tests/unit/")
        return 1

    xml_dir = Path(".pytest_artifacts/junitxml")
    xml_dir.mkdir(parents=True, exist_ok=True)

    print(f"Found {len(test_files)} test files\n" + "=" * 80)

    results = []
    for i, tf in enumerate(test_files, 1):
        print(f"[{i}/{len(test_files)}] Running {tf.name}...", end=" ", flush=True)
        res = run_test_file(tf, xml_dir)
        results.append(res)
        print(f"✓ {res['passed']} | ✗ {res['failed']} | ⊝ {res['skipped']}")

    report = Path("TEST_REPORT_SUMMARY.md")
    write_report(report, results)

    print("\n" + "=" * 80)
    print("Test execution complete.")
    print("=" * 80)
    print(f"Report saved to: {report.resolve()}\n")

    # exit code
    return 0 if sum(r["failed"] for r in results) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())