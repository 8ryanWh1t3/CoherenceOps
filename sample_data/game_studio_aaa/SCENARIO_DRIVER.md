# Scenario Driver -- AetherForge Interactive

## Loading This Pack

Copy the pack into your CoherenceOps coherence root (training mode):

```bash
cp -r sample_data/game_studio_aaa/* coherence/
```

No configuration changes required. CoherenceOps discovers records from the standard directory layout and `MASTER_INDEX.csv`.

---

## PR Demo Actions

Use these to exercise CoherenceOps PR checks against common coherence violations:

| Violation | How to Trigger | Expected Check Failure |
|---|---|---|
| **Major PR missing DLR** | Open a PR that touches matchmaking config without referencing any DLR | `coherence/dlr-required`: no DLR linked for config change |
| **Canon change missing changelog** | Edit a canon file (e.g., `canon/versions/CANON-v1.3.yaml`) without updating the changelog field | `coherence/canon-changelog`: canon version modified without changelog entry |
| **Expired assumption** | Reference `ASM-0005` in a PR body | `coherence/asm-expired`: ASM-0005 expired 2026-03-08, must renew or retire |

---

## Key Demo Records

| ID | Title | Why It Matters |
|---|---|---|
| `DLR-20260309-001` | Emergency MTX rollback EU | Sev-1 monetization decision with regulatory pressure; links to 5+ drift events |
| `DRIFT-20260302-001` | Tournament CCU exceeded projections 340% | Cascade trigger for latency, matchmaking, and sponsor drift |
| `ASM-0005` | Tournament CCU assumption | Expired assumption -- any reference triggers a check failure |
| `DLR-20260228-001` | Patch Tuesday SLA definition | Foundational SLA later breached in W11 (DRIFT-20260313-001) |

---

## 10-Minute Demo Path

Walk through these files in order. Each step builds on the previous.

| Step | Time | Open File / Action | What to Show |
|---|---|---|---|
| 1 | 0:00 | `MASTER_INDEX.csv` | Overview: 100 records, 7 types, 5 weeks. Filter by `sev-1` to show 6 critical drifts. |
| 2 | 1:00 | `decisions/DLR-20260228-001.yaml` | Patch Tuesday SLA -- baseline decision. Note the `assumptions:` field referencing ASM-0003. |
| 3 | 2:00 | `intel/provenance/ASM-0005.yaml` | Tournament CCU assumption. Show `status: expired`, `expiry: 2026-03-08`. |
| 4 | 3:00 | `drift/DRIFT-20260302-001.yaml` | CCU spike 340%. Show `triggered_by: ASM-0005 invalidation`, `severity: sev-1`. |
| 5 | 4:00 | `drift/DRIFT-20260304-001.yaml` | APAC latency cascade. Show `upstream: DRIFT-20260302-001` -- drift chaining. |
| 6 | 5:00 | `drift/DRIFT-20260305-002.yaml` | SAI spike to 82. Show how Stakeholder Anxiety Index aggregates from multiple drifts. |
| 7 | 6:00 | `decisions/DLR-20260309-001.yaml` | Emergency MTX rollback. Show `triggered_by:` linking DRIFT-20260309-001 (EU regulatory) and DRIFT-20260310-001 (refund spike). |
| 8 | 7:30 | `canon/versions/CANON-v1.2.yaml` | Canon snapshot W11. Show monetization policy change and narrative divergence flags. |
| 9 | 8:30 | `drift/DRIFT-20260320-001.yaml` | Narrative localization divergence JP vs EN. Show `canon_conflict: true`. |
| 10 | 9:30 | `MASTER_INDEX.csv` | Return to index. Filter `status=open` or `status=in_progress` to show 7 unresolved items entering W14. Summarize: 3 scenarios, 6 sev-1 events, 35 decisions, 25 drifts. |

---

## Scenarios

### Scenario 1: Esports Spike (W10, Mar 2--8)

**Trigger:** Eclipse Dominion Invitational tournament launches. CCU exceeds projections by 340%.

**Cascade chain:**
```
ASM-0005 (CCU assumption) invalidated
  -> DRIFT-20260302-001  CCU 340% over projection
    -> DRIFT-20260302-002  Matchmaking queue time spike
    -> DRIFT-20260304-001  APAC latency >120ms
      -> DRIFT-20260305-001  Competitive fairness complaints
        -> DRIFT-20260305-002  SAI spike to 82
    -> DRIFT-20260303-001  OrionTel sponsor uptime clause at risk
      -> DRIFT-20260306-001  VantaFuel sponsor suspension threat
```

