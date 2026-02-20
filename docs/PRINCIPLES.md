# CoherenceOps Principles

## 1. Decisions Are Artifacts

Every significant decision gets a record. Not a Slack message, not a meeting note — a versioned, reviewable, searchable artifact in the repo where the code lives.

## 2. Assumptions Expire

Every assumption has a half-life. Treat "we believe X" the same way you treat a cache TTL: it's valid until it isn't, and you need a mechanism to detect when it goes stale.

## 3. Canon Is Protected Memory

Mission, architecture, and public commitments are canon. Changing canon is a deliberate, versioned act with a changelog entry and a steward's approval. Canon doesn't drift silently.

## 4. Drift Is Normal

Systems drift. Assumptions go stale, decisions become outdated, reality diverges from intent. The failure isn't drifting — it's not detecting it. CoherenceOps makes drift visible and patchable.

## 5. Why Retrieval Is the KPI

The ultimate test: can a new team member find out *why* something was built this way in under 60 seconds? If yes, your coherence infrastructure is working. If no, decisions are trapped in heads.

## 6. Infrastructure Over Culture

"We have a culture of documentation" is not a system. Infrastructure means: templates that prompt, gates that block, scores that measure, and loops that correct. Culture helps; infrastructure guarantees.

## 7. Minimal Overhead, Maximum Signal

CoherenceOps adds process only where it prevents loss. Normal PRs get zero overhead. Major decisions get a DLR. Expired assumptions get a drift signal. That's it.
