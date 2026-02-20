# telemetry_out/

This directory contains **generated telemetry outputs** from non-production coherence roots (e.g., sample data packs).

When `COHERENCE_ROOT` is set to something other than `coherence`, scripts and workflows write outputs here instead of `coherence/telemetry/` to avoid polluting source data.

## Structure

```
telemetry_out/
  <sanitized_root>/
    weekly_rollup.json
    top_risks.md
    coherence_score.json
    coherence_badge.json
```

Example: running against `sample_data/game_studio_aaa` writes to:

```
telemetry_out/sample_data_game_studio_aaa/
```

## Contents

These files are generated and can be safely deleted or regenerated at any time.

See [docs/SAMPLE_MODE.md](../docs/SAMPLE_MODE.md) for details.
