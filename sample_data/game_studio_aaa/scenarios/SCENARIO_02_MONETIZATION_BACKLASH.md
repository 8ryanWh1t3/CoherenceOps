# Scenario 02: The EU Price Shock

> **Window:** W11 (2026-03-09 through 2026-03-13)
> **Severity:** sev-1
> **Root Trigger:** DRIFT-20260309-001 (EU loot box regulatory notice)
> **Cascade Depth:** 6 drift signals, 2 parallel chains
> **Emergency DLRs:** 6
> **Financial Exposure:** $38M annualized revenue shortfall, $11.5M refund/penalty

---

## Overview

Three days after the Apex Invitational concluded, a second crisis hit AetherForge
from an entirely different vector. The EU Digital Consumer Rights Authority issued
a formal notice classifying Eclipse Dominion's loot box mechanics as "de facto
gambling under Article 7(b)" of the EU Digital Services Regulation. AetherForge
had 72 hours to demonstrate compliance or face fines up to 4% of EU annual revenue.

The regulatory notice landed on a player base already stressed by the Invitational
infrastructure failures. Within 48 hours, a perfect storm of regulatory pressure,
community backlash, and financial contagion produced the most expensive week in
Eclipse Dominion's operating history.

The monetization backlash invalidated two key assumptions (ASM-0004, ASM-0007),
exposed a structural error in the EU churn model, and forced AetherForge to
execute a loot-box-to-direct-purchase pivot in EU markets under extreme time
pressure. It also triggered the first canon contradiction in CoherenceOps
history (DRIFT-20260311-001).

---

## Timeline

| Date       | Time (UTC) | Event | Severity | ID |
|------------|------------|-------|----------|----|
| 2026-03-09 | 08:00      | EU DCRA formal notice received by legal (Berlin) | sev-1 | DRIFT-20260309-001 |
| 2026-03-09 | 09:30      | Berlin initiates emergency MTX rollback | sev-1 | DLR-20260309-001 |
| 2026-03-09 | 10:00      | Emergency localization sync triggered | sev-1 | DLR-20260309-002 |
| 2026-03-09 | 14:00      | CANON-v1.2 ratified (14h turnaround) | -- | CANON-v1.2 |
| 2026-03-09 | 18:00      | EU MTX price increase reverted server-side | -- | -- |
| 2026-03-10 | 06:00      | EU refund rate spikes +340% WoW | sev-1 | DRIFT-20260310-001 |
| 2026-03-10 | 10:00      | Localization divergence correction policy initiated | high | DLR-20260309-003 |
| 2026-03-10 | 14:00      | EU DAU drops 18% (420K -> 344K) | high | DRIFT-20260310-002 |
| 2026-03-11 | 08:00      | Loot box conversion to direct purchase begins | sev-1 | DLR-20260311-001 |
| 2026-03-11 | 10:00      | Canon contradiction flagged: player-first pledge vs reality | high | DRIFT-20260311-001 |
| 2026-03-11 | 12:00      | Pay-to-win allegation response plan activated | high | DLR-20260311-002 |
| 2026-03-12 | 08:00      | EU ARPPU collapses 31% | sev-1 | DRIFT-20260312-001 |
| 2026-03-13 | 06:00      | Patch cadence SLA breached: 48h target -> 96h actual | high | DRIFT-20260313-001 |
| 2026-03-13 | 10:00      | Sponsor renegotiation triggered (cascade from W10) | sev-1 | DRIFT-20260313-002 |
| 2026-03-13 | 11:00      | Patch cadence SLA revision ratified | high | DLR-20260313-001 |
| 2026-03-13 | 14:00      | Ranked mode fairness audit initiated | medium | DLR-20260313-002 |
| 2026-03-13 | 15:00      | Cross-studio hotfix cadence alignment | high | DLR-20260313-003 |

---

## Key Decisions

| DLR | Title | Studio | Impact |
|-----|-------|--------|--------|
| DLR-20260309-001 | Emergency MTX rollback EU | Berlin | Reverted all W10 pricing changes in EU; $3.8M refund authorization |
| DLR-20260309-002 | Emergency localization sync | Berlin + Warsaw | Triggered cross-region string audit; discovered 47-string JP divergence |
| DLR-20260309-003 | Localization divergence correction policy | Montreal | Established policy for handling multi-version localization gaps |
| DLR-20260311-001 | Loot box conversion to direct purchase EU | Berlin | Converted all randomized rewards to direct purchase; 68% catalog coverage by W12 |
| DLR-20260311-002 | Pay-to-win allegation response plan | LA | Public comms strategy; negative sentiment reduced ~25% (CLAIM-0007, contested) |
| DLR-20260313-001 | Patch cadence SLA revision | LA | Acknowledged 48h SLA breach; revised to tiered SLA (sev-1: 24h, sev-2: 48h, sev-3: Patch Tuesday) |

---

## Drift Cascade

```
DRIFT-20260309-001  EU loot box regulatory notice
  |
  +-> DRIFT-20260310-001  MTX refund rate spike EU +340%
  |     |
  |     +-> DRIFT-20260310-002  DAU drop EU -18% (420K -> 344K)
  |           |
  |           +-> DRIFT-20260312-001  ARPPU collapse EU -31%
  |
  +-> DRIFT-20260311-001  Canon contradiction: monetization ethics
  |
  +-> DRIFT-20260313-001  Patch cadence SLA breached (48h -> 96h)
        |
        +-> DRIFT-20260313-002  Sponsor renegotiation triggered (cascade from W10)
```

