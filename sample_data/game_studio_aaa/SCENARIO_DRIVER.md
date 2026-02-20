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
