# CoherenceOps Feature Catalog

Machine source of truth: `coherence/telemetry/feature_catalog.json`

## Categories

### Core Artifacts
DLR / RS / DS / MG as the minimal institutional decision memory set.

- **Decision Lineage Record (DLR)** (`DLR`)
  - Artifacts: artifacts/DLR.md
  - Enforcement: coherence gate
  - Lenses: PRIME, EXEC, OPS
- **Reasoning Spec (RS)** (`RS`)
  - Artifacts: artifacts/RS.md
  - Enforcement: coherence gate
  - Lenses: PRIME, EXEC, OPS
- **Drift Signature (DS)** (`DS`)
  - Artifacts: artifacts/DS.md
  - Enforcement: weekly drift triage
  - Lenses: AI/TECH, OPS
- **Memory Graph (MG)** (`MG`)
  - Artifacts: artifacts/MG.*
  - Enforcement: why retrieval checks
  - Lenses: MEMORY, EXEC

### Governance Gates
Pre-merge / pre-decision enforcement that prevents governance theater.

- **DLR Required Gate** (`DLR_REQUIRED`)
  - Artifacts: artifacts/DLR.md
  - Enforcement: CI gate
  - Lenses: PRIME
- **Assumption TTL / Half-life** (`ASSUMPTION_TTL`)
  - Artifacts: artifacts/DLR.md, artifacts/RS.md
  - Enforcement: expiry alerts
  - Lenses: PRIME, EXEC
- **Seal -> Version -> Patch (No Overwrite)** (`NO_OVERWRITE`)
  - Artifacts: patches/*
  - Enforcement: workflow policy
  - Lenses: PRIME

### Drift -> Patch Loop
Detect drift, triage, patch, and update memory as a releaseable operation.

- **Drift Event Capture** (`DRIFT_EVENTS`)
  - Artifacts: artifacts/DS.md
  - Enforcement: weekly drift rollup
  - Lenses: OPS, AI/TECH
- **Patch Release Workflow** (`PATCH_RELEASE`)
  - Artifacts: patches/*, release_notes.md
  - Enforcement: monthly patch cadence
  - Lenses: EXEC, OPS

### Coherence Index & Telemetry
0-100 Coherence Index with thresholds + adoption stages.

- **Coherence Index Score** (`CI_SCORE`)
  - Artifacts: docs/COHERENCE_INDEX.md
  - Enforcement: CI job
  - Lenses: EXEC, AI/TECH
- **Adoption Threshold Stages** (`ADOPTION_STAGES`)
  - Artifacts: docs/ADOPTION_THRESHOLDS.md
  - Enforcement: exec review
  - Lenses: EXEC

### Lenses & Interfaces
6 lenses and interactive surfaces that make governance legible.

- **Six Lenses Model** (`SIX_LENSES`)
  - Artifacts: docs/6_LENSES.md
  - Enforcement: training
  - Lenses: ICON, HUMAN, AI/TECH
- **Interactive Architecture View** (`INTERACTIVE_ARCH`)
  - Artifacts: *.html
  - Enforcement: docs build
  - Lenses: ICON

## Outer-Edge Boundaries

- Not claiming runtime model safety control
- Not claiming cryptographic attestation of runtime actions
- Not claiming comprehensive legal policy packs
- Not claiming replacement of enterprise GRC tooling
