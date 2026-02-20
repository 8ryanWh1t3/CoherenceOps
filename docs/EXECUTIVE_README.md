# How to Read Coherence Health in 60 Seconds

## The Badge

Look at the repo README. The coherence badge shows a score from 0 to 100.

| Color | Score | Meaning |
|-------|-------|---------|
| Green | 90-100 | Excellent — all governance current |
| Blue | 70-89 | Good — minor items to address |
| Yellow | 50-69 | Needs Attention — expired assumptions or open drift |
| Red | 0-49 | Critical — governance gaps, action required |

## The Score Components

Open `coherence/telemetry/coherence_score.json`:

| Component | What It Measures |
|-----------|-----------------|
| DLR Coverage | % of major PRs that linked a decision record |
| Assumption Currency | % of active assumptions that haven't expired |
| Drift Health | Penalty for each open drift signal |
| Why Retrieval | How fast a new person can answer "why did we build it this way?" |

## Weekly Rollup

Every Monday, the rollup workflow generates:
- `coherence/telemetry/weekly_rollup.json` — machine-readable summary
- `coherence/telemetry/top_risks.md` — ranked list of what needs attention

## What To Do When Score Is Low

| Symptom | Action |
|---------|--------|
| DLR Coverage low | Ensure major PRs reference a DLR in the body |
| Assumptions expired | Review `coherence/intel/assumptions.yaml` — extend, validate, or retire |
| Drift signals open | Triage `coherence/drift/` — assign owners, open patch PRs |
| Why Retrieval slow | Improve DLR quality — better context, clearer trade-offs |

## Where To Start

1. Check the badge
2. Open `coherence/telemetry/top_risks.md`
3. Fix the top item
4. Repeat weekly
