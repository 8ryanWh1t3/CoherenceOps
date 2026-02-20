# CANON-v1.3 -- Localization Policy and Pricing Parity

| Field          | Value                                      |
|----------------|--------------------------------------------|
| **Version**    | 1.3                                        |
| **Date**       | 2026-03-16                                 |
| **Author**     | @narrative-lead (Montreal), @loc-lead (Tokyo) |
| **Status**     | superseded (by CANON-v1.4, 2026-03-27)     |
| **Scope**      | Global (JP and EU-specific addenda)        |
| **Linked DLRs**| DLR-20260320-001                           |
| **Base**       | CANON-v1.2                                 |

---

## Summary

Addresses the localization divergence crisis exposed during W11-W12. The
Japanese client had fallen two canon versions behind (running CANON-v1.1
content while EN was on CANON-v1.3) after emergency patches in W10-W11
bypassed the localization review pipeline. Adds mandatory canon-diff tooling
for all localization workflows and establishes a regional pricing parity
standard within 15% of purchasing power parity (PPP).

---

## Diff from CANON-v1.2

### Added

1. **Canon-Diff Tooling Requirement** (New Section 5.5)
   - All localization pipelines must integrate canon-diff validation before
     deployment to any regional environment.
   - Canon-diff compares the current localized build against the latest
     ratified CANON version and flags string-level divergences.
   - Deployment to any region is blocked if canon-diff detects >0 critical
     divergences (quest dialogue, UI labels affecting gameplay, legal text).
   - Non-critical divergences (flavor text, loading screen tips) allowed
     with @loc-lead sign-off.
   - Tooling owned by Warsaw (QA pipeline integration) with Montreal
     providing the canonical string database.

2. **Regional Pricing Parity Standard** (New Section 4.7)
   - All in-game pricing must fall within 15% of the PPP-adjusted
     equivalent of the US base price.
   - Parity calculated quarterly using IMF PPP data.
   - Pricing drift detected outside the 15% band triggers an automatic
     review by @finance-lead within 5 business days.
   - DRIFT-20260317-001 (cross-region pricing parity drift NA vs EU)
     was the precipitating signal for this policy.
   - DRIFT-20260325-001 (residual LATAM drift) remains open at time of
     publication.

3. **JP Localization Resync Plan** (Section 5.6)
   - 47 strings across 12 quest lines diverged between JP and EN.
   - Resync target: all critical strings within 1 sprint (ASM-0014).
   - Non-critical strings: within 2 sprints.
   - JP player NPS impact: -22 points week-over-week.
   - Estimated rework cost: $1.4M (localization vendor + internal QA).
   - Full resync scheduled for CANON-v1.4 deployment.

### Modified

4. **Localization Quality Standard** (Section 5.4, updated from v1.0)
   - Previous: "Localized builds must match the current CANON version
     within one business day of English deployment."
   - Updated: "Localized builds must pass canon-diff validation before
     deployment. No regional build may ship content older than the
     current CANON version minus one."
   - Rationale: the "one business day" SLA was unenforceable during
     crisis periods when multiple canon versions shipped in rapid
     succession (v1.2 and v1.3 within 7 days).

5. **EU Monetization Addendum** (Section 4.6, updated from v1.2)
   - Added: direct-purchase catalog must include equivalent cosmetic
     variety to the retired loot box catalog within 30 days.
   - Conversion progress: 68% of loot box items available as direct
     purchase at time of publication.

### Unchanged

- Mission canon (Section 1) -- no changes.
- Technical architecture (Section 2) -- no changes.
- Tournament rules (Section 3) -- no changes.
- Kill switch policy (Section 4.5) -- no changes.
- Canon contradiction acknowledgment (Section 7) -- no changes.

---

## Rationale

The JP localization divergence (DRIFT-20260320-001) revealed a systemic
failure in the localization pipeline: emergency patches deployed during W10
(esports spike) and W11 (monetization backlash) bypassed the standard
localization review gate. Tokyo's localization team was not notified of 3
of the 5 emergency patches that modified player-facing strings.

The root cause was not negligence but process: the emergency hotfix bypass
protocol (DLR-20260306-002) had no localization checkpoint. When the bypass
was invoked 4 times in 10 days, JP and KR clients accumulated a growing
delta against the EN canonical version.

Separately, the cross-region pricing parity drift (DRIFT-20260317-001)
exposed a $2.40 (18%) gap between NA and EU cosmetic pricing after the
emergency MTX adjustments. Without a formal parity standard, each region's
pricing was drifting independently.

**Financial impact:**
- JP localization rework: $1.4M
- KR localization rework: $0.6M
- Pricing parity audit cost: $0.3M
- JP NPS recovery campaign: $0.9M
- Total: $3.2M

---

## Assumptions Affected

| ASM ID   | Description                              | Status  |
|----------|------------------------------------------|---------|
| ASM-0014 | JP localization resync in 1 sprint       | new, active |
| ASM-0013 | Refund policy change reduces churn 15%   | active  |
| ASM-0011 | Direct purchase conversion >60% loot box | active  |

---

## Canon Linkage

- **Supersedes:** CANON-v1.2
- **Superseded by:** CANON-v1.4
- **Linked DLRs:** DLR-20260320-001, DLR-20260309-002, DLR-20260309-003
- **Linked Drifts:** DRIFT-20260320-001, DRIFT-20260317-001, DRIFT-20260325-001
- **MASTER_INDEX Row:** 90
