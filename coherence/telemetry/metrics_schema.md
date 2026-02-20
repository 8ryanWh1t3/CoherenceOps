# Metrics Schema

## coherence_score.json

```json
{
  "version": "string — semver of CoherenceOps",
  "date": "string — YYYY-MM-DD of measurement",
  "score": "integer — 0-100 composite score",
  "components": {
    "<component_name>": {
      "value": "integer — 0-100 raw component value",
      "weight": "integer — max points this component contributes",
      "points": "integer — actual points earned (value * weight / 100)",
      "detail": "string — human-readable explanation"
    }
  }
}
```

## Components

| Component | Measures | Source |
|-----------|----------|--------|
| `dlr_coverage` | % of major PRs with a linked DLR | PR metadata |
| `assumption_currency` | % of assumptions with `status: active` and `expires > today` | `assumptions.yaml` |
| `drift_health` | 100 - (open_drift_count * 20), floor 0 | `coherence/drift/` file count with status: open |
| `why_retrieval` | Inverse of median retrieval time: `100 - min(retrieval_seconds, 100)` | Manual measurement or automation |

## Scoring

`score = sum(component.points for each component)`

Maximum: 100 (25 + 25 + 25 + 25)
