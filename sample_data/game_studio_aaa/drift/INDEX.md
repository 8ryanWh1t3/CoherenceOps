# DRIFT Index -- AetherForge Interactive / Eclipse Dominion

> **Coverage**: W09--W13 2026 (Feb 24 -- Mar 27)
> **Total signals**: 25
> **Severity breakdown**: 6 sev-1 | 8 high | 9 medium | 2 low
> **Status breakdown**: 3 open | 6 in_progress | 16 patched

---

## All Drift Signals

| ID | Date | Title | Severity | Status | Cascade Chain |
|---|---|---|---|---|---|
| DRIFT-20260225-001 | 2026-02-25 | Pre-Tournament Matchmaking Latency Baseline Drift | low | patched | -- |
| DRIFT-20260227-001 | 2026-02-27 | Season 4 Client Patch Size Exceeds CDN Budget | medium | patched | -- |
| DRIFT-20260228-001 | 2026-02-28 | Anti-Cheat False Positive Rate Spike (+240%) | high | patched | -- |
| DRIFT-20260302-001 | 2026-03-02 | Tournament CCU Exceeded Projections 340% | sev-1 | patched | ASM-0005 invalidated -> DRIFT-20260302-002, DRIFT-20260303-001, DRIFT-20260304-001 |
| DRIFT-20260302-002 | 2026-03-02 | Matchmaking Queue Time Spike (P50: 4m12s) | high | patched | <- DRIFT-20260302-001 |
| DRIFT-20260303-001 | 2026-03-03 | OrionTel Sponsor Uptime Clause at Risk | high | patched | <- DRIFT-20260302-001 -> DRIFT-20260306-001 |
| DRIFT-20260304-001 | 2026-03-04 | APAC Latency >120ms (P95: 142ms) | sev-1 | patched | <- DRIFT-20260302-001 -> DRIFT-20260305-001 |
| DRIFT-20260305-001 | 2026-03-05 | Competitive Fairness Complaints Surge | high | patched | <- DRIFT-20260304-001 -> DRIFT-20260305-002 |
| DRIFT-20260305-002 | 2026-03-05 | Stakeholder Anxiety Index Spike to 82 | sev-1 | patched | <- DRIFT-20260302-001, DRIFT-20260305-001 |
| DRIFT-20260306-001 | 2026-03-06 | VantaFuel Sponsor Suspension Threat | high | patched | <- DRIFT-20260303-001 -> DRIFT-20260313-002 |
| DRIFT-20260309-001 | 2026-03-09 | EU Loot Box Regulatory Notice | sev-1 | in_progress | -> DRIFT-20260310-001, DRIFT-20260311-001, DRIFT-20260313-001 |
| DRIFT-20260310-001 | 2026-03-10 | MTX Refund Rate Spike EU (+340%) | high | patched | <- DRIFT-20260309-001 -> DRIFT-20260310-002, DRIFT-20260316-001 |
| DRIFT-20260310-002 | 2026-03-10 | DAU Drop EU -18% (420K to 344K) | sev-1 | in_progress | <- DRIFT-20260310-001 -> DRIFT-20260312-001 |
| DRIFT-20260311-001 | 2026-03-11 | Canon Contradiction: Monetization Ethics | high | patched | <- DRIFT-20260309-001 -> DRIFT-20260313-002 |
| DRIFT-20260312-001 | 2026-03-12 | ARPPU Collapse EU ($14.50 to $8.90) | sev-1 | in_progress | <- DRIFT-20260310-002 -> DRIFT-20260323-001 |
| DRIFT-20260313-001 | 2026-03-13 | Patch Cadence SLA Breached: 48h to 96h | high | patched | <- DRIFT-20260309-001, DLR-20260228-001 -> DRIFT-20260313-002, DRIFT-20260319-001 |
| DRIFT-20260313-002 | 2026-03-13 | Sponsor Renegotiation Triggered ($30M at risk) | sev-1 | in_progress | <- DRIFT-20260306-001, DRIFT-20260313-001 |
| DRIFT-20260316-001 | 2026-03-16 | Rollback Kill Switch Invoked: MTX | high | patched | <- DLR-20260309-001 -> DRIFT-20260317-001 |
| DRIFT-20260317-001 | 2026-03-17 | Cross-Region Pricing Parity Drift NA vs EU | medium | in_progress | <- DLR-20260309-001, DRIFT-20260316-001 -> DRIFT-20260325-001 |
| DRIFT-20260318-001 | 2026-03-18 | ASM-0007 Expired: Churn Model Outdated (R-sq 0.94 to 0.71) | medium | patched | <- DRIFT-20260312-001 -> DRIFT-20260327-001 |
| DRIFT-20260319-001 | 2026-03-19 | QA Pipeline Warsaw Bottleneck (96h turnaround) | medium | in_progress | <- DRIFT-20260313-001 -> DRIFT-20260323-001 |
| DRIFT-20260320-001 | 2026-03-20 | Narrative Localization Divergence JP vs EN | medium | patched | <- DLR-20260309-002 -> CANON-v1.3 |
| DRIFT-20260323-001 | 2026-03-23 | Recovery Metrics Below Target: D7 Retention (38% vs 42%) | medium | open | <- DRIFT-20260312-001, DRIFT-20260319-001 |
| DRIFT-20260325-001 | 2026-03-25 | Residual Pricing Parity Drift LATAM (18% PPP gap) | low | open | <- DRIFT-20260317-001 |
| DRIFT-20260327-001 | 2026-03-27 | Post-Mortem: 3 Assumptions Invalidated (ASM-0005, 0007, 0012) | high | open | <- DRIFT-20260302-001, DRIFT-20260318-001, DRIFT-20260313-001 |