**Decisions triggered:**
- DLR-20260302-001: Tournament infrastructure scaling plan
- DLR-20260302-002: Tournament dedicated server provisioning
- DLR-20260302-003: Tournament balance patch freeze
- DLR-20260304-001: Latency compensation algorithm update APAC
- DLR-20260304-002: Competitive integrity reporting system
- DLR-20260306-001 through DLR-20260306-004: Emergency response cluster

**Key metrics:**
- Peak CCU: 2.1M (projection: 620K)
- APAC P95 latency: 142ms (SLA: 80ms)
- Matchmaking P50 wait: 4m 12s (normal: 45s)
- SAI peak: 82
- Sponsor contracts at risk: 2 (OrionTel, VantaFuel)

**Resolution:** Auto-scaling thresholds adjusted, APAC edge nodes added, balance patch frozen, sponsor SLAs renegotiated.

---

### Scenario 2: Monetization Backlash (W11, Mar 9--15)

**Trigger:** EU regulatory body issues formal notice on loot box mechanics. Community backlash escalates.

**Cascade chain:**
```
DRIFT-20260309-001  EU loot box regulatory notice
  -> DRIFT-20260310-001  MTX refund rate spike EU +340%
    -> DRIFT-20260310-002  DAU drop EU -18%
      -> DRIFT-20260312-001  ARPPU collapse EU
  -> DRIFT-20260311-001  Canon contradiction monetization ethics
  -> DRIFT-20260313-001  Patch cadence SLA breached 48h->96h
    -> DRIFT-20260313-002  Sponsor renegotiation triggered
```

**Decisions triggered:**
- DLR-20260309-001: Emergency MTX rollback EU (the key demo record)
- DLR-20260309-002: Emergency localization sync
- DLR-20260309-003: Localization divergence correction policy
- DLR-20260311-001: Loot box conversion to direct purchase EU
- DLR-20260311-002: Pay-to-win allegation response plan
- DLR-20260313-001 through DLR-20260313-003: Remediation cluster

**Key metrics:**
- SAI peak: 82 (sustained from Scenario 1)
- EU refund rate: +340% WoW
- EU DAU: -18% (420K -> 344K)
- EU ARPPU: -31%
- Patch SLA breached: 48h target -> 96h actual
- Revenue impact: estimated -$12M/month EU

**Resolution:** MTX rollback via kill switch (DLR-20260309-001), loot boxes converted to direct purchase in EU (DLR-20260311-001), refund policy revised (DLR-20260316-001).

---

### Scenario 3: Canon Contradiction (W12, Mar 16--22)

**Trigger:** Localization team discovers Japanese client narrative diverges from English canon after emergency patches in W10-W11 bypassed localization review.

**Cascade chain:**
```
DRIFT-20260320-001  Narrative localization divergence JP vs EN
  <- DLR-20260309-002  Emergency localization sync (incomplete)
  <- DRIFT-20260316-001  Rollback kill switch invoked MTX
  <- DRIFT-20260317-001  Cross-region pricing parity drift
```

**Decisions triggered:**
- DLR-20260320-001: Lore consistency framework
- DLR-20260320-002: Automated regression gate for patches
- DLR-20260309-003: Localization divergence correction policy (from W11, still in progress)

**Key metrics:**
- JP player NPS: -22 points WoW
- Localization delta: 47 strings diverged across 12 quest lines
- Canon version gap: JP on CANON-v1.1, EN on CANON-v1.3
- QA backlog Warsaw: +180 tickets

**Resolution:** Lore consistency framework established (DLR-20260320-001), automated regression gate added to patch pipeline (DLR-20260320-002), full JP resync scheduled for CANON-v1.4.

---

## Unresolved Items Entering W14

These records remain open or in-progress at the end of the sample window:

| ID | Title | Status |
|---|---|---|
| DRIFT-20260309-001 | EU loot box regulatory notice | in_progress |
| DRIFT-20260310-002 | DAU drop EU -18% | in_progress |
| DRIFT-20260312-001 | ARPPU collapse EU | in_progress |
| DRIFT-20260313-002 | Sponsor renegotiation triggered | in_progress |
| DRIFT-20260317-001 | Cross-region pricing parity drift | in_progress |
| DRIFT-20260319-001 | QA pipeline Warsaw bottleneck | in_progress |
| DRIFT-20260323-001 | Recovery metrics below target D7 retention | open |
| DRIFT-20260325-001 | Residual pricing parity drift LATAM | open |
| DRIFT-20260327-001 | Post-mortem 3 assumptions invalidated | open |

---

## Guided Walkthrough: Esports Spike to Monetization Backlash to Canon Patch

This guided walkthrough takes you through a realistic AAA governance cascade using actual records from the dataset. Each step references real files with real cross-linked IDs. Total time: approximately 10 minutes.

## Step 1 -- Baseline Health (0:00)

**Open:** `telemetry/telemetry_2026-W09.json`

