# Demo: Drift to Patch in 10 Minutes

A reproducible walkthrough showing the full CoherenceOps governance loop.

---

## Prerequisites

- A fork or clone of CoherenceOps with GitHub Actions enabled
- `ORG/REPO` placeholders replaced (run `bin/coherence-adopt`)
- Labels created (run the label-bootstrap workflow)

## Step 1: Open a Major PR Without DLR (Gate Fails)

```bash
git checkout -b demo/drift-patch
echo "# Demo change" >> coherence/canon/architecture.md
git add coherence/canon/architecture.md
git commit -m "demo: touch architecture"
git push -u origin demo/drift-patch
```

Open a PR on GitHub. Add the `major` label.

**Expected:** Gate 1 fails — _"Major PR has no DLR linked."_

## Step 2: Add a DLR Reference (Gate Passes)

Create `coherence/decisions/DLR-0002.md`:

```markdown
# DLR-0002: Demo Architecture Change

## Status
Accepted

## Context
Demonstrating the governance loop.

## Options Considered
1. Skip governance — fast but no audit trail
2. Use CoherenceOps — adds 5 minutes, full traceability

## Decision
Option 2. Ship with a DLR.

## Trade-offs
Slightly slower for full auditability.

## Assumptions
- ASM-0001

## Blast Radius
Demo only — no production impact.

## Rollback
Revert the PR.

## Owner
@your-handle

## Date
YYYY-MM-DD
```

Add `coherence/decisions/DLR-0002.md` to the PR body, then push.

**Expected:** Gate 1 passes. Gate 3 fails (canon changed without changelog).

## Step 3: Update Canon Changelog (Gate 3 Passes)

Add an entry to `coherence/canon/changelog.md`:

```markdown
## YYYY-MM-DD
- Updated architecture.md (demo change, DLR-0002)
```

Push. **Expected:** Gates 1 + 3 pass.

## Step 4: Force an Expired Assumption (Gate 2 Fails)

Copy the expired fixture into place:

```bash
cp demo/fixtures/assumptions_expired.yaml coherence/intel/assumptions.yaml
git add coherence/intel/assumptions.yaml
git commit -m "demo: force expired assumption"
git push
```

**Expected:** Gate 2 fails — _"Expired assumptions: ASM-0001"_

## Step 5: Create a Drift Signal

Create `coherence/drift/DRIFT-0002.md`:

```markdown
# DRIFT-0002: Assumption ASM-0001 Expired

## Severity
medium

## What Drifted
ASM-0001 ("Teams will adopt folder-based governance") expired without re-validation.

## Evidence
Gate 2 failure on demo PR. Assumption expiry date passed.

## Affected
- Assumption: ASM-0001
- DLR: DLR-0001

## Proposed Patch
Re-validate ASM-0001 with current adoption data. Extend expiry or retire.

## Patch PR
[this PR]

## Status
open
```

Push. **Expected:** Gate 4 passes (valid drift format).

## Step 6: Patch and Resolve

Restore assumptions with extended expiry:

```bash
cp demo/fixtures/assumptions_near_expiry.yaml coherence/intel/assumptions.yaml
```

Update `DRIFT-0002.md` status to `patched`. Push.

**Expected:** All gates pass. Summary comment shows green.

---

## Proof Checklist (30 seconds)

- [ ] Gate 1 failed without DLR, passed with DLR
- [ ] Gate 2 failed on expired assumption
- [ ] Gate 3 failed without changelog, passed with it
- [ ] Gate 4 passed on valid drift signal
- [ ] Summary comment posted and updated (not duplicated)
- [ ] Full loop: Decide -> Seal -> Drift -> Patch