---

## Cascade Topology

```
W09 (Feb 24-28) -- Baseline
  DRIFT-20260225-001  Pre-tournament latency baseline
  DRIFT-20260227-001  Client patch CDN budget
  DRIFT-20260228-001  Anti-cheat false positives

W10 (Mar 2-8) -- Esports Spike
  ASM-0005 invalidated
    -> DRIFT-20260302-001  CCU 340% over projection
      -> DRIFT-20260302-002  Matchmaking queue spike
      -> DRIFT-20260303-001  OrionTel uptime clause
        -> DRIFT-20260306-001  VantaFuel suspension threat
      -> DRIFT-20260304-001  APAC latency >120ms
        -> DRIFT-20260305-001  Competitive fairness complaints
          -> DRIFT-20260305-002  SAI spike to 82

W11 (Mar 9-15) -- Monetization Backlash
  DRIFT-20260309-001  EU regulatory notice
    -> DRIFT-20260310-001  MTX refund spike EU
      -> DRIFT-20260310-002  DAU drop EU -18%
        -> DRIFT-20260312-001  ARPPU collapse EU
    -> DRIFT-20260311-001  Canon contradiction
    -> DRIFT-20260313-001  Patch SLA breached 48h->96h
      -> DRIFT-20260313-002  Sponsor renegotiation

W12 (Mar 16-22) -- Stabilization
  DRIFT-20260316-001  Kill switch invoked MTX
    -> DRIFT-20260317-001  Pricing parity drift NA vs EU
  DRIFT-20260318-001  ASM-0007 expired (churn model)
  DRIFT-20260319-001  Warsaw QA bottleneck
  DRIFT-20260320-001  JP localization divergence

W13 (Mar 23-27) -- Recovery
  DRIFT-20260323-001  D7 retention below target
  DRIFT-20260325-001  LATAM pricing parity drift
  DRIFT-20260327-001  Post-mortem: 3 assumptions invalidated
```

---

## Unresolved Entering W14

| ID | Title | Status | Owner |
|---|---|---|---|
| DRIFT-20260309-001 | EU Loot Box Regulatory Notice | in_progress | Berlin Legal |
| DRIFT-20260310-002 | DAU Drop EU -18% | in_progress | Berlin Analytics |
| DRIFT-20260312-001 | ARPPU Collapse EU | in_progress | Berlin Revenue |
| DRIFT-20260313-002 | Sponsor Renegotiation Triggered | in_progress | LA Partnerships |
| DRIFT-20260317-001 | Cross-Region Pricing Parity Drift | in_progress | Berlin Revenue |
| DRIFT-20260319-001 | QA Pipeline Warsaw Bottleneck | in_progress | Warsaw QA |
| DRIFT-20260323-001 | Recovery Metrics Below Target | open | LA Player Insights |
| DRIFT-20260325-001 | Residual Pricing Parity Drift LATAM | open | Berlin Revenue |
| DRIFT-20260327-001 | Post-Mortem: 3 Assumptions Invalidated | open | LA Engineering |
