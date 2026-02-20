# FranOps (Memory / Canon)

Protected institutional memory. These files represent commitments that outlive any individual.

## Files

| File | Purpose |
|------|---------|
| [mission.md](mission.md) | Why this project exists |
| [architecture.md](architecture.md) | Core architectural commitments |
| [public-commitments.md](public-commitments.md) | Promises made to users, partners, or stakeholders |
| [changelog.md](changelog.md) | Every change to canon, with date and rationale |

## Rules

- **All canon changes require a changelog entry** in `changelog.md`
- Canon changes should be reviewed by a Canon Steward
- Changing canon without updating the changelog will be flagged by CI
- When canon changes, check if any DLRs or assumptions are affected
- Canon files are append-mostly: supersede, don't delete

## Canon Steward

The Canon Steward is responsible for:
- Reviewing PRs that touch `coherence/canon/`
- Ensuring changelog entries are complete
- Triggering drift signals when canon changes invalidate existing decisions
