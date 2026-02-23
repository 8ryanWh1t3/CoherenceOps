#!/usr/bin/env python3
"""
Single source of truth: VERSION file.
Updates common docs/workflows strings best-effort.
"""
from pathlib import Path
import re

VERSION = Path("VERSION").read_text(encoding="utf-8").strip()

TARGETS = [
    Path("README.md"),
    Path("docs/README.md"),
    Path(".github/workflows/ci.yml"),
    Path(".github/workflows/coherence.yml"),
    Path(".github/workflows/coherence_gate.yml"),
    Path(".github/workflows/ci-test.yml"),
    Path(".github/workflows/coherence-gates.yml"),
    Path(".github/workflows/coherence-score.yml"),
    Path(".github/workflows/coherence-weekly-rollup.yml"),
    Path(".github/workflows/drift-auto-detect.yml"),
    Path(".github/workflows/release.yml"),
]


def patch_file(p: Path):
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8", errors="replace")

    # Replace patterns like v0.4.0 / v0.4.2 etc.
    t2 = re.sub(r"v\d+\.\d+\.\d+", f"v{VERSION}", t)

    # Also allow bare 0.4.2
    t2 = re.sub(r"\b\d+\.\d+\.\d+\b", VERSION, t2)

    if t2 != t:
        p.write_text(t2, encoding="utf-8")


def main():
    for p in TARGETS:
        patch_file(p)
    print(f"PASS: synced version references to v{VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