This is Week 9 -- the calm before the storm. Note the key baselines:

| Metric | W09 Value |
|--------|-----------|
| Coherence Score | 88/100 |
| Global DAU | 1,200,000 |
| Global CCU Peak | 420,000 |
| Weekly Revenue | $9.2M |
| EU ARPPU | $14.80 |
| EU Churn | 1.7% |
| SAI (Sentiment) | 34 |
| Patch SLA | 4.2 hours |
| Open Drift Signals | 0 |
| Expired Assumptions | 0 |

Everything is within normal operating bands. No drift signals, all assumptions current. Eclipse Dominion is in steady-state.

**Takeaway:** This is what governance health looks like when the system is working.

---

## Step 2 -- Esports Spike Decision (1:30)

**Open:** `decisions/DLR-20260302-001.md` -- Tournament Infrastructure Scaling Plan

This DLR was created on March 2 when the Eclipse Dominion Championship Series (EDCS) W10 finals approached. The infrastructure team pre-provisioned 3x capacity at a cost of $1.8M. Note:

- **Assumptions referenced:** ASM-0005 ("Peak concurrent users will not exceed 2.5M"), ASM-0002 (session length), ASM-0013 (AWS reserved capacity).
- **Finance section:** $1.8M infrastructure cost vs. $3.5M in sponsor revenue (OrionTel + VantaFuel). Net positive.
- **Kill switch:** Scale-down to 2x if utilization below 40% after 2 hours.

**Now open:** `intel/assumptions.yaml` and find `ASM-0005`.

ASM-0005 states: "Tournament CCU spikes will not exceed 2.0x normal Saturday peak." Status: **expired** (2026-03-02). Blast radius: **high**. Financial exposure: **$22M**.

This assumption was about to be invalidated by reality.

---

## Step 3 -- Drift Trigger (3:00)

**Open:** `drift/DRIFT-20260302-001.md` -- Tournament CCU Exceeded Projections 340%

This is the primary sev-1 cascade trigger. What happened:

| Metric | Expected | Reality |
|--------|----------|---------|
| Peak CCU | 620K | 2.1M (340% over projection) |
| Scaling lag | 0 min | 9 min (AWS burst provisioning) |
| Players affected | 0 | 340,000 degraded, 82,000 disconnected |

**Financial impact:**
- $2.1M in lost MTX revenue during the 9-minute degradation window
- $380K in emergency cloud compute charges
- $4.8M in sponsor contractual risk (OrionTel + VantaFuel uptime clauses triggered)

**Cascade chain:** This single drift triggered 6 downstream drift signals:
- DRIFT-20260302-002 (matchmaking queue spike)
- DRIFT-20260303-001 (OrionTel sponsor clause at risk)
- DRIFT-20260304-001 (APAC latency >120ms)
- DRIFT-20260305-001 (competitive fairness complaints)
- DRIFT-20260305-002 (SAI spike to 82)
- DRIFT-20260306-001 (VantaFuel suspension threat)

---

## Step 4 -- Cascade: Sentiment Breach (4:30)

**Open:** `drift/DRIFT-20260305-002.md` -- SAI Spike to 82

This is a cascade drift -- it was caused by the upstream chain (DRIFT-20260302-001 to DRIFT-20260305-001). The Sentiment Anomaly Index (SAI) hit 82, the highest in Eclipse Dominion history.

Why this matters commercially:
- **VantaFuel clause 4.1** -- instantaneous SAI >80 triggers contract review. **BREACHED** at 82.
- **OrionTel clause 7.2** -- SAI >75 for 48h continuous triggers renegotiation. Approaching threshold.
- **Combined sponsor exposure:** $18.4M/yr at contractual risk.
- **Stock impact:** AetherForge parent company saw a 2.3% decline ($180M market cap reduction).

**Now open:** `drift/DRIFT-20260310-001.md` -- MTX Refund Rate Spike EU +340%

The crisis shifted from infrastructure to monetization. EU refund rates spiked from 1.8% baseline to 6.8%. Apple issued a formal warning (Belgium App Store refund rate hit 11.2%). 14,200 refund transactions worth EUR 892,000 processed in 48 hours.

This drift was caused by DRIFT-20260309-001 (EU regulatory notice) and cascaded downstream to DRIFT-20260310-002 (EU DAU drop -18%) and DRIFT-20260312-001 (ARPPU collapse).

---

## Step 5 -- Canon Contradiction and Doctrine Update (6:00)

**Open:** `canon/versions/CANON-v1.2.md` -- MTX Policy and Emergency Rollback

This canon version was issued under crisis conditions on March 9. Turnaround from trigger to ratification: 14 hours.

