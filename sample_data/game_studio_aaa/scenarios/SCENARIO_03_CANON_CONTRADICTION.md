# Scenario 03: When Canon Breaks

> **Window:** W11--W12 (2026-03-09 through 2026-03-20)
> **Severity:** high (sustained)
> **Root Trigger:** DRIFT-20260311-001 (Canon contradiction: monetization ethics)
> **Secondary Trigger:** DRIFT-20260320-001 (Narrative localization divergence JP vs EN)
> **Canon Versions Issued:** 2 (CANON-v1.2, CANON-v1.3)
> **Financial Impact:** $3.2M localization rework, NPS drop quantified

---

## Overview

This scenario documents what happens when an organization's institutional memory
-- its canon -- contradicts itself under crisis pressure. Unlike Scenarios 01
and 02, which are infrastructure and financial cascades respectively, Scenario 03
is a governance cascade: the system of record that is supposed to provide
coherence itself becomes incoherent.

Two distinct canon failures occurred in rapid succession:

1. **The monetization contradiction (W11).** AetherForge's "player-first
   monetization" pledge -- published in press releases, investor calls, and
   community posts -- was contradicted by the emergency loot-box-to-direct-purchase
   pivot. The pivot was player-protective in intent, but its existence implied
   that prior monetization practices violated the pledge. DRIFT-20260311-001
   flagged this as a canon contradiction.

2. **The localization divergence (W12).** Emergency patches deployed during W10
   (esports spike) and W11 (monetization backlash) bypassed the localization
   review pipeline. The Japanese client fell two canon versions behind (running
   CANON-v1.1 content while EN was on CANON-v1.3), with 47 strings diverged
   across 12 quest lines. Different players in different regions were
   experiencing different canonical realities.

Together, these failures demonstrate that canon is not a static document -- it
is a living system that must evolve under crisis pressure without losing
coherence. The rapid succession of CANON-v1.2 and CANON-v1.3 (issued 7 days
apart) was both the symptom and the treatment.

---

## Timeline

| Date       | Event | ID |
|------------|-------|----|
| 2026-03-09 | EU regulatory notice triggers emergency MTX rollback | DRIFT-20260309-001 |
| 2026-03-09 | CANON-v1.2 ratified: monetization framework rewritten | CANON-v1.2 |
| 2026-03-09 | Emergency localization sync reveals JP/KR gaps | DLR-20260309-002 |
| 2026-03-10 | Localization divergence correction policy drafted | DLR-20260309-003 |
| 2026-03-11 | Canon contradiction formally flagged | DRIFT-20260311-001 |
| 2026-03-11 | Loot box conversion to direct purchase begins | DLR-20260311-001 |
| 2026-03-11 | Pay-to-win allegation response plan activated | DLR-20260311-002 |
| 2026-03-13 | Patch cadence SLA breached (localization bottleneck contributing) | DRIFT-20260313-001 |
| 2026-03-16 | Kill switch invoked on residual MTX pricing | DRIFT-20260316-001 |
| 2026-03-16 | CANON-v1.3 ratified: localization policy and pricing parity | CANON-v1.3 |
| 2026-03-17 | Cross-region pricing parity drift detected (NA vs EU) | DRIFT-20260317-001 |
| 2026-03-19 | Warsaw QA pipeline bottleneck from localization backlog | DRIFT-20260319-001 |
| 2026-03-20 | JP localization divergence formally documented | DRIFT-20260320-001 |
| 2026-03-20 | Lore consistency framework ratified | DLR-20260320-001 |
| 2026-03-20 | Automated regression gate for patches ratified | DLR-20260320-002 |

---

## Key Decisions

