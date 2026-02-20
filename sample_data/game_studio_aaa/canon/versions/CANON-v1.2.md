# CANON-v1.2 -- MTX Policy and Emergency Rollback

| Field          | Value                                      |
|----------------|--------------------------------------------|
| **Version**    | 1.2                                        |
| **Date**       | 2026-03-09                                 |
| **Author**     | @narrative-lead (Montreal), @monetization-lead (Berlin) |
| **Status**     | superseded (by CANON-v1.3, 2026-03-16)     |
| **Scope**      | Global (EU-specific addenda)               |
| **Linked DLRs**| DLR-20260309-001                           |
| **Base**       | CANON-v1.1                                 |

---

## Summary

Emergency canon update issued in response to the EU loot box regulatory notice
(DRIFT-20260309-001). Revises the monetization framework to mandate a
loot-box-to-direct-purchase transition for EU markets. Introduces the kill
switch policy for pricing changes. Formally acknowledges a contradiction
between the "player-first monetization" pledge and the operational reality
of the emergency pivot.

This is the first canon version issued under crisis conditions. Turnaround
from trigger event to ratification: 14 hours.

---

## Diff from CANON-v1.1

### Added

1. **Kill Switch Policy** (New Section 4.5)
   - Any pricing or monetization change that triggers regulatory action OR
     causes refund rates to exceed 200% of the trailing 4-week average can
     be unilaterally rolled back by @monetization-lead or @exec-team.
   - Rollback must be logged as a sev-1 DLR within 1 hour.
   - Post-rollback review required within 48 hours with all five studios.
   - Kill switch was invoked on 2026-03-16 (DRIFT-20260316-001).

2. **EU Monetization Addendum** (New Section 4.6)
   - Loot box mechanics suspended in EU markets effective immediately.
   - All randomized reward mechanics converted to direct-purchase model.
   - Conversion managed by Berlin studio (DLR-20260311-001).
   - Revenue impact modeled at -$12M/month EU until direct-purchase
     conversion rate stabilizes (ASM-0011 targets >60% of loot box revenue).

3. **Canon Contradiction Acknowledgment** (New Section 7)
   - The "player-first monetization" pledge (public-commitments.md,
     Commitment 1) states: "We will never gate gameplay progression
     behind a paywall."
   - The emergency loot-box removal, while player-protective in intent,
     was perceived by segments of the community as an admission that
     prior monetization violated the pledge.
   - DRIFT-20260311-001 logged this as a canon contradiction.
   - Resolution: the pledge is reaffirmed. The direct-purchase model is
     positioned as an improvement, not a correction. Comms plan:
     DLR-20260311-002.

### Modified

4. **Monetization Framework** (Section 4, updated)
   - Loot box mechanics: status changed from "permitted with regional
     compliance review" to "suspended in EU; under review globally."
   - Executive sign-off threshold lowered: any monetization change affecting
     >5% of revenue requires @exec-team approval (previously 15%).

### Unchanged

- Mission canon (Section 1) -- no changes.
- Technical architecture (Section 2) -- no changes.
- Tournament rules (Section 3) -- no changes (Invitational concluded).
- Localization standard (Section 5.4) -- no changes (addressed in v1.3).

---

## Rationale

On 2026-03-09, the EU Digital Consumer Rights Authority issued a formal
notice classifying Eclipse Dominion's loot box mechanics as "de facto
gambling under Article 7(b)" of the EU Digital Services Regulation.
AetherForge had 72 hours to demonstrate compliance or face fines of up
to 4% of EU revenue ($7.6M annually).

Simultaneously, the MTX price increase deployed in W10 drove EU churn
to 8.2% (vs. 3% modeled by ASM-0007), refund rates spiked 340%
(DRIFT-20260310-001), and EU DAU dropped 18% (DRIFT-20260310-002).
ARPPU collapsed 31% (DRIFT-20260312-001).

The emergency rollback (DLR-20260309-001) and loot-box conversion
(DLR-20260311-001) were the fastest sev-1 decisions in AetherForge
history. CANON-v1.2 codifies the new monetization reality.

**Financial exposure at time of publication:**
- EU regulatory fine risk: $7.6M/yr
- Refund liability (W11): $3.8M
- Revenue shortfall (annualized): $38M
- Sponsor renegotiation risk: $30M (OrionTel + VantaFuel)
- Total exposure: ~$79.4M

---

## Assumptions Affected

| ASM ID   | Description                              | Status      |
|----------|------------------------------------------|-------------|
| ASM-0004 | Battle Pass ARPPU $14.50 baseline        | under review|
| ASM-0007 | EU churn model valid through Q1          | expired     |
| ASM-0011 | Direct purchase conversion >60% loot box | new, active |

---

## Canon Linkage

- **Supersedes:** CANON-v1.1
- **Superseded by:** CANON-v1.3
- **Linked DLRs:** DLR-20260309-001, DLR-20260311-001, DLR-20260311-002
- **Linked Drifts:** DRIFT-20260309-001, DRIFT-20260310-001, DRIFT-20260310-002,
  DRIFT-20260311-001, DRIFT-20260312-001
- **MASTER_INDEX Row:** 89
