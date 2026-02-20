# Technical Architecture Canon -- Eclipse Dominion

> **Canon Type:** Seed
> **Effective:** 2026-02-24
> **Owner:** @infra-lead, @eng-lead
> **Scope:** Global
> **Product:** Eclipse Dominion

---

## Overview

Eclipse Dominion runs on a globally distributed microservices architecture
designed for low-latency competitive play across five regions. This document
is the canonical reference for infrastructure topology, service boundaries,
and operational SLAs.

---

## Server Fleet -- Multi-Region Deployment

| Region     | Location(s)                | Provider   | Capacity (CCU) |
|------------|----------------------------|------------|----------------|
| US-East    | Virginia, Ohio             | AWS        | 320K           |
| US-West    | Oregon, N. California      | AWS        | 180K           |
| EU-Central | Frankfurt, Amsterdam       | AWS + GCP  | 240K           |
| APAC-NE    | Tokyo, Seoul               | AWS        | 160K           |
| APAC-SE    | Singapore, Sydney          | AWS        | 100K           |
| **Total**  |                            |            | **1,000K**     |

Auto-scaling is configured with a 3-minute warm-up window. Baseline fleet
runs at 40% capacity; burst scaling targets 90% within 8 minutes. The
tournament profile pre-provisions an additional 30% headroom 24 hours
before sanctioned events.

> **Note:** ASM-0005 assumed peak tournament CCU of 620K. This was
> invalidated during the Apex Invitational (DRIFT-20260302-001) when
> actual CCU reached 2.1M. Post-incident scaling thresholds were revised
> via DLR-20260306-001.

---

## Microservices Architecture (Kubernetes)

All services run on managed Kubernetes (EKS in AWS regions, GKE in EU-Central
secondary). Service mesh: Istio. Deployment: Argo CD with GitOps.

### Core Service Groups

| Service Group       | Owner Studio | Services                                          |
|---------------------|--------------|---------------------------------------------------|
| Game Servers        | LA + Tokyo   | match-host, physics-sim, replay-capture           |
| Matchmaking         | Tokyo        | skill-rating, queue-manager, region-router        |
| Monetization        | Berlin       | store-front, pricing-engine, entitlement-svc      |
| Anti-Cheat          | Warsaw       | vanguardshield-agent, ban-engine, appeal-svc      |
| Narrative           | Montreal     | quest-engine, lore-state, dialogue-svc            |
| Platform            | LA           | auth-svc, profile-svc, social-svc, party-svc     |
| Telemetry           | LA           | event-ingest, aggregation-svc, alerting-svc       |

### Key Dependencies

- **Matchmaking** depends on **Game Servers** (capacity awareness) and
  **Anti-Cheat** (pre-match integrity check).
- **Monetization** depends on **Matchmaking** for post-match reward grants.
- **Narrative** depends on **Matchmaking** for quest-progress event triggers.

---

## CDN -- Asset Delivery

| CDN Provider  | Coverage      | Cache TTL | Purge SLA |
|---------------|---------------|-----------|-----------|
| CloudFront    | NA, APAC      | 24h       | < 5 min   |
| Cloud CDN     | EU            | 24h       | < 5 min   |
| Akamai        | LATAM, APAC-SE| 12h       | < 10 min  |

Patch delivery uses delta-compression. Average Season patch: 2.8 GB full,
420 MB delta. CDN failover target: < 30 seconds (ASM-0009, DLR-20260316-003).

---

## VanguardShield Anti-Cheat

| Metric                    | Target     | Current (W13) |
|---------------------------|------------|---------------|
| False Positive Rate       | < 0.1%    | 0.07%         |
| Detection Latency (P95)   | < 500ms   | 340ms         |
| Ban Appeal Resolution     | < 24h     | 18h           |
| Coverage                  | 100% Ranked/Tournament | 100% |

VanguardShield runs as a kernel-level agent on client machines and a
server-side behavioral analysis pipeline. Warsaw maintains the detection
models; LA operates the ban-engine infrastructure.

- **Linked ASM:** ASM-0008 (false positive rate < 0.1%)
- **Linked EVID:** EVID-0002 (false positive analysis report)

---

## Matchmaking Algorithm -- Skill-Based (SBMM)

Eclipse Dominion uses a modified Glicko-2 rating system with the following
parameters:

| Parameter          | Value          |
|--------------------|----------------|
| Rating Range       | 0 -- 5000      |
| Placement Matches  | 10             |
| Confidence Decay   | 0.06 per week  |
| Queue Timeout      | 90s (expands bracket by 200 SR) |
| Region Priority    | Latency < 80ms preferred; cross-region if wait > 120s |

Matchmaking is owned by the Tokyo studio. Cross-region routing was
rebalanced after the Apex Invitational incident (DLR-20260306-003).

---

## Telemetry Pipeline

```
Client SDK --> Kafka (3 clusters: NA, EU, APAC)
           --> Kafka Connect --> Snowflake (analytics warehouse)
           --> Kafka Streams --> Real-time alerting (PagerDuty)
           --> S3 (raw event archive, 90-day retention)
```

| Metric                  | Value         |
|-------------------------|---------------|
| Events per Second (avg) | 1.2M         |
| Events per Second (peak)| 4.8M         |
| Kafka Lag SLA           | < 30s        |
| Snowflake Freshness     | < 5 min      |
| Alerting Latency (P95)  | < 45s        |

Weekly telemetry snapshots (TELEMETRY-W09 through TELEMETRY-W13) are
published every Friday by @data-lead and archived in `/telemetry/`.

---

## Canon Linkage

- **Referenced by:** CANON-v1.0, CANON-v1.1, CANON-v1.4
- **Linked DLRs:** DLR-20260224-001 (build pipeline), DLR-20260224-002 (scaling policy)
- **Linked ASMs:** ASM-0001, ASM-0005 (expired), ASM-0009
