# Telemetry

Coherence health metrics and scoring.

## Files

| File | Purpose |
|------|---------|
| [coherence_score.json](coherence_score.json) | Current coherence score snapshot |
| [metrics_schema.md](metrics_schema.md) | Schema definition for the score object |

## How Scoring Works

The Coherence Score (0-100) is calculated from four inputs:

1. **DLR Coverage** (25 pts) — % of major PRs with a DLR
2. **Assumption Currency** (25 pts) — % of assumptions not expired
3. **Drift Health** (25 pts) — inverse of open drift signals
4. **Why Retrieval** (25 pts) — median time to answer "why did we build it this way?"

See [actions/COHERENCE_SCORE_SPEC.md](../../actions/COHERENCE_SCORE_SPEC.md) for the full formula.

## Updating the Score

For v0.1, the score is updated manually:
1. Edit `coherence_score.json`
2. Fill in the four component values
3. Commit with a message like `telemetry: update coherence score 2026-02-20`

Future versions will automate this via GitHub Actions.
