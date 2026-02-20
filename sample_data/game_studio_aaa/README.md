# CoherenceOps Sample Data Pack: AAA Game Studio

## Purpose

This sample data pack provides a realistic, self-contained dataset for **demo, training, and stress-testing** CoherenceOps tooling against the operational complexity of a large live-service game studio. It covers five weeks of institutional decision records, drift events, assumptions, claims, canon versions, telemetry snapshots, and evidence artifacts -- all interconnected through cross-references that exercise every CoherenceOps surface.

Use this pack to:

- **Demo** CoherenceOps to stakeholders using a believable AAA scenario.
- **Train** teams on DLR/DRIFT/ASM/CLAIM/CANON workflows before rolling out on real data.
- **Stress-test** parsers, validators, and coherence checks against 100 interlinked records spanning multiple studios, regions, and severity levels.

## Company Profile

| Field | Value |
|---|---|
| Company | AetherForge Interactive |
| Employees | 1,200 |
| Annual Revenue | $480M |
| Product | *Eclipse Dominion* (live-service competitive shooter) |
| Studios | Los Angeles (HQ), Montreal, Tokyo, Berlin, Warsaw |
| Regions | NA, EU, APAC, LATAM |
| Time Window | W09--W13 2026 (Feb 24 -- Mar 27) |

### Studio Responsibilities

| Studio | Primary Role |
|---|---|
| LA | Platform ops, infrastructure, esports, comms |
| Montreal | Game design, balance, narrative |
| Tokyo | APAC infrastructure, netcode, matchmaking |
| Berlin | Monetization, EU compliance, localization |
| Warsaw | QA, anti-cheat, regression testing |

## Record Counts

| Type | Count | Description |
|---|---|---|
| DLR | 35 | Decision Ledger Records |
| DRIFT | 25 | Drift detection events |
| ASM | 15 | Assumptions |
| CLAIM | 10 | Claims |
| CANON | 5 | Canon versions (v1.0--v1.4) |
| TELEMETRY | 5 | Weekly telemetry snapshots (W09--W13) |
| EVID | 5 | Evidence artifacts |
| **Total** | **100** | |

## File Tree

```
game_studio_aaa/
  README.md                  # This file
  SCENARIO_DRIVER.md         # Demo script, scenario walkthroughs, load instructions
  MASTER_INDEX.csv           # 100-row index of every record (CSV)
  canon/
    versions/                # CANON-v1.0 through CANON-v1.4
  decisions/                 # DLR YAML files (35 records)
  drift/                     # DRIFT YAML files (25 records)
  intel/
    provenance/              # ASM, CLAIM, EVID files
  scenarios/                 # Scenario narrative docs
  telemetry/                 # Weekly telemetry snapshots (W09--W13)
```

## Loading

Copy the entire `game_studio_aaa/` directory into your CoherenceOps `/coherence/` root:

```bash
cp -r sample_data/game_studio_aaa/ coherence/
```

CoherenceOps will discover records via `MASTER_INDEX.csv` and the standard directory layout. See `SCENARIO_DRIVER.md` for a guided 10-minute demo path and detailed scenario walkthroughs.
