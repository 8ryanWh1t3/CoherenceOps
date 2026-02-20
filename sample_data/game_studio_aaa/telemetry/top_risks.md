# Eclipse Dominion — Top Risks (as of W13)

**Studio:** AetherForge Interactive
**Assessment Date:** 2026-03-27
**Based On:** telemetry_2026-W13.json
**Coherence Score:** 76/100

---

## Risk 1: EU Revenue Recovery

| Field | Value |
|-------|-------|
| **Severity** | Critical |
| **Likelihood** | High |
| **Drift Signal** | DRIFT-0015 |
| **Related Decision** | DLR-0037 (cosmetic rebalance) |

**Current State:** EU weekly revenue is estimated at ~$2.54M vs ~$2.95M baseline (-14%). EU ARPPU at $11.40 vs $14.80 baseline (-23%). EU D7 retention at 38.0% vs 49.5% baseline (-23%).

**Why It Matters:** EU represents 29% of global DAU and historically 30%+ of MTX revenue. The pricing backlash damaged whale trust — the cohort that drives disproportionate MTX spend. Even with pricing parity restored, behavioral patterns suggest EU whales have adopted a "wait and see" posture. If EU ARPPU does not recover above $13.00 by W16, the annualized revenue shortfall exceeds $18M.

**Mitigation:**
- Cosmetic rebalance (DLR-0037) launched W13 with transparent pricing. Early reception positive.
- EU-exclusive loyalty program under consideration (not yet ratified).
- Weekly EU sentiment tracking via community pulse surveys.

**Recovery Target:** EU ARPPU > $13.50 by W16. EU D7 retention > 42% by W17.

---

## Risk 2: Sponsor Renegotiation Exposure

| Field | Value |
|-------|-------|
| **Severity** | Critical |
| **Likelihood** | Medium |
| **Drift Signal** | DRIFT-0018 |
| **Related Decision** | DLR-0036 (sponsor communication protocol) |

**Current State:** Two tier-1 esports sponsors — NovaTech ($18M/yr) and Pulse Energy ($12M/yr) — flagged "brand safety" concerns following the W11 pricing controversy. Combined exposure: $30M annual. Both contracts contain morality/reputation clauses that were arguably triggered. Neither has formally initiated exit, but both requested renegotiation meetings.

**Why It Matters:** Esports sponsorship revenue ($1.38M/wk baseline) funds 15% of the competitive ecosystem. Loss of either sponsor would force cuts to prize pools, broadcast quality, or regional tournament support. The downstream effect on DAU (esports viewership drives ~8% of new player acquisition) compounds the financial impact.

**Mitigation:**
- DLR-0036 established a dedicated sponsor relations team with weekly touchpoints.
- Transparency report prepared showing corrective actions taken (kill switch timeline, refund program, pricing rebalance).
- Contingency sponsor shortlist developed (3 potential replacements identified).

**Resolution Target:** Renegotiation closed by W17. Acceptable outcome: contract renewal at 85%+ of current value.

---

## Risk 3: Regulatory Compliance Timeline

| Field | Value |
|-------|-------|
| **Severity** | High |
| **Likelihood** | Medium |
| **Drift Signal** | DRIFT-0016 |
| **Related Decision** | DLR-0032 (EU pricing audit) |

**Current State:** German Federal Office of Justice (BfJ) issued an informal inquiry in W11. French DGCCRF is monitoring. The inquiry focuses on whether the EU pricing disparity constituted an unfair commercial practice under the EU Consumer Rights Directive (2011/83/EU). Estimated timeline: formal decision within 60 days of initial inquiry (by approximately W19-W20).

**Why It Matters:** A formal finding could result in:
- Mandatory pricing disclosures for all in-game purchases in EU markets.
- Fines up to 4% of annual EU revenue (~$5.5M based on current run rate).
- Precedent-setting requirements that affect the entire live-service industry.
- Mandatory refund window extension from 14 to 30 days for digital goods.

Even without a formal finding, the regulatory attention increases compliance overhead and constrains future pricing flexibility in the EU.

**Mitigation:**
- EU pricing audit (DLR-0032) completed. Full pricing history documented and preserved.
- External counsel engaged in Berlin and Paris.
- Proactive compliance brief submitted to BfJ showing corrective actions and timeline.
- Regional pricing canon updated to enforce automated parity checks on all future store updates.

