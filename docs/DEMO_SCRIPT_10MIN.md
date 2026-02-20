# 10-Minute Demo Script (Spoken Walkthrough)

Use this outline when presenting CoherenceOps to a team or stakeholder.

---

## Minute 0-1: The Problem

> "If your lead left tomorrow, could a new hire answer 'why did we build it this way?' in under 60 seconds?"
>
> Probably not. Decisions live in Slack. Assumptions rot. Architecture commitments exist in someone's head.
>
> CoherenceOps fixes this with four modules: Truth, Reasoning, Memory, and Correction. All in your repo. No SaaS.

## Minute 1-3: Show the Structure

Open the repo. Walk through:

- `coherence/intel/` — "Here's what we believe and when it expires"
- `coherence/decisions/` — "Here's what we decided and why"
- `coherence/canon/` — "Here's what we committed to"
- `coherence/drift/` — "Here's what went wrong and how we fixed it"

> "Every folder has a README with a one-click create link. Zero friction."

## Minute 3-5: Live Gate Demo

Show a PR that triggers gates:

1. Open a PR touching `coherence/canon/architecture.md`
2. Point at the summary comment — Gate 1 fails (no DLR)
3. Add `DLR-0001` to the PR body
4. Re-run — Gate 1 passes

> "The system enforces governance automatically. No human bottleneck."

## Minute 5-7: Drift Detection

Show the assumption expiry flow:

1. Point at `assumptions.yaml` — show the `expires` field
2. Swap in the expired fixture
3. Show Gate 2 failure
4. Create a drift signal — show the template
5. Patch: extend the expiry, mark drift as `patched`

> "When reality changes, the system tells you. Then you fix it and move on."

## Minute 7-9: Coherence Score

Show:

- The badge in the README
- `coherence/telemetry/coherence_score.json`
- The dashboard issue (if it exists)

> "One number: 0 to 100. Four components. Updated weekly. No opinions — just math."

## Minute 9-10: Adoption

> "Three ways to adopt: copy the folder, use as a template, or run `coherence-init`. Five minutes to set up. Zero dependencies."

Show `bin/coherence-init` running in a fresh repo (optional).

Close with:

> "Coherence is infrastructure, not culture. This makes it enforceable."

---

## Tips

- Pre-stage the expired fixture so the demo doesn't depend on real dates
- Have two browser tabs ready: one on the PR, one on the repo tree
- The demo works best with a real repo — avoid slides