Key changes codified:
1. **Kill Switch Policy** (Section 4.5) -- any pricing change causing refund rates >200% of trailing average can be unilaterally rolled back.
2. **EU Monetization Addendum** (Section 4.6) -- loot box mechanics suspended in EU, converted to direct purchase.
3. **Canon Contradiction Acknowledgment** (Section 7) -- the "player-first monetization" pledge was contradicted by the emergency pivot. This is formally logged and addressed.

**Linked decision:** `decisions/DLR-20260309-001.md` -- Emergency MTX Rollback EU

This DLR is the **kill switch activation** for DLR-20260224-003 (Season 4 pricing strategy). Note the finance section:
- Refund liability: $2.1M
- Quarterly EU revenue impact: -$4.8M
- EBITDA impact: -$3.1M net
- Two assumptions invalidated: ASM-0006 (EU price tolerance) and ASM-0014 (EU regulatory tolerance)

**Total financial exposure at time of CANON-v1.2 publication: $79.4M.**

---

## Step 6 -- Telemetry Impact (7:30)

**Open:** `telemetry/telemetry_2026-W11.json`

Compare W11 to the W09 baseline:

| Metric | W09 (Baseline) | W11 (Crisis) | Delta |
|--------|----------------|--------------|-------|
| Coherence Score | 88 | **52** | -36 |
| Global DAU | 1.2M | **1.05M** | -12.5% |
| EU DAU | 348K | **285K** | -18% |
| EU ARPPU | $14.80 | **$8.90** | -40% |
| EU Churn | 1.7% | **8.2%** | +383% |
| SAI | 34 | **74** | +118% |
| Refund Rate | 0.4% | **6.8%** | +1,600% |
| Patch SLA | 4.2h | **12.4h** | +195% |
| Support Tickets | 3,200 | **14,200** | +344% |
| Expired Assumptions | 0 | **2** | ASM-0007, ASM-0009 |

The coherence score dropped from 88 to 52 -- the system detected the governance breakdown. Every component degraded: assumption health (91 to 41), decision freshness (86 to 55), drift response (89 to 48), canon alignment (85 to 64).

---

## Step 7 -- Patch and Recovery (9:00)

**Verify patched drift:** Reopen `drift/DRIFT-20260302-001.md` -- status is **patched**. The autoscaler was reconfigured (stabilization window: 120s to 45s, max surge: 200% to 400%), the CCU model was retrained (v3.0, 6% error vs. v2.1's 46%), and a Demand Signal Council was established.

**Open:** `telemetry/telemetry_2026-W13.json`

| Metric | W11 (Crisis) | W13 (Recovery) | W09 (Baseline) | Recovery % |
|--------|--------------|----------------|----------------|------------|
| Coherence Score | 52 | **76** | 88 | 67% |
| Global DAU | 1.05M | **1.15M** | 1.2M | 67% |
| EU DAU | 285K | **310K** | 348K | 40% |
| EU ARPPU | $8.90 | **$11.40** | $14.80 | 42% |
| EU Churn | 8.2% | **4.1%** | 1.7% | 63% |
| SAI | 74 | **45** | 34 | 73% |
| Refund Rate | 6.8% | **1.4%** | 0.4% | 84% |
| Patch SLA | 12.4h | **5.1h** | 4.2h | 89% |

The system is recovering. Coherence score climbed from 52 to 76. Refund rate is approaching baseline. SAI dropped to 45. EU metrics are still below baseline but trending positively. The governance framework detected the crisis, triggered decisions, and is tracking recovery.

Nine drift signals remain open or in-progress entering W14 -- the system is not done yet, and it knows it.

---

## What This Proves

- **Drift detection works.** DRIFT-20260302-001 was detected 9 minutes after the CCU breach. Within 72 hours, 6 cascade drifts were logged with full root cause and impact.
- **Assumptions expire and the system catches it.** ASM-0005 (CCU projection) was invalidated by reality. The governance framework flagged it, triggered a DLR, and the assumption was revised.
- **Financial risk is quantified at every layer.** Every DLR and DRIFT includes EBITDA impact, revenue delta by region, churn elasticity, and sponsor clause exposure. Decision-makers see dollar amounts, not abstractions.
- **Canon updates are governed even under crisis.** CANON-v1.2 was ratified in 14 hours under sev-1 conditions, with full diff, rationale, and contradiction acknowledgment. No doctrine changed without a paper trail.
- **Telemetry reflects governance health in real time.** The coherence score dropped from 88 to 52 during the crisis and recovered to 76 as patches landed. The score is a leading indicator -- when governance degrades, the number moves before the revenue does.
- **Cascades are traceable end-to-end.** From a single CCU assumption failure (ASM-0005) to a $79.4M financial exposure event, every link in the chain is recorded, cross-referenced, and auditable.
