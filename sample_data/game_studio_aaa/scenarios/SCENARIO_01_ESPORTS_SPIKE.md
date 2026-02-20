# Scenario 01: The Apex Invitational Cascade

> **Window:** W10 (2026-03-02 through 2026-03-06)
> **Severity:** sev-1
> **Root Trigger:** DRIFT-20260302-001 (Tournament CCU exceeded projections 340%)
> **Cascade Depth:** 6 drift signals from single root event
> **Emergency DLRs:** 5
> **Financial Exposure:** $4.2M direct, $30M sponsor risk

---

## Overview

The Eclipse Dominion Apex Invitational was the flagship competitive event of
Season 4: $2.5M prize pool, 32 professional teams, 4-day broadcast window
across NA, EU, and APAC time zones. It was supposed to be AetherForge's
biggest esports moment. Instead, it became the trigger event for the worst
operational cascade in the company's history.

The root cause was a single invalidated assumption: ASM-0005 projected peak
tournament CCU at 620K. Actual peak CCU reached 2.1M -- a 340% overshoot.
The auto-scaling infrastructure, designed for a world where 800K was the
ceiling (ASM-0001), could not absorb the spike within its 3-minute warm-up
window. What followed was a 6-event drift cascade that touched infrastructure,
matchmaking, competitive fairness, and sponsor relations across all five
studios in under 96 hours.

---

## Timeline

| Date       | Time (UTC) | Event | Severity | ID |
|------------|------------|-------|----------|----|
| 2026-03-02 | 14:00      | Invitational Day 1 broadcast begins (NA window) | -- | -- |
| 2026-03-02 | 14:22      | CCU crosses 800K; auto-scaler initiates burst | -- | -- |
| 2026-03-02 | 14:31      | CCU reaches 1.15M; auto-scaler lag detected | sev-1 | DRIFT-20260302-001 |
| 2026-03-02 | 14:45      | Matchmaking queue times spike to 4m 12s (normal: 45s) | high | DRIFT-20260302-002 |
| 2026-03-02 | 16:00      | Peak CCU: 2.1M. US-East at 98% capacity. | sev-1 | -- |
| 2026-03-02 | 18:30      | Emergency scaling plan ratified | sev-1 | DLR-20260302-001 |
| 2026-03-02 | 19:15      | Tournament dedicated servers provisioned (Tokyo) | sev-1 | DLR-20260302-002 |
| 2026-03-03 | 02:00      | OrionTel sponsor uptime clause flagged (99.5% SLA at risk) | high | DRIFT-20260303-001 |
| 2026-03-03 | 09:00      | Tournament balance patch freeze ratified | high | DLR-20260302-003 |
| 2026-03-04 | 06:30      | APAC broadcast window: Tokyo P95 latency hits 142ms (SLA: 80ms) | sev-1 | DRIFT-20260304-001 |
| 2026-03-04 | 08:00      | Latency compensation algorithm hotfix deployed (Tokyo) | sev-1 | DLR-20260304-001 |
| 2026-03-04 | 14:00      | Competitive integrity reporting system activated | high | DLR-20260304-002 |
| 2026-03-05 | 10:00      | 1,200+ competitive fairness complaints logged | high | DRIFT-20260305-001 |
| 2026-03-05 | 14:00      | SAI spikes to 82 (threshold for executive escalation: 75) | sev-1 | DRIFT-20260305-002 |
| 2026-03-06 | 06:00      | VantaFuel suspends sponsorship discussions pending review | sev-1 | DRIFT-20260306-001 |
| 2026-03-06 | 09:00      | Auto-scaling threshold adjustment ratified | high | DLR-20260306-001 |
| 2026-03-06 | 10:30      | Emergency hotfix bypass protocol established | sev-1 | DLR-20260306-002 |
| 2026-03-06 | 14:00      | Cross-region matchmaking rebalance deployed | high | DLR-20260306-003 |
| 2026-03-06 | 16:00      | Competitive fairness protest response issued | high | DLR-20260306-004 |
| 2026-03-06 | 22:00      | Invitational concludes. CCU stabilizes at 680K. | -- | -- |

---

## Key Decisions

| DLR | Title | Studio | Impact |
|-----|-------|--------|--------|
| DLR-20260302-001 | Tournament infrastructure scaling plan | LA + Tokyo | Authorized emergency capacity procurement: $1.8M |
| DLR-20260302-002 | Tournament dedicated server provisioning | Tokyo | Spun up 340 dedicated tournament servers in APAC-NE |
| DLR-20260302-003 | Tournament balance patch freeze | Montreal | Froze all balance changes through tournament + 24h cooldown |
| DLR-20260304-001 | Latency compensation algorithm update APAC | Tokyo | Hotfixed APAC netcode; reduced P95 from 142ms to 91ms |
| DLR-20260306-001 | Auto-scaling threshold adjustment | LA | Revised burst threshold from 40% -> 90% to 40% -> 95% with 60s pre-warm |
| DLR-20260306-002 | Emergency hotfix bypass protocol | LA | Created fast-track deployment path (later amended in CANON-v1.4) |
| DLR-20260306-003 | Cross-region matchmaking rebalance | Tokyo + LA | Re-weighted region routing to balance load across US-East and APAC-NE |
| DLR-20260306-004 | Competitive fairness protest response | LA | Public statement + 1,200 case reviews; 340 compensation grants |

