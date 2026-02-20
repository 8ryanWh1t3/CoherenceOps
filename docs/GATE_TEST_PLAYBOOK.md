# Gate Test Playbook

Step-by-step verification for all four Coherence Gates.

---

## Gate 1: DLR Required for Major PRs

### Scenario A: Major PR without DLR — should FAIL

1. Create a branch and open a PR that touches >10 files (or add the `major` label).
2. Leave the PR body empty (no DLR reference).
3. **Expected:** Gate 1 fails with _"Major PR has no DLR linked."_

### Scenario B: Major PR with DLR path — should PASS

1. Same PR as above.
2. Edit the PR body to include a path: `coherence/decisions/DLR-0001.md`
3. Ensure `coherence/decisions/DLR-0001.md` exists in the branch.
4. **Expected:** Gate 1 passes with _"DLR linked: coherence/decisions/DLR-0001.md"_.

### Scenario C: Major PR with plain DLR ID — should PASS

1. Same PR as above.
2. Edit the PR body to include just `DLR-0001` (no path).
3. Ensure `coherence/decisions/DLR-0001.md` exists in the branch.
4. **Expected:** Gate 1 passes. The plain ID is resolved to the file path automatically.

### Scenario D: Non-major PR — should SKIP

1. Open a PR that changes fewer than 10 files, has no `major` label, and does not touch `coherence/canon/` or `coherence/intel/`.
2. **Expected:** Gate 1 skips with _"Not a major PR — DLR not required."_

---

## Gate 2: Assumption Expiry

### Scenario A: Expired assumption without waiver — should FAIL

1. Set an assumption's `expires` to a past date in `coherence/intel/assumptions.yaml`.
2. Open a PR.
3. **Expected:** Gate 2 fails with _"Expired assumptions: ASM-XXXX (expired YYYY-MM-DD)."_

### Scenario B: Expired assumption with waiver label — should WARN

1. Same as above, but add the `assumption-waiver` label to the PR.
2. **Expected:** Gate 2 warns (does not fail) with _"Expired assumptions waived."_

### Scenario C: Assumption expiring within 14 days — should WARN (not fail)

1. Set an assumption's `expires` to a date 1-13 days from today.
2. Open a PR.
3. **Expected:** Gate 2 warns with _"Warning: assumptions expiring within 14 days."_ The workflow does NOT fail.

### Scenario D: All assumptions current — should PASS

1. Ensure all active assumptions have `expires` dates more than 14 days out.
2. **Expected:** Gate 2 passes with _"X active assumptions, all current."_

---

## Gate 3: Canon Changelog Required

### Scenario A: Canon file changed without changelog — should FAIL

1. Modify any file under `coherence/canon/` (e.g., `mission.md`).
2. Do NOT update `coherence/canon/changelog.md`.
3. **Expected:** Gate 3 fails with _"Canon changed without a changelog entry."_

### Scenario B: Canon file changed with changelog — should PASS

1. Modify a file under `coherence/canon/`.
2. Also update `coherence/canon/changelog.md` with a new entry.
3. **Expected:** Gate 3 passes with _"Canon changed with changelog entry."_

### Scenario C: No canon files changed — should SKIP

1. Open a PR that does not touch `coherence/canon/`.
2. **Expected:** Gate 3 skips with _"No canon files changed."_

---

## Gate 4: Drift Format Validation

### Scenario A: New drift file with all required sections — should PASS

1. Add a new file matching `coherence/drift/DRIFT-NNN.md`.
2. Include all required sections: `## Severity`, `## What Drifted`, `## Evidence`, `## Affected`, `## Status`.
3. Set severity to one of: `low`, `medium`, `critical`.
4. **Expected:** Gate 4 passes with _"1 drift signal(s) validated."_

### Scenario B: New drift file missing sections — should WARN

1. Add a new `DRIFT-NNN.md` file missing one or more required sections.
2. **Expected:** Gate 4 warns with _"missing sections: ..."_ The workflow does NOT fail (non-blocking gate).

### Scenario C: Invalid severity value — should WARN

1. Add a new drift file with `## Severity` set to an invalid value (e.g., `high`).
2. **Expected:** Gate 4 warns with _"invalid severity."_

### Scenario D: No new drift files — should SKIP

1. Open a PR that does not add any new `DRIFT-*.md` files.
2. **Expected:** Gate 4 skips with _"No new drift signals added."_

---

## 30-Second Smoke Test Checklist

Run these checks after any change to `coherence-gates.yml`:

- [ ] Open a trivial PR (1 file, no canon/intel) — all gates skip or pass, summary comment posted
- [ ] Add the `major` label to that PR — Gate 1 fires and fails (no DLR in body)
- [ ] Add `DLR-0001` to the PR body — Gate 1 passes on re-run
- [ ] Remove the `major` label — Gate 1 skips again on re-run
- [ ] Verify the summary comment updates (not duplicated) on each re-run

## Local Smoke Test (bin/coherence-check)

```bash
# Run from repo root — mirrors gates locally
bin/coherence-check
```

Expected output: colored pass/warn/fail for each gate, overall summary, exit 0 if all pass.

---

## Common Failure Modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gate 1 fails on a non-major PR | PR has >10 files or touches `coherence/canon/` or `coherence/intel/` | Add a DLR reference, or reduce scope |
| Gate 1 fails despite DLR in body | DLR format not recognized (e.g. `DLR-01` — needs 4+ digits) | Use `DLR-0001` or `coherence/decisions/DLR-0001.md` |
| Gate 1 says "file not found" | DLR ID in body doesn't match an actual file in the branch | Create the file or fix the ID |
| Gate 2 fails unexpectedly | An assumption's `expires` date has passed | Update the date, retire the assumption, or add `assumption-waiver` label |
| Gate 2 warns but doesn't fail | Assumption expires within 14 days — this is intentional (warning only) | Review and extend or retire before expiry |
| Gate 3 fails on canon change | `coherence/canon/changelog.md` not updated in the same PR | Add a changelog entry describing what changed |
| Gate 4 warns about missing sections | New drift file missing `## Severity`, `## What Drifted`, `## Evidence`, `## Affected`, or `## Status` | Add the missing heading(s) |
| Gate 4 warns about invalid severity | Severity not one of `low`, `medium`, `critical` | Fix the value under `## Severity` |
| Summary comment duplicated | Bot comment detection failed (rare) | Delete the extra comment manually |
