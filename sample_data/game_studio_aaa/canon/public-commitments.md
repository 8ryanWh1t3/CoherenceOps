# Public Commitments Canon -- AetherForge Interactive

> **Canon Type:** Seed
> **Effective:** 2026-02-24
> **Owner:** @exec-team, @comms-lead
> **Scope:** Global
> **Product:** Eclipse Dominion

---

## Purpose

This document codifies every public-facing commitment AetherForge has made
to the Eclipse Dominion player base, press, regulators, and sponsors.
Public commitments carry the weight of canon: violating them creates
institutional drift that must be logged, assessed, and resolved.

---

## Commitment 1: Player-First Monetization Pledge

**Published:** Season 2 launch blog post, press release, investor call
**Audience:** Players, press, regulators, investors

> "Eclipse Dominion will never sell competitive advantage. Every item
> available for purchase is cosmetic-only. We will never gate gameplay
> progression behind a paywall."

### Operational Implications

- All monetization changes require Berlin studio sign-off AND cross-studio
  competitive-impact review (Montreal).
- Any mechanic perceived as pay-to-win triggers an automatic escalation to
  the executive team within 4 hours.
- Loot box mechanics must comply with all regional regulations. If a
  regional regulator issues a formal notice, AetherForge will comply
  within 72 hours or invoke the kill switch (see Commitment 5 addendum).

> **Canon Conflict Note (W11):** The emergency loot-box-to-direct-purchase
> pivot in EU (DLR-20260309-001, DLR-20260311-001) was flagged as a
> contradiction to this pledge by DRIFT-20260311-001. CANON-v1.2 revised
> the monetization framework to acknowledge the contradiction and establish
> the direct-purchase model as the new EU standard.

- **Linked DLRs:** DLR-20260224-003, DLR-20260309-001, DLR-20260311-001
- **Linked Drifts:** DRIFT-20260309-001, DRIFT-20260311-001

---

## Commitment 2: 48-Hour Patch SLA

**Published:** Dev blog, patch notes header (recurring)
**Audience:** Players, esports teams, sponsors

> "When we identify a critical gameplay-affecting bug, we commit to
> deploying a fix within 48 hours. For non-critical issues, our target
> is the next scheduled Patch Tuesday."

### Operational Implications

- @ops-lead owns the SLA clock. Timer starts when a sev-1 or sev-2 bug
  is confirmed by QA (Warsaw) or reported by 3+ independent sources.
- Bypass protocol (DLR-20260306-002) allows emergency hotfixes outside
  the Patch Tuesday cadence, but requires post-deployment review within
  24 hours.
- The SLA was breached during W11 (DRIFT-20260313-001): a 48h target
  stretched to 96 hours due to cross-studio coordination overhead during
  the monetization crisis. Patch cadence was revised via DLR-20260313-001.

- **Linked DLRs:** DLR-20260228-001, DLR-20260306-002, DLR-20260313-001
- **Linked ASMs:** ASM-0003
- **Linked Drifts:** DRIFT-20260228-001, DRIFT-20260313-001

---

## Commitment 3: Tournament Competitive Integrity Guarantee

**Published:** Esports rulebook, sponsor contracts, broadcast agreements
**Audience:** Esports teams, sponsors (OrionTel, VantaFuel), broadcast partners

> "All sanctioned Eclipse Dominion tournaments run on dedicated server
> infrastructure with a guaranteed latency SLA of 80ms P95. Balance
> changes are frozen 72 hours before tournament start. Any integrity
> violation is investigated within 24 hours with public findings."

### Operational Implications

- Tournament balance freeze is mandatory (DLR-20260302-003).
- Dedicated server provisioning must be completed 24h before event start
  (DLR-20260302-002).
- The APAC latency spike during the Apex Invitational (DRIFT-20260304-001)
  breached the 80ms SLA at P95 (actual: 142ms). This triggered competitive
  fairness complaints (DRIFT-20260305-001) and sponsor clause activation
  (DRIFT-20260303-001, DRIFT-20260306-001).
- OrionTel ($18M/yr) and VantaFuel ($12M/yr) contracts include uptime and
  latency clauses. Combined sponsor exposure: $30M/yr.

- **Linked DLRs:** DLR-20260302-001, DLR-20260302-002, DLR-20260302-003, DLR-20260304-001
- **Linked Drifts:** DRIFT-20260302-001, DRIFT-20260304-001, DRIFT-20260303-001, DRIFT-20260306-001
- **Linked Claims:** CLAIM-0004, CLAIM-0005

---

## Commitment 4: Localization Quality Standard

**Published:** Regional community posts (JP, DE, KR, PT-BR, FR)
**Audience:** Non-English player communities

> "Eclipse Dominion delivers the same narrative experience in every
> supported language. Localization is not an afterthought -- it ships
> with the same quality bar as the English original."

### Operational Implications

- All narrative content must pass Montreal editorial review before
  localization handoff.
- Localized builds must match the current CANON version within one
  business day of English deployment.
- The JP localization divergence (DRIFT-20260320-001) violated this
  commitment: JP clients were running content aligned to CANON-v1.1
  while EN was on CANON-v1.3. The gap spanned 47 strings across
  12 quest lines. JP player NPS dropped 22 points.
- CANON-v1.3 added canon-diff tooling as a hard requirement for
  localization pipelines.

- **Linked DLRs:** DLR-20260309-002, DLR-20260309-003, DLR-20260320-001
- **Linked Drifts:** DRIFT-20260320-001
- **Linked ASMs:** ASM-0014

---

## Commitment 5: Transparent Communication Policy

**Published:** Community guidelines, developer blog cadence
**Audience:** Players, press

> "We communicate openly about changes that affect gameplay, monetization,
> or competitive integrity. Major changes are announced at least 7 days
> in advance. Emergency changes are communicated within 2 hours of
> deployment with a full rationale."

### Operational Implications

- @comms-lead owns the communication timeline. Pre-announcement window:
  7 days for planned changes, 2 hours for emergency deployments.
- The pay-to-win allegation response plan (DLR-20260311-002) was activated
  during W11. Community sentiment analysis showed the response reduced
  negative sentiment by an estimated 25% (CLAIM-0007, contested).
- Post-mortem reports for sev-1 incidents are published within 5 business
  days.

- **Linked DLRs:** DLR-20260311-002
- **Linked Claims:** CLAIM-0007

---

## Kill Switch Addendum (Added CANON-v1.2)

**Added:** 2026-03-09
**Context:** Emergency response to EU regulatory notice

Any pricing or monetization change that triggers regulatory action or
causes refund rates to exceed 200% of the trailing 4-week average can
be unilaterally rolled back by @monetization-lead or @exec-team without
cross-studio review. The rollback must be logged as a sev-1 DLR within
1 hour.

- **Invoked:** DRIFT-20260316-001 (MTX kill switch invoked)
- **Linked DLR:** DLR-20260309-001

---

## Canon Linkage

- **Referenced by:** CANON-v1.0, CANON-v1.1, CANON-v1.2, CANON-v1.3, CANON-v1.4
- **Financial Exposure:** $30M/yr sponsor contracts, $480M/yr total revenue
