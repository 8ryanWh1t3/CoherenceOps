# Glossary

| Term | Definition |
|------|-----------|
| **Assumption** | A belief the team holds to be true, with an expiry date and half-life. Tracked in `coherence/intel/assumptions.yaml`. |
| **Blast Radius** | The scope of impact if a decision goes wrong. Documented in every DLR. |
| **Canon** | Protected institutional memory: mission, architecture, public commitments. Lives in `coherence/canon/`. |
| **Canon Steward** | The person responsible for approving changes to canon files. |
| **Claim** | A factual assertion with provenance (source, confidence, timestamp). Tracked in `coherence/intel/claims.yaml`. |
| **Coherence Score** | A 0-100 metric measuring governance health: DLR coverage, assumption currency, drift count, why retrieval time. |
| **Decision Owner** | The person accountable for a DLR post-merge. Responds to drift signals related to that decision. |
| **DLR** | Decision Ledger Record. A structured document recording what was decided, why, what was traded off, and how to roll back. |
| **Drift** | When reality diverges from a recorded decision, assumption, or canon entry. |
| **Drift Signal** | A formal record that drift has been detected, with severity and proposed patch. Lives in `coherence/drift/`. |
| **DriftOps** | The module responsible for detecting drift and routing patches. |
| **FranOps** | The memory/canon module. Protects institutional knowledge that must survive personnel changes. |
| **Half-Life** | The period after which an assumption should be re-validated. |
| **IntelOps** | The truth module. Manages claims, assumptions, and provenance. |
| **Major PR** | A PR that requires a DLR: labeled `major`, changes 10+ files, or touches canon/intel/architecture. |
| **Patch PR** | A pull request that resolves a drift signal by fixing the root cause. |
| **Provenance** | The chain of evidence supporting a claim: who said it, when, based on what. |
| **ReOps** | The reasoning module. Records decisions via DLRs. |
| **Why Retrieval** | The time it takes a new person to find why something was built a certain way. Target: ≤ 60 seconds. |