| DLR | Title | Studio | Canon Impact |
|-----|-------|--------|--------------|
| DLR-20260309-001 | Emergency MTX rollback EU | Berlin | Triggered CANON-v1.2; rewrote monetization framework |
| DLR-20260309-002 | Emergency localization sync | Berlin + Warsaw | Discovered JP divergence; triggered CANON-v1.3 localization addenda |
| DLR-20260309-003 | Localization divergence correction policy | Montreal | Established process for multi-version localization gaps |
| DLR-20260311-001 | Loot box conversion to direct purchase | Berlin | Operationalized CANON-v1.2 EU monetization addendum |
| DLR-20260320-001 | Lore consistency framework | Montreal | Canon-level policy: all narrative changes require editorial review |
| DLR-20260320-002 | Automated regression gate | Warsaw | Technical enforcement of canon-diff in CI/CD pipeline |

---

## Drift Cascade: The Contradiction Chain

```
DRIFT-20260309-001  EU regulatory notice
  |
  +-> CANON-v1.2 issued (emergency, 14h turnaround)
  |     |
  |     +-> DRIFT-20260311-001  Canon contradiction: "player-first" pledge
  |           vs. emergency monetization pivot
  |
  +-> DLR-20260309-002  Emergency localization sync
        |
        +-> DRIFT-20260320-001  JP localization divergence discovered
        |     |
        |     +-> CANON-v1.3 issued (localization policy overhaul)
        |
        +-> DRIFT-20260319-001  Warsaw QA pipeline bottleneck
```

```
DRIFT-20260316-001  Kill switch invoked on residual MTX pricing
  |
  +-> DRIFT-20260317-001  Cross-region pricing parity drift (NA vs EU)
```

The contradiction chain is qualitatively different from the infrastructure
and financial cascades in Scenarios 01 and 02. Here, the drift signals are
not about systems failing -- they are about the governing documents themselves
becoming inconsistent. The "fix" is not a hotfix or a rollback; it is a
canon revision.

---

## The Monetization Contradiction (Deep Dive)

**The pledge (public-commitments.md, Commitment 1):**
> "Eclipse Dominion will never sell competitive advantage. Every item available
> for purchase is cosmetic-only."

**The reality:**
The loot box mechanics, while cosmetic-only, were classified by the EU DCRA as
"de facto gambling." The emergency removal of loot boxes was the right decision,
but it created an implicit admission: if loot boxes needed to be removed for
player protection, were they ever compatible with the "player-first" pledge?

**Community response:**
- Reddit megathread: 14,000 upvotes, 3,200 comments (68% negative sentiment)
- Twitter/X: "AetherForge admits loot boxes were predatory" trending for 18h
- Content creator coverage: 23 videos with >100K views, 78% critical

**CANON-v1.2 resolution:**
Section 7 (Canon Contradiction Acknowledgment) took an unusual approach: rather
than revising the pledge, it acknowledged the contradiction transparently and
reframed the direct-purchase model as an improvement. This was a deliberate
governance choice -- erasing the contradiction would have undermined the canon's
credibility as a system of record.

**Comms effectiveness (contested):**
CLAIM-0007 asserts the comms response plan reduced negative sentiment by 25%.
This claim is contested because the sentiment measurement window overlaps with
organic attention decay. True attribution is uncertain.

---

## The Localization Divergence (Deep Dive)

**Root cause:** The emergency hotfix bypass protocol (DLR-20260306-002) created
a fast-track deployment path during the Apex Invitational (W10). The bypass was
invoked 4 times in 10 days across W10-W11. None of the 4 invocations included
a localization checkpoint because the protocol did not require one.

**Scale of divergence:**

| Metric | Value |
|--------|-------|
| Diverged strings (JP) | 47 |
| Affected quest lines | 12 |
| Canon version gap | JP on v1.1, EN on v1.3 (2 versions behind) |
| KR divergence | 23 strings, 6 quest lines (secondary) |
| Discovery date | 2026-03-20 (11 days after first bypass) |

**Player impact (JP):**

| Metric | Before (W10) | After (W12) | Delta |
|--------|-------------|-------------|-------|
| JP NPS | +31 | +9 | -22 pts |
| JP DAU | 186K | 172K | -7.5% |
| JP support tickets (lore) | 12/day | 89/day | +642% |
| JP refund rate | 1.2% | 3.8% | +217% |

