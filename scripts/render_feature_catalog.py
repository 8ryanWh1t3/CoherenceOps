#!/usr/bin/env python3
import json
from pathlib import Path

SRC = Path("coherence/telemetry/feature_catalog.json")
OUT = Path("docs/FEATURE_CATALOG.md")


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    lines = []
    lines.append("# CoherenceOps Feature Catalog")
    lines.append("")
    lines.append("Machine source of truth: `coherence/telemetry/feature_catalog.json`")
    lines.append("")

    lines.append("## Categories")
    lines.append("")
    for c in data.get("categories", []):
        lines.append(f"### {c.get('name','(unnamed)')}")
        lines.append(f"{c.get('summary','')}".strip())
        lines.append("")
        for f in c.get("features", []):
            lines.append(f"- **{f.get('name','(unnamed)')}** (`{f.get('id','')}`)")
            if f.get("artifacts"):
                lines.append(f"  - Artifacts: {', '.join(f['artifacts'])}")
            if f.get("enforcement"):
                lines.append(f"  - Enforcement: {', '.join(f['enforcement'])}")
            if f.get("lens"):
                lx = f["lens"] if isinstance(f["lens"], list) else [str(f["lens"])]
                lines.append(f"  - Lenses: {', '.join(lx)}")
        lines.append("")

    lines.append("## Outer-Edge Boundaries")
    lines.append("")
    for b in data.get("outer_edge_boundaries", []):
        lines.append(f"- {b}")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("PASS: rendered docs/FEATURE_CATALOG.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
