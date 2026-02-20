# CANON-v1.4 -- Narrative Review Gate and Incident SOP

| Field          | Value                                      |
|----------------|--------------------------------------------|
| **Version**    | 1.4                                        |
| **Date**       | 2026-03-27                                 |
| **Author**     | @narrative-lead (Montreal), @ops-lead (LA)  |
| **Status**     | current                                    |
| **Scope**      | Global                                     |
| **Linked DLRs**| DLR-20260327-001, DLR-20260327-002         |
| **Base**       | CANON-v1.3                                 |

---

## Summary

Final canon version in the W09-W13 window. Adds two major governance
structures that emerged from the crisis arc of Weeks 10-12: a mandatory
narrative review gate for all live events, and a global incident response
SOP codified from the ad-hoc processes that were improvised during the
esports spike and monetization backlash. Also establishes the post-mortem
framework as a canon requirement.

This version represents the "stabilization" phase of the Season 4 arc.
The institutional knowledge gained through three cascading crises is now
encoded into operational canon.

---

## Diff from CANON-v1.3

### Added

1. **Narrative Review Gate for Live Events** (New Section 3.6)
   - All live events (tournaments, seasonal launches, limited-time modes)
     require narrative sign-off from Montreal editorial before deployment.
   - Review window: minimum 72 hours before event start.
   - Review scope: quest dialogue, event lore, UI copy, reward descriptions,
     promotional materials.
   - No bypass permitted. Emergency events that cannot meet the 72h window
     must be escalated to @exec-team.
   - Gate enforced via CI/CD pipeline check (Warsaw implementation,
     DLR-20260320-002).
   - Rationale: the W10-W11 crisis produced 5 emergency patches that
     modified narrative content without Montreal review, causing the JP
     divergence (DRIFT-20260320-001) and community confusion around the
     monetization pivot messaging.

2. **Global Incident Response SOP** (New Section 8)
   - Formalizes the incident response process that was improvised during
     W10 (esports spike) and W11 (monetization backlash).
   - Severity classification:
     - **sev-1:** Revenue impact >$1M/day OR regulatory action OR sponsor
       contract breach. Requires @exec-team notification within 30 min.
     - **sev-2:** Revenue impact >$100K/day OR public commitment breach.
       Requires @ops-lead notification within 2 hours.
     - **sev-3:** Operational degradation without immediate revenue impact.
       Standard escalation path.
   - Incident commander: @ops-lead (LA) for infrastructure, @monetization-lead
     (Berlin) for revenue, @narrative-lead (Montreal) for content.
   - Cross-studio war room: mandatory for sev-1, optional for sev-2.
   - Communication cadence: internal status every 2 hours (sev-1) or
     every 6 hours (sev-2). External comms per Commitment 5 (transparent
     communication policy).
   - Estimated MTTR improvement: 35% (CLAIM-0010).

3. **Post-Mortem Framework** (New Section 8.3)
   - All sev-1 and sev-2 incidents require a written post-mortem within
     5 business days of resolution.
   - Post-mortem template: timeline, root cause, contributing factors,
     assumptions invalidated, canon updates required, action items with
     owners and deadlines.
   - Post-mortems are published internally to all studios. Sanitized
     versions are published to the community per Commitment 5.
   - Post-mortem findings that invalidate assumptions must be logged as
     ASM status changes within 24 hours.
   - DRIFT-20260327-001 logged 3 assumptions invalidated by the W10-W12
     arc (ASM-0005, ASM-0007, ASM-0012).

### Modified

4. **Emergency Hotfix Bypass Protocol** (Section updated from DLR-20260306-002)
   - Added mandatory localization checkpoint to the bypass protocol.
   - Bypass now requires @loc-lead notification within 1 hour of deployment.
   - Localization delta assessment required within 4 hours.
   - Rationale: the original bypass protocol had no localization gate,
     which caused the JP divergence.

5. **JP Localization Status** (Section 5.6, updated from v1.3)
   - Resync completed for 41 of 47 diverged strings (87%).
   - Remaining 6 strings require voice-over re-recording (scheduled W14).
   - JP NPS recovering: -22 at nadir, -11 at CANON-v1.4 publication.

### Unchanged

- Mission canon (Section 1) -- no changes.
- Technical architecture (Section 2) -- no changes.
- Kill switch policy (Section 4.5) -- no changes.
- Canon-diff tooling (Section 5.5) -- no changes.
- Regional pricing parity standard (Section 4.7) -- no changes.
- Canon contradiction acknowledgment (Section 7) -- no changes.

---

## Rationale

The W10-W13 arc exposed two governance gaps that CANON-v1.4 closes:

**Gap 1: Narrative review was optional during emergencies.** Five emergency
patches in W10-W11 modified player-facing content without Montreal review.
The narrative review gate makes this structurally impossible going forward.
Cost of the gap: $3.2M in localization rework, -22 NPS points in JP.

**Gap 2: Incident response was improvised.** During the esports spike,
the cross-studio war room was convened ad-hoc over Slack. During the
monetization backlash, Berlin operated semi-independently for the first
6 hours because no SOP existed. The incident response SOP ensures that
future sev-1 events follow a documented, rehearsed process. Estimated
MTTR improvement: 35%.

**Financial context at time of publication:**
- Esports spike direct cost: $4.2M
- Monetization backlash annualized shortfall: $38M (recovering)
- Localization rework: $3.2M
- SOP development and training: $0.4M
- Total W10-W13 crisis cost: ~$45.8M
- Recovered/mitigated by W13: ~$18.3M (sponsors renegotiated, EU refunds
  processed, direct-purchase conversion at 72%)

---

## Unresolved Items Carried Forward

| ID                 | Description                           | Status      |
|--------------------|---------------------------------------|-------------|
| DRIFT-20260309-001 | EU loot box regulatory notice         | in_progress |
| DRIFT-20260312-001 | ARPPU collapse EU                     | in_progress |
| DRIFT-20260313-002 | Sponsor renegotiation triggered       | in_progress |
| DRIFT-20260323-001 | Recovery metrics below target         | open        |
| DRIFT-20260325-001 | Residual pricing parity drift LATAM   | open        |
| DRIFT-20260327-001 | Post-mortem: 3 assumptions invalidated| open        |

---

## Canon Linkage

- **Supersedes:** CANON-v1.3
- **Superseded by:** N/A (current)
- **Linked DLRs:** DLR-20260327-001, DLR-20260327-002
- **Linked Drifts:** DRIFT-20260320-001, DRIFT-20260327-001
- **Linked Claims:** CLAIM-0010
- **MASTER_INDEX Row:** 91