Two parallel chains radiated from the regulatory notice: a financial chain
(refunds -> DAU loss -> ARPPU collapse) and an operational chain (patch SLA
breach -> sponsor renegotiation). The canon contradiction (DRIFT-20260311-001)
was a standalone governance signal that did not cascade further but required
the emergency CANON-v1.2 update.

---

## Assumption Invalidation

| ASM ID   | Original Claim | Actual | Gap | Consequence |
|----------|---------------|--------|-----|-------------|
| ASM-0004 | Battle Pass ARPPU $14.50 | EU ARPPU dropped to $10.01 (-31%) | $4.49/user | Revenue model invalid for EU; pricing rebalance required |
| ASM-0007 | EU churn model valid through Q1 | 8.2% churn (modeled: 3.0%) | +5.2 ppt | Model missed regulatory/sentiment tail risk; structural rebuild needed |

The churn model (ASM-0007) was the more consequential failure. It had been
validated against 18 months of organic churn data but had never been stress-tested
against a regulatory shock or a community backlash event. The model treated
churn as a function of price sensitivity alone, ignoring sentiment, trust,
and regulatory risk as input variables.

Post-mortem recommendation: churn models must include a sentiment multiplier
derived from community NPS and a regulatory risk factor derived from the
compliance team's jurisdiction tracker.

---

## Financial Impact

| Category | Amount | Notes |
|----------|--------|-------|
| EU refund processing (W11) | $3.8M | 340% spike; 42,000 refund requests processed |
| Regulatory penalty reserve | $7.6M/yr | 4% of EU revenue; reserved pending DCRA resolution |
| EU ARPPU collapse (annualized) | $38M | -31% ARPPU across 344K EU DAU base |
| Direct-purchase conversion engineering | $2.1M | Berlin + Warsaw sprint costs |
| PR and comms (response plan) | $0.4M | DLR-20260311-002 execution |
| Legal fees (DCRA response) | $0.8M | External counsel + compliance audit |
| **Refund/Penalty Exposure** | **$11.5M** | W11 direct exposure |
| **Annualized Revenue Shortfall** | **$38M** | EU ARPPU at -31% (recovering) |
| **Total W11 Exposure** | **$49.5M** | Direct + annualized |

Recovery trajectory (as of W13): EU ARPPU recovering at +3.2% WoW.
Direct-purchase conversion at 72% of prior loot box revenue (ASM-0011
target: 60%). Full recovery projected by W18 under optimistic scenario,
W24 under conservative scenario.

---

## Lessons Learned

1. **Regulatory risk was unpriced.** AetherForge had no regulatory risk model.
   The EU loot box classification had been discussed in industry forums for
   18 months, but no assumption or claim tracked the probability of enforcement.
   Post-incident: @monetization-lead now maintains a jurisdiction-level
   regulatory risk register.

2. **Churn models must include non-price variables.** ASM-0007 modeled churn
   as f(price) when the actual function was f(price, sentiment, trust, regulatory).
   The 8.2% actual vs. 3.0% modeled gap was entirely attributable to sentiment
   and trust erosion. Post-incident: churn model rebuilt with NPS and SAI inputs.

3. **Kill switch policy should have existed before the crisis.** The MTX rollback
   (DLR-20260309-001) required ad-hoc executive authorization. The kill switch
   policy (CANON-v1.2, Section 4.5) was written after the fact. If the policy
   had existed, rollback could have been executed 4 hours faster.

4. **Canon contradictions are governance signals, not failures.** The
   "player-first monetization" contradiction (DRIFT-20260311-001) was initially
   treated as a PR crisis. In hindsight, it was a signal that the canon needed
   to evolve. CANON-v1.2's formal acknowledgment set a precedent for how
   institutional memory handles self-contradiction.

5. **Cross-studio coordination overhead is a hidden cost.** The patch SLA breach
   (48h -> 96h) was not caused by engineering complexity but by the time required
   to coordinate Berlin (monetization), LA (ops), Warsaw (QA), and Montreal
   (narrative review) across time zones during a crisis. DLR-20260313-003
   (cross-studio hotfix cadence alignment) addresses this structurally.

---

## Cross-References

| Type | IDs |
|------|-----|
| DLRs | DLR-20260309-001, DLR-20260309-002, DLR-20260309-003, DLR-20260311-001, DLR-20260311-002, DLR-20260313-001, DLR-20260313-002, DLR-20260313-003 |
| Drifts | DRIFT-20260309-001, DRIFT-20260310-001, DRIFT-20260310-002, DRIFT-20260311-001, DRIFT-20260312-001, DRIFT-20260313-001, DRIFT-20260313-002 |
| Assumptions | ASM-0004 (under review), ASM-0007 (expired), ASM-0011 (new) |
| Claims | CLAIM-0006 (direct purchase maintains 70% revenue), CLAIM-0007 (comms reduces sentiment 25%, contested) |
| Canon | CANON-v1.2 (issued during event) |
| Telemetry | TELEMETRY-W11 |
| Evidence | EVID-0003 (EU regulatory notice scan and legal memo) |
| Scenarios | Preceded by SCENARIO_01 (SAI carried over); feeds into SCENARIO_03 (canon contradiction) |
