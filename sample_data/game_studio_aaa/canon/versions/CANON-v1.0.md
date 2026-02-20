# CANON-v1.0 -- Canon Baseline: Season 4 Launch

| Field          | Value                                      |
|----------------|--------------------------------------------|
| **Version**    | 1.0                                        |
| **Date**       | 2026-02-24                                 |
| **Author**     | @narrative-lead (Montreal)                 |
| **Status**     | superseded (by CANON-v1.1, 2026-03-02)     |
| **Scope**      | Global                                     |
| **Linked DLRs**| DLR-20260226-001, DLR-20260224-004         |

---

## Summary

Establishes the canonical baseline for Eclipse Dominion Season 4 across all
five studios. This version codifies the mission principles, technical architecture
reference, competitive integrity rules, and monetization framework that govern
all operational decisions during the Season 4 window.

CANON-v1.0 is the first versioned snapshot under the CoherenceOps governance
model. All prior institutional knowledge was unversioned and distributed across
wikis, Slack channels, and tribal memory. This document marks the transition
to auditable canon.

---

## Contents Established

### 1. Mission Canon (Seed: mission.md)
- Player-first competitive experience as the root principle.
- Five-studio responsibility matrix (LA, Montreal, Tokyo, Berlin, Warsaw).
- Revenue context: $480M annual, 62% MTX / 24% Battle Pass / 14% Esports.

### 2. Technical Architecture Canon (Seed: architecture.md)
- Multi-region server fleet: US-East, US-West, EU-Central, APAC-NE, APAC-SE.
  Total capacity: 1,000K CCU.
- Microservices on Kubernetes (EKS/GKE). Service mesh: Istio.
- CDN: CloudFront (NA/APAC), Cloud CDN (EU), Akamai (LATAM/APAC-SE).
- VanguardShield anti-cheat: <0.1% false positive rate target.
- SBMM: Modified Glicko-2, 80ms latency preference, 90s queue timeout.
- Telemetry: Kafka -> Snowflake, 1.2M events/sec average.

### 3. Competitive Integrity Rules
- Tournament balance freeze: 72 hours before sanctioned events.
- Dedicated server provisioning: 24 hours before event start.
- Latency SLA: 80ms P95 for ranked and tournament modes.
- Anti-cheat coverage: 100% of ranked and tournament matches.

### 4. Monetization Framework
- Cosmetic-only default. No pay-to-win mechanics.
- Loot box mechanics permitted with regional compliance review.
- Battle Pass pricing benchmarked against regional PPP.
- Executive sign-off required for any mechanic with competitive impact.

### 5. Public Commitments (Seed: public-commitments.md)
- Player-first monetization pledge.
- 48-hour patch SLA for critical bugs.
- Tournament competitive integrity guarantee.
- Localization quality standard.
- Transparent communication policy.

---

## Diff from Previous Version

N/A -- this is the initial baseline. No prior versioned canon exists.

---

## Rationale

Season 4 introduces the largest content drop in Eclipse Dominion history (3 new
agents, 2 maps, ranked overhaul). The operational complexity of coordinating
five studios across a live-service launch with a concurrent esports season
requires a single source of truth. CANON-v1.0 provides that foundation.

The decision to formalize canon was driven by two near-misses in Season 3:
1. A balance patch deployed by Montreal conflicted with a Tokyo-initiated
   matchmaking change, causing a 6-hour ranked queue outage.
2. Berlin launched a promotional bundle that community perceived as pay-to-win,
   triggering a 48-hour PR crisis before executive review could intervene.

Both incidents would have been caught by cross-studio canon review.

---

## Assumptions Active at This Version

| ASM ID   | Description                              | Status  |
|----------|------------------------------------------|---------|
| ASM-0001 | Server fleet handles 800K peak CCU       | active  |
| ASM-0002 | Build pipeline 95th-pct under 45min      | active  |
| ASM-0003 | Patch Tuesday SLA 48h response window    | active  |
| ASM-0004 | Battle Pass ARPPU $14.50 baseline        | active  |
| ASM-0006 | Season 4 narrative arc no lore conflicts | active  |

---

## Canon Linkage

- **Superseded by:** CANON-v1.1
- **Seed Documents:** mission.md, architecture.md, public-commitments.md
- **Linked DLRs:** DLR-20260226-001, DLR-20260224-004
- **MASTER_INDEX Row:** 87
