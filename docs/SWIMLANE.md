# CoherenceOps Swim Lane

End-to-end flow from PR to drift resolution.

```mermaid
sequenceDiagram
    participant DEV as Developer
    participant REPO as Repo (Folders)
    participant CI as CI / Automation
    participant OWN as Decision Owner
    participant LEAD as Leadership

    Note over DEV,LEAD: Phase 1 — PR Opened

    DEV->>REPO: Open PR (code changes)
    DEV->>REPO: Create DLR in coherence/decisions/
    DEV->>REPO: Update coherence/intel/assumptions.yaml
    DEV->>REPO: Fill PR template (DLR link, assumptions, canon impact)

    Note over DEV,LEAD: Phase 2 — Validation Gates

    CI->>REPO: Check: major PR has DLR?
    CI->>REPO: Check: assumptions not expired?
    CI->>REPO: Check: canon change has changelog entry?
    CI-->>DEV: Pass / Fail with guidance

    Note over DEV,LEAD: Phase 3 — Merge Seals Decision

    OWN->>REPO: Review DLR completeness
    OWN->>DEV: Approve PR
    DEV->>REPO: Merge PR
    REPO->>REPO: Decision sealed in git history

    Note over DEV,LEAD: Phase 4 — Drift → Patch Loop

    CI->>REPO: Detect: assumption expired
    CI->>OWN: Notify: drift signal
    OWN->>REPO: Create DRIFT record in coherence/drift/
    OWN->>DEV: Assign patch PR
    DEV->>REPO: Open patch PR (fixes drift root cause)
    OWN->>REPO: Review + merge patch
    REPO->>REPO: Drift resolved, coherence restored

    Note over DEV,LEAD: Continuous — Coherence Score

    CI->>LEAD: Weekly coherence score report
    LEAD->>OWN: Address low-scoring areas
```

## Reading the Diagram

- **Left to right** = increasing authority
- **Top to bottom** = time progression through 4 phases
- **Solid arrows** = actions taken
- **Dashed arrows** = automated feedback
- The loop repeats: decide, seal, detect drift, patch
