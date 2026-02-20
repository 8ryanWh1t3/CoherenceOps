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

## Rules

- Every claim needs a `source` and `confidence` (low / medium / high)
- Every assumption needs an `expires` date and `half_life`
- When an assumption expires, open a [Drift signal](../drift/README.md)
- Provenance documents go in `provenance/` with a filename matching the claim ID