**Resolution Target:** Informal inquiry closed without escalation to formal proceedings. Compliance framework in place by W18 regardless of outcome.

---

## Risk 4: Churn Model Unreliable

| Field | Value |
|-------|-------|
| **Severity** | High |
| **Likelihood** | High |
| **Drift Signal** | DRIFT-0019 |
| **Related Decision** | DLR-0038 (churn model rebuild) |

**Current State:** The predictive churn model was trained on steady-state behavioral data (Season 5-7 cohorts). The W11 pricing crisis introduced a novel churn pattern — mass sentiment-driven departure — that the model was never designed to detect. Current model accuracy has degraded from 87% precision to an estimated 54% (barely better than random for the EU cohort). The model is actively producing false negatives: players flagged as "retained" are churning.

**Why It Matters:** Without a reliable churn model:
- Retention interventions (targeted offers, re-engagement campaigns) are misfiring.
- Revenue forecasts carry wider error bars, complicating sponsor and investor communications.
- The LiveOps team is operating on intuition rather than data for EU player recovery.
- Assumption validation for future ASMs related to retention is impossible.

**Mitigation:**
- DLR-0038 authorized a full model rebuild with 21-day timeline (target: W16 completion).
- Rebuild will incorporate crisis-cohort behavioral data and sentiment signals.
- Interim: manual cohort analysis by the Berlin analytics team for EU retention decisions.
- Model validation gate added to deployment pipeline to prevent silent degradation in future.

**Resolution Target:** New model deployed by W16 with >80% precision on post-crisis cohorts. Sentiment signal integration by W18.

---

## Risk 5: LATAM Pricing Parity Gap

| Field | Value |
|-------|-------|
| **Severity** | Medium |
| **Likelihood** | Medium |
| **Drift Signal** | -- (not yet flagged; emerging) |
| **Related Decision** | -- (none yet) |

**Current State:** LATAM ARPPU ($9.70) is 40% below NA ($16.10) and 15% below APAC ($12.50). This gap has been persistent since launch but gained new relevance in the post-W11 environment where pricing parity is under intense scrutiny. LATAM players are aware of the EU pricing controversy and community forums are surfacing questions about whether LATAM is being "underserved" — lower bundle quality, fewer localized events, later content drops.

**Why It Matters:** LATAM represents 12.5% of DAU (143,750) and is the fastest-growing region by engagement. Brazilian tournament viewership drove LATAM's W10-W13 resilience. However:
- If LATAM perceives inequitable treatment, the EU backlash pattern could repeat.
- LATAM regulatory environments (Brazil's SENACON, Argentina's consumer protection) are increasingly active in digital markets.
- The cosmetic rebalance (DLR-0037) addressed EU parity but did not explicitly address LATAM bundle composition.
- LATAM content localization is 2 patches behind NA/EU.

**Mitigation:**
- LATAM pricing and content audit recommended (not yet ratified as a decision).
- Warsaw studio (responsible for LATAM localization) should accelerate the localization backlog.
- Community team monitoring LATAM sentiment channels (Reddit, Twitter/X, Discord).
- Preventive pricing parity check should be added to the LATAM store update pipeline.

**Resolution Target:** LATAM pricing/content audit ratified by W15. Localization backlog cleared by W17. Proactive parity canon established before Season 8 launch.

---

## Risk Summary Matrix

| # | Risk | Severity | Likelihood | Drift Signal | Resolution Target |
|---|------|----------|------------|--------------|-------------------|
| 1 | EU revenue recovery | Critical | High | DRIFT-0015 | W16-W17 |
| 2 | Sponsor renegotiation | Critical | Medium | DRIFT-0018 | W17 |
| 3 | Regulatory compliance | High | Medium | DRIFT-0016 | W18-W20 |
| 4 | Churn model unreliable | High | High | DRIFT-0019 | W16 |
| 5 | LATAM pricing parity gap | Medium | Medium | -- (emerging) | W15-W17 |

**Combined financial exposure:** ~$53.5M annualized ($18M EU revenue gap + $30M sponsor risk + $5.5M regulatory fine ceiling).

**Coherence implication:** Three of five risks have active drift signals. Until these resolve, coherence score is capped at approximately 80/100. Full coherence recovery (85+) requires closing DRIFT-0015, DRIFT-0016, DRIFT-0018, and DRIFT-0019.
