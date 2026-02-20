# IntelOps (Truth)

What the team believes to be true, and why.

## Files

| File | Purpose |
|------|---------|
| [claims.yaml](claims.yaml) | Factual assertions with provenance and confidence |
| [assumptions.yaml](assumptions.yaml) | Beliefs with half-life and expiry dates |
| [provenance/](provenance/) | Supporting evidence and source documents |

## Quick Actions

> Replace `ORG` and `REPO` with your GitHub org and repo name.

- [Edit claims.yaml](https://github.com/ORG/REPO/edit/main/coherence/intel/claims.yaml) — Add or update a claim
- [Edit assumptions.yaml](https://github.com/ORG/REPO/edit/main/coherence/intel/assumptions.yaml) — Add or update an assumption

## Assumption Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Active: recorded with<br/>expires + half_life

    Active --> HalfLife: half-life reached
    HalfLife --> Active: re-validated

    Active --> Expired: expires date passed
    HalfLife --> Expired: expires date passed

    Expired --> DriftSignal: open drift in<br/>coherence/drift/

    Active --> Validated: confirmed by evidence
    Active --> Retired: no longer relevant

    Validated --> [*]
    Retired --> [*]
    DriftSignal --> [*]

    note right of HalfLife: Re-validate:<br/>is this still true?
    note right of Expired: BLOCKS merge<br/>unless waived
```

## Rules

- Every claim needs a `source` and `confidence` (low / medium / high)
- Every assumption needs an `expires` date and `half_life`
- When an assumption expires, open a [Drift signal](../drift/README.md)
- Provenance documents go in `provenance/` with a filename matching the claim ID
