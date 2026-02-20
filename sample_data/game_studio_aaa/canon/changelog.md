# Canon Changelog -- Eclipse Dominion

> **Product:** Eclipse Dominion
> **Owner:** @narrative-lead (Montreal)
> **Window:** W09--W13 2026 (Feb 24 -- Mar 27)
> **Versions:** v1.0 through v1.4

---

## Version History

| Version | Date       | Summary                                   | Breaking Changes | DLR Reference |
|---------|------------|-------------------------------------------|------------------|---------------|
| v1.0    | 2026-02-24 | Canon Baseline: Season 4 Launch           | N/A (initial)    | DLR-20260226-001, DLR-20260224-004 |
| v1.1    | 2026-03-02 | Tournament Rules and Balance Freeze       | None             | DLR-20260302-003 |
| v1.2    | 2026-03-09 | MTX Policy and Emergency Rollback         | Loot box mechanics suspended in EU; executive sign-off threshold lowered from 15% to 5% of revenue | DLR-20260309-001 |
| v1.3    | 2026-03-16 | Localization Policy and Pricing Parity    | Localization deployment blocked without canon-diff validation; pricing parity band enforced at 15% PPP | DLR-20260320-001 |
| v1.4    | 2026-03-27 | Narrative Review Gate and Incident SOP    | Narrative review gate mandatory for all live events (no bypass); emergency hotfix bypass now requires localization checkpoint | DLR-20260327-001, DLR-20260327-002 |

---

## Detailed Change Log

### v1.0 -- Canon Baseline: Season 4 Launch (2026-02-24)

- **Author:** @narrative-lead
- **Status:** superseded
- **Sections established:** Mission canon, technical architecture, competitive
  integrity rules, monetization framework, public commitments.
- **Breaking changes:** None (initial baseline).
- **Assumptions registered:** ASM-0001, ASM-0002, ASM-0003, ASM-0004, ASM-0006.
- **Notes:** First versioned canon under CoherenceOps governance. Replaces
  unversioned wiki-based institutional knowledge.

### v1.1 -- Tournament Rules and Balance Freeze (2026-03-02)

- **Author:** @narrative-lead, @esports-lead
- **Status:** superseded
- **Sections added:** Tournament balance freeze policy (3.1), broadcast
  scheduling rules (3.5), sponsor integration guidelines (6).
- **Sections modified:** Server fleet capacity reference (2).
- **Breaking changes:** None. All additions are forward-compatible.
- **Assumptions referenced:** ASM-0005 (tournament CCU 620K -- later expired).
- **Notes:** Issued at the start of the Apex Invitational. ASM-0005 was
  invalidated within hours of publication (DRIFT-20260302-001).

### v1.2 -- MTX Policy and Emergency Rollback (2026-03-09)

- **Author:** @narrative-lead, @monetization-lead
- **Status:** superseded
- **Sections added:** Kill switch policy (4.5), EU monetization addendum (4.6),
  canon contradiction acknowledgment (7).
- **Sections modified:** Monetization framework (4) -- loot boxes suspended in EU.
- **Breaking changes:**
  - Loot box mechanics suspended in EU markets. All randomized reward mechanics
    must be converted to direct purchase.
  - Executive sign-off threshold lowered from 15% to 5% of revenue.
- **Assumptions affected:** ASM-0004 (under review), ASM-0007 (expired),
  ASM-0011 (new).
- **Financial exposure at publication:** ~$79.4M combined.
- **Notes:** Emergency canon update. Fastest canon turnaround in AetherForge
  history (14 hours from trigger to ratification). First canon version to
  formally acknowledge an internal contradiction.

### v1.3 -- Localization Policy and Pricing Parity (2026-03-16)

- **Author:** @narrative-lead, @loc-lead
- **Status:** superseded
- **Sections added:** Canon-diff tooling requirement (5.5), regional pricing
  parity standard (4.7), JP localization resync plan (5.6).
- **Sections modified:** Localization quality standard (5.4) -- "one business
  day" SLA replaced with canon-diff validation gate. EU monetization addendum
  (4.6) -- direct-purchase catalog completeness requirement added.
- **Breaking changes:**
  - Localization deployment blocked without canon-diff validation (zero
    critical divergences allowed).
  - Regional pricing must fall within 15% of PPP-adjusted US base price.
- **Assumptions registered:** ASM-0014 (JP resync in 1 sprint).
- **Financial impact:** $3.2M localization rework.
- **Notes:** Second canon version issued in 7 days. The rapid succession
  of v1.2 and v1.3 itself caused the JP canon version gap that this
  version addresses.

### v1.4 -- Narrative Review Gate and Incident SOP (2026-03-27)

- **Author:** @narrative-lead, @ops-lead
- **Status:** current
- **Sections added:** Narrative review gate for live events (3.6), global
  incident response SOP (8), post-mortem framework (8.3).
- **Sections modified:** Emergency hotfix bypass protocol (localization
  checkpoint added), JP localization status (resync 87% complete).
- **Breaking changes:**
  - Narrative review gate mandatory for all live events. No bypass path.
  - Emergency hotfix bypass now requires @loc-lead notification within
    1 hour and localization delta assessment within 4 hours.
- **Assumptions invalidated by W10-W13 arc:** ASM-0005, ASM-0007, ASM-0012.
- **Total crisis cost (W10-W13):** ~$45.8M.
- **Notes:** Stabilization version. Encodes institutional learning from three
  cascading crises into operational canon. 6 unresolved drift items carried
  forward into W14.

---

## Seed Documents

These seed documents are the foundation of all canon versions and are
updated independently from the version sequence:

| Document               | Last Updated | Owner           |
|------------------------|--------------|-----------------|
| mission.md             | 2026-02-24   | @exec-team      |
| architecture.md        | 2026-02-24   | @infra-lead     |
| public-commitments.md  | 2026-03-09   | @exec-team      |

---

## Statistics

| Metric                          | Value |
|---------------------------------|-------|
| Total versions (W09-W13)        | 5     |
| Emergency versions              | 1 (v1.2) |
| Breaking changes                | 3 (v1.2, v1.3, v1.4) |
| Assumptions registered          | 15    |
| Assumptions expired/invalidated | 3 (ASM-0005, ASM-0007, ASM-0012) |
| Canon contradictions logged     | 1 (monetization pledge) |
| Fastest turnaround              | 14h (v1.2) |
| Longest gap between versions    | 11 days (v1.3 to v1.4) |
