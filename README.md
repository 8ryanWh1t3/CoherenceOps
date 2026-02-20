# CoherenceOps

**Coherence is infrastructure, not culture.**

[![Coherence Score](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/8ryanWh1t3/CoherenceOps/main/coherence/telemetry/coherence_badge.json&style=flat-square)](coherence/telemetry/coherence_score.json)

GitHub-native governance for any repo. Track truth, record reasoning, protect memory, detect drift, ship patches.

---

## What Is This?

CoherenceOps is a folder-and-template system that turns your GitHub repo into a governed decision surface. No SaaS, no agents, no vendor lock-in. Just Markdown, YAML, and the workflows you already use.

It implements four modules:

| Module | Folder | Purpose |
|--------|--------|---------|
| **IntelOps** (Truth) | `coherence/intel/` | Claims, assumptions, provenance — what you believe and why |
| **ReOps** (Reasoning) | `coherence/decisions/` | Decision Ledger Records — what you decided and what you traded off |
| **FranOps** (Memory) | `coherence/canon/` | Canon — mission, architecture, commitments that outlive any individual |
| **DriftOps** (Correction) | `coherence/drift/` | Drift signals and patch PRs — what changed and how you fixed it |

Plus a **telemetry** surface (`coherence/telemetry/`) for scoring coherence health.

```mermaid
graph LR
    subgraph IntelOps["IntelOps (Truth)"]
        CLM[Claims] --> PRV[Provenance]
        ASM[Assumptions<br/>+ half-life]
    end

    subgraph ReOps["ReOps (Reasoning)"]
        DLR[Decision<br/>Ledger Records]
    end

    subgraph FranOps["FranOps (Memory)"]
        CAN[Canon]
        CHL[Changelog]
    end

    subgraph DriftOps["DriftOps (Correction)"]
        DRF[Drift Signals]
        PAT[Patch PRs]
    end

    subgraph Telemetry
        SCR[Coherence<br/>Score 0-100]
    end

    ASM -->|"depends on"| DLR
    CLM -->|"supports"| DLR
    DLR -->|"may change"| CAN
    CAN -->|"changelog"| CHL
    ASM -.->|"expires"| DRF
    DLR -.->|"invalidated"| DRF
    CAN -.->|"contradicted"| DRF
    DRF -->|"fix"| PAT

    IntelOps --> SCR
    ReOps --> SCR
    DriftOps --> SCR
```

## Why?

Ask yourself: **If your lead left tomorrow, could a new person answer "why did we build it this way?" in under 60 seconds?**

If not, you have a coherence problem. Decisions live in Slack threads, assumptions rot in stale docs, architectural commitments exist only in someone's head. When that person leaves, institutional memory leaves with them.

CoherenceOps makes the invisible visible — and keeps it current.

## How to Adopt

### Option A: Copy the folder
```bash
cp -r coherence/ /path/to/your-repo/coherence/
cp -r .github/ /path/to/your-repo/.github/
```

### Option B: Git submodule
```bash
git submodule add https://github.com/ORG/CoherenceOps.git coherence-ops
```

### Option C: Use as a template
Click **Use this template** on GitHub to create a new repo with the full structure.

### Option D: Run `coherence-init`
```bash
git clone https://github.com/8ryanWh1t3/CoherenceOps.git /tmp/coherence-ops
/tmp/coherence-ops/bin/coherence-init .
```
Bootstraps the full `coherence/` folder, templates, and labels into your existing repo. Zero dependencies.

## Demo Workflow (6 Steps)

1. **Developer opens a PR** that changes core architecture
2. **PR template asks**: DLR link? Assumptions touched? Canon impact?
3. **Developer creates a DLR** via the one-click link in `coherence/decisions/README.md`
4. **Reviewer verifies** the DLR covers trade-offs, blast radius, and rollback
5. **PR merges** — the decision is sealed in version control forever
6. **Three months later**, an assumption expires. A **Drift** signal opens. A **Patch PR** resolves it.

That's the loop: **Decide → Seal → Drift → Patch → Repeat.**

## Quick Links

| Resource | Link |
|----------|------|
| 1-Page Quick Start | [docs/QUICKSTART_1PAGE.md](docs/QUICKSTART_1PAGE.md) |
| Swim Lane Diagram | [docs/SWIMLANE.md](docs/SWIMLANE.md) |
| Principles | [docs/PRINCIPLES.md](docs/PRINCIPLES.md) |
| Glossary | [docs/GLOSSARY.md](docs/GLOSSARY.md) |
| 30-Min Training Outline | [docs/TRAINING_30MIN_OUTLINE.md](docs/TRAINING_30MIN_OUTLINE.md) |

## What's a "Major PR"?

A PR is **major** (and requires a DLR) if any of these are true:

- It has the `major` label
- It changes more than 10 files
- It touches `coherence/canon/`, `coherence/intel/`, or core architecture folders

Everything else is a normal PR. No overhead.

## Scoring

CoherenceOps defines a simple **Coherence Score** (0-100) based on:

- DLR coverage for major PRs
- Expired assumption count
- Open drift signal count
- Median "why retrieval" time

See [actions/COHERENCE_SCORE_SPEC.md](actions/COHERENCE_SCORE_SPEC.md) for the formula.

## License

[MIT](LICENSE)

## Version

v0.3.0 — See [CHANGELOG.md](CHANGELOG.md)