---

## Drift Cascade

```
ASM-0005 invalidated (620K CCU projection vs 2.1M actual)
  |
  +-> DRIFT-20260302-001  CCU 340% over projection
  |     |
  |     +-> DRIFT-20260302-002  Matchmaking queue time spike (4m 12s)
  |     |
  |     +-> DRIFT-20260304-001  APAC latency >120ms (actual: 142ms P95)
  |     |     |
  |     |     +-> DRIFT-20260305-001  Competitive fairness complaints (1,200+)
  |     |           |
  |     |           +-> DRIFT-20260305-002  SAI spike to 82
  |     |
  |     +-> DRIFT-20260303-001  OrionTel sponsor uptime clause at risk
  |           |
  |           +-> DRIFT-20260306-001  VantaFuel sponsor suspension threat
```

Six drift signals cascaded from a single root event in 96 hours. Each
signal compounded the severity of the next. The SAI (Stakeholder Anxiety
Index) hit 82 -- the highest recorded value in Eclipse Dominion history --
because infrastructure, competitive fairness, and sponsor relations were
all degraded simultaneously.

---

## Financial Impact

| Category | Amount | Notes |
|----------|--------|-------|
| Emergency infrastructure procurement | $1.8M | 340 dedicated servers + burst capacity |
| Latency compensation engineering | $0.6M | Tokyo team overtime + vendor support |
| Competitive fairness compensation | $0.5M | 340 grants to affected players |
| Matchmaking rebalance engineering | $0.3M | Cross-studio war room (4 days) |
| Esports broadcast overrun | $0.2M | Extended broadcast windows + re-streams |
| PR and communications | $0.1M | Emergency press response |
| **Direct Cost** | **$3.5M** | |
| Sponsor contract exposure (OrionTel) | $18M/yr | 99.5% uptime clause breached |
| Sponsor contract exposure (VantaFuel) | $12M/yr | Suspended discussions pending review |
| **Sponsor Risk** | **$30M/yr** | Renegotiated in W12; $4.2M penalty paid |
| **Total Exposure** | **$34.2M** | Direct + worst-case sponsor |

---

## Lessons Learned

1. **Assumption ASM-0005 was structurally flawed.** The 620K projection used
   Season 3 tournament data without accounting for the Season 4 content drop,
   the $2.5M prize pool (3x previous), or the APAC broadcast expansion.
   Post-mortem estimated fair projection: 1.4M--1.8M CCU.

2. **Auto-scaling warm-up was too slow.** The 3-minute warm-up window was
   adequate for organic growth but not for event-driven spikes. Revised to
   60-second pre-warm with tournament-profile pre-provisioning (DLR-20260306-001).

3. **Cross-region matchmaking had no surge mode.** Region-router treated each
   region independently. When US-East saturated, overflow traffic hit APAC-NE
   without capacity awareness. DLR-20260306-003 added cross-region load balancing.

4. **Sponsor SLA monitoring was passive.** OrionTel and VantaFuel clauses were
   buried in legal documents. No automated alerting existed for sponsor SLA
   thresholds. Post-incident: sponsor SLA dashboards added to ops monitoring.

5. **SAI is a useful leading indicator.** The SAI spike to 82 preceded the
   VantaFuel suspension threat by 24 hours. Earlier SAI-based escalation
   could have compressed the response timeline.

---

## Cross-References

| Type | IDs |
|------|-----|
| DLRs | DLR-20260302-001, DLR-20260302-002, DLR-20260302-003, DLR-20260304-001, DLR-20260304-002, DLR-20260306-001, DLR-20260306-002, DLR-20260306-003, DLR-20260306-004 |
| Drifts | DRIFT-20260302-001, DRIFT-20260302-002, DRIFT-20260303-001, DRIFT-20260304-001, DRIFT-20260305-001, DRIFT-20260305-002, DRIFT-20260306-001 |
| Assumptions | ASM-0001 (strained), ASM-0005 (expired), ASM-0008 (held) |
| Claims | CLAIM-0004 (balance freeze preserved integrity), CLAIM-0005 (sponsor renegotiation) |
| Canon | CANON-v1.1 (active during event) |
| Telemetry | TELEMETRY-W10 |
| Scenarios | Feeds into SCENARIO_02 (monetization backlash, SAI sustained at 82) |
