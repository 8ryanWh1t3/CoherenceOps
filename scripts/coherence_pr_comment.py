#!/usr/bin/env python3
"""
Produces release_kpis/COHERENCE_PR_COMMENT.md (repo-local artifact).
This is NOT a GitHub API commenter; it generates the payload for PR automation.
"""
import json
from pathlib import Path
from datetime import datetime, timezone

OUTDIR = Path("release_kpis")
OUTDIR.mkdir(parents=True, exist_ok=True)


def safe_read(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="replace")


def main():
    version = safe_read(Path("VERSION")).strip() or "0.0.0"

    signals = {
        "DLR_present": Path("artifacts/DLR.md").exists() or Path("DLR.md").exists(),
        "RS_present": Path("artifacts/RS.md").exists() or Path("RS.md").exists(),
        "DS_present": Path("artifacts/DS.md").exists() or Path("DS.md").exists(),
        "MG_present": any(Path(".").glob("**/MG.*")),
        "FeatureCatalog_present": Path("docs/FEATURE_CATALOG.md").exists(),
        "OuterEdge_present": Path("docs/OUTER_EDGE_BOUNDARIES.md").exists(),
    }

    coherence_score = None
    score_paths = [
        Path("coherence/telemetry/coherence_score.json"),
        Path("release_kpis/coherence_score.json"),
        Path("coherence_score.json"),
    ]
    for sp in score_paths:
        if sp.exists():
            try:
                coherence_score = json.loads(sp.read_text(encoding="utf-8")).get("coherence_index")
                break
            except Exception:
                pass

    lines = []
    lines.append(f"# Coherence Gate Summary - v{version}")
    lines.append("")
    lines.append(f"- Generated: {datetime.now(timezone.utc).isoformat()}")
    if coherence_score is not None:
        lines.append(f"- Coherence Index: **{coherence_score} / 100**")
    lines.append("")
    lines.append("## Gate Signals")
    for k, v in signals.items():
        lines.append(f"- {k}: {'OK' if bool(v) else 'MISSING'}")
    lines.append("")
    lines.append("## Notes")
    lines.append("- Governance is pre-merge: artifacts + drift->patch + memory.")
    lines.append("- Observability is not governance; enforcement is.")
    lines.append("")

    (OUTDIR / "COHERENCE_PR_COMMENT.md").write_text("\n".join(lines), encoding="utf-8")
    print("PASS: wrote release_kpis/COHERENCE_PR_COMMENT.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
