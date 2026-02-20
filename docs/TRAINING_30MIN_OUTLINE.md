# CoherenceOps Training (30 Minutes)

## Agenda

| Time | Topic | Activity |
|------|-------|----------|
| 0-5 min | **The Problem** | "If your lead left tomorrow..." diagnostic |
| 5-10 min | **Four Modules** | IntelOps, ReOps, FranOps, DriftOps overview |
| 10-15 min | **Live Demo** | Create a DLR via one-click link, walk through template |
| 15-20 min | **Assumptions** | Edit claims.yaml, show half-life and expiry concepts |
| 20-25 min | **Drift Loop** | Open a drift signal, link to patch PR, resolve |
| 25-30 min | **Q&A + Targets** | Coherence Score, "why retrieval" KPI, next steps |

## Materials Needed

- Screen share with repo open on GitHub
- The [Quick Start](QUICKSTART_1PAGE.md) printed or shared
- The [Swim Lane](SWIMLANE.md) diagram projected

## Key Takeaways for Participants

1. Decisions are sealed in version control, not Slack
2. Assumptions expire — treat them like TTLs, not permanent truths
3. Canon is protected memory — changing it is a deliberate act
4. Drift is normal — the system helps you find it and fix it
5. The Coherence Score tells you if the system is healthy

## Follow-Up Actions

- [ ] Each team member creates one DLR for a recent decision
- [ ] Team reviews `assumptions.yaml` and adds expiry dates
- [ ] Assign a Canon Steward for the first quarter
- [ ] Schedule first drift review (monthly)
