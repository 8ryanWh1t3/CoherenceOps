# CoherenceOps Quick Start (1 Page)

## When to Create a DLR

Create a **Decision Ledger Record** when your PR is "major":
- Has the `major` label
- Changes 10+ files
- Touches `coherence/canon/`, `coherence/intel/`, or core architecture

## How to Create a DLR

1. Go to [`coherence/decisions/README.md`](../coherence/decisions/README.md)
2. Click the **"Create New DLR"** link
3. Fill in the template: context, options, decision, trade-offs, blast radius, rollback
4. Commit to your branch
5. Reference the DLR path in your PR

## How to Update Assumptions

1. Go to [`coherence/intel/README.md`](../coherence/intel/README.md)
2. Click the **"Edit assumptions.yaml"** link
3. Add or update your assumption with an `expires` date and `half_life`
4. Commit to your branch

## How to Open a Drift Signal

When something no longer matches reality:

1. Go to [`coherence/drift/README.md`](../coherence/drift/README.md)
2. Click the **"Create New Drift"** link
3. Fill in: what drifted, severity, evidence, proposed patch
4. Open a Patch PR that fixes the root cause

## Owner Responsibilities

| Role | Must Do |
|------|---------|
| **PR Author** | Create DLR for major PRs, list assumptions touched |
| **Reviewer** | Verify DLR completeness, check assumption currency |
| **Decision Owner** | Own the DLR post-merge, respond to drift signals |
| **Canon Steward** | Approve canon changes, maintain changelog |

## Targets

| Metric | Target |
|--------|--------|
| Median "why retrieval" | 60 seconds |
| DLR coverage (major PRs) | 100% |
| Expired assumptions | 0 |
| Open drift signals | < 3 |
| Coherence Score | > 80 |
