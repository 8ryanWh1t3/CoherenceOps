# Sample Mode (COHERENCE_ROOT)

Run CoherenceOps dashboards, scoring, and local checks against **sample data packs** without copying files into `coherence/`.

## How It Works

The environment variable `COHERENCE_ROOT` controls which directory scripts and workflows read from.

| Variable | Default | Purpose |
|----------|---------|---------|
| `COHERENCE_ROOT` | `coherence` | Root directory for intel, decisions, drift, canon, telemetry |
| `TELEMETRY_OUT_DIR` | `coherence/telemetry` | Where generated outputs are written |

When `COHERENCE_ROOT` is set to anything other than `coherence`, the output directory switches automatically:

```
TELEMETRY_OUT_DIR = telemetry_out/<sanitized_root>/
```

For example, `COHERENCE_ROOT=sample_data/game_studio_aaa` writes outputs to `telemetry_out/sample_data_game_studio_aaa/`.

This keeps sample data read-only and avoids polluting the sample pack with generated files.

## What Gets Read (from COHERENCE_ROOT)

- `${COHERENCE_ROOT}/intel/assumptions.yaml`
- `${COHERENCE_ROOT}/drift/*.md`
- `${COHERENCE_ROOT}/telemetry/coherence_score.json` (for prior score data)

## What Gets Written (to TELEMETRY_OUT_DIR)

- `weekly_rollup.json`
- `top_risks.md`
- `coherence_score.json`
- `coherence_badge.json`

## Run Locally

### Default (production)

```bash
bin/coherence-check
```

Reads from `coherence/`, writes to `coherence/telemetry/`.

### Sample mode

```bash
COHERENCE_ROOT=sample_data/game_studio_aaa bin/coherence-check
```

Reads from `sample_data/game_studio_aaa/`, writes nothing (check is read-only).

### Validate a root

```bash
COHERENCE_ROOT=sample_data/game_studio_aaa bin/coherence-root
```

Prints resolved paths and validates that required files exist.

## Run via GitHub Actions (workflow_dispatch)

The following workflows accept a `coherence_root` input:

- **Coherence Weekly Rollup** (`coherence-weekly-rollup.yml`)
- **Coherence Score** (`coherence-score.yml`)
- **Drift Auto-Detection** (`drift-auto-detect.yml`)

### From the GitHub UI

1. Go to **Actions** > select the workflow
2. Click **Run workflow**
3. Set `coherence_root` to `sample_data/game_studio_aaa`
4. Click **Run workflow**

### From the CLI

```bash
gh workflow run coherence-weekly-rollup.yml -f coherence_root=sample_data/game_studio_aaa
gh workflow run coherence-score.yml -f coherence_root=sample_data/game_studio_aaa
```

Scheduled runs always default to `coherence` (production).

## Safety Guards

The following tools are **production-only** and will refuse to run in sample mode:

- `bin/coherence-new-dlr` — creates new DLR files
- `bin/coherence-new-drift` — creates new drift signals

These tools always write to `coherence/decisions/` and `coherence/drift/` respectively. If `COHERENCE_ROOT` is set to anything other than `coherence`, they print a warning and exit.

## Available Sample Packs

| Pack | Path | Records |
|------|------|---------|
| AAA Game Studio | `sample_data/game_studio_aaa` | 100 (35 DLR, 25 DRIFT, 15 ASM, 10 CLM, 5 CANON, 5 TEL) |