**Systemic lesson:** The JP divergence was not a localization failure -- it was
a governance failure. The bypass protocol created a structural gap in the
canon enforcement pipeline. Every emergency patch that modified player-facing
strings was technically correct in EN but canonically invalid in JP. The players
experiencing the JP client were living in a different narrative reality.

---

## Financial Impact

| Category | Amount | Notes |
|----------|--------|-------|
| JP localization rework | $1.4M | 47 strings, 12 quest lines, includes VO re-recording for 6 strings |
| KR localization rework | $0.6M | 23 strings, 6 quest lines |
| Pricing parity audit | $0.3M | Cross-region pricing analysis and adjustment |
| JP NPS recovery campaign | $0.9M | Community events, exclusive cosmetics, dev stream apology |
| Canon-diff tooling development | $0.4M | Warsaw CI/CD integration |
| **Total** | **$3.2M** | Localization and governance rework |

**Indirect costs (not separately quantified):**
- Warsaw QA pipeline backlog: +180 tickets (DRIFT-20260319-001), estimated
  2-sprint recovery.
- Montreal editorial bandwidth consumed by emergency canon revisions: ~120
  person-hours across W11-W12.
- Cross-studio coordination overhead for CANON-v1.2 and v1.3 ratification:
  ~80 person-hours across 5 studios.

---

## Lessons Learned

1. **Canon must version gracefully under pressure.** Two canon versions in 7
   days is a symptom of crisis, but the rapid versioning itself was correct.
   The alternative -- delaying CANON-v1.3 to bundle it with v1.2 -- would have
   left the JP divergence unaddressed for an additional week. Speed of canon
   evolution must match the speed of operational reality.

2. **Contradictions should be acknowledged, not hidden.** CANON-v1.2 Section 7
   set a precedent: when canon contradicts itself, the system of record must
   say so explicitly. Hiding contradictions erodes trust in the canon itself,
   which is more damaging than the contradiction.

3. **Every bypass path must include every enforcement gate.** The emergency
   hotfix bypass protocol lacked a localization checkpoint because localization
   was considered "non-critical" during infrastructure emergencies. But canon
   coherence is always critical. CANON-v1.4 amends the bypass protocol to
   include mandatory localization notification.

4. **Canon-diff tooling is infrastructure, not nice-to-have.** The 47-string
   JP divergence was discoverable by automated tooling. Canon-diff could have
   flagged the gap within hours of the first bypass deployment. Instead, it
   was discovered 11 days later by a localization QA engineer reviewing
   player complaints. The $0.4M tooling investment prevents the $2.0M
   rework cost.

5. **NPS is a lagging indicator of canon coherence.** The JP NPS drop (-22
   points) was measurable only after players had experienced the divergence
   for 11 days. By the time NPS moved, the damage was already embedded.
   Canon-diff provides a leading indicator that would have fired on Day 1.

---

## Cross-References

| Type | IDs |
|------|-----|
| DLRs | DLR-20260309-001, DLR-20260309-002, DLR-20260309-003, DLR-20260311-001, DLR-20260311-002, DLR-20260320-001, DLR-20260320-002 |
| Drifts | DRIFT-20260309-001, DRIFT-20260311-001, DRIFT-20260316-001, DRIFT-20260317-001, DRIFT-20260319-001, DRIFT-20260320-001 |
| Assumptions | ASM-0014 (JP resync in 1 sprint) |
| Claims | CLAIM-0007 (comms reduces sentiment 25%, contested) |
| Canon | CANON-v1.2, CANON-v1.3 (both issued during this scenario) |
| Telemetry | TELEMETRY-W11, TELEMETRY-W12 |
| Evidence | EVID-0005 (Warsaw QA pipeline throughput analysis) |
| Scenarios | Preceded by SCENARIO_01 (bypass protocol origin) and SCENARIO_02 (monetization trigger) |
