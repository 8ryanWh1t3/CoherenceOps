# CANON-v1.1 -- Tournament Rules and Balance Freeze

| Field          | Value                                      |
|----------------|--------------------------------------------|
| **Version**    | 1.1                                        |
| **Date**       | 2026-03-02                                 |
| **Author**     | @narrative-lead (Montreal), @esports-lead (LA) |
| **Status**     | superseded (by CANON-v1.2, 2026-03-09)     |
| **Scope**      | Global                                     |
| **Linked DLRs**| DLR-20260302-003                           |
| **Base**       | CANON-v1.0                                 |

---

## Summary

Extends the Season 4 canon baseline with explicit rules for the Apex Invitational
tournament window. Adds tournament balance freeze policy, broadcast scheduling
rules, and sponsor integration guidelines for OrionTel ($18M/yr) and VantaFuel
($12M/yr). This update was prompted by DLR-20260302-003 (Tournament balance
patch freeze) as the Invitational entered its live phase.

---

## Diff from CANON-v1.0

### Added

1. **Tournament Balance Freeze Policy** (Section 3.1 addendum)
   - All balance changes frozen 72 hours before sanctioned tournament start.
   - Freeze enforced via Montreal-owned feature flag (`tournament-freeze-lock`).
   - Exception path: sev-1 exploit affecting competitive integrity, requiring
     unanimous sign-off from @balance-lead, @esports-lead, and @exec-team.
   - Freeze duration: from T-72h through tournament conclusion + 24h cooldown.

2. **Broadcast Scheduling Rules** (New Section 3.5)
   - Broadcast windows coordinated across NA (EST prime), EU (CET prime),
     APAC (JST prime) to maximize concurrent viewership.
   - Server capacity pre-provisioned for each broadcast window: +30% headroom
     over projected CCU.
   - Replay system guaranteed available within 15 minutes of match conclusion.

3. **Sponsor Integration Guidelines** (New Section 6)
   - OrionTel and VantaFuel branding placement rules for in-game tournament UI.
   - Sponsor uptime clause: 99.5% availability during broadcast windows.
   - Sponsor content review: all branded assets approved by @comms-lead 48h
     before deployment.
   - Contractual penalty exposure: $4.2M combined if uptime clause breached
     during any Invitational broadcast day.

### Modified

4. **Server Fleet Capacity Reference** (Section 2, architecture.md)
   - Added tournament-specific scaling profile: pre-provision +30% headroom.
   - Referenced ASM-0005 (tournament CCU peak 620K) as the planning baseline.

### Unchanged

- Mission canon (Section 1) -- no changes.
- Monetization framework (Section 4) -- no changes.
- Public commitments (Section 5) -- no changes.

---

## Rationale

The Apex Invitational is the highest-stakes competitive event in Eclipse
Dominion history: $2.5M prize pool, 32 teams, 4-day broadcast across 3
time zones. OrionTel and VantaFuel sponsor contracts include performance
clauses that expose AetherForge to $4.2M in penalties if infrastructure
SLAs are breached during broadcast windows.

CANON-v1.1 formalizes the tournament operating rules that were previously
communicated informally between LA (infrastructure), Tokyo (matchmaking),
and Montreal (balance). The goal is to ensure that no studio can deploy
a change during the tournament window without explicit cross-studio sign-off.

> **Foreshadow:** ASM-0005 (620K peak CCU) was already under pressure at
> the time of this canon update. Actual peak CCU during the Invitational
> reached 2.1M (DRIFT-20260302-001), invalidating the assumption and
> triggering a 6-event drift cascade.

---

## Assumptions Active at This Version

| ASM ID   | Description                              | Status  |
|----------|------------------------------------------|---------|
| ASM-0001 | Server fleet handles 800K peak CCU       | active  |
| ASM-0005 | Tournament CCU peak 620K                 | active (expired 2026-03-08) |
| ASM-0006 | Season 4 narrative arc no lore conflicts | active  |
| ASM-0008 | Anti-cheat false positive rate <0.1%     | active  |

---

## Canon Linkage

- **Supersedes:** CANON-v1.0
- **Superseded by:** CANON-v1.2
- **Linked DLRs:** DLR-20260302-003
- **Linked Drifts:** DRIFT-20260302-001 (CCU spike, post-publication)
- **MASTER_INDEX Row:** 88
