# Design Decisions

## THE RECALIBRATION PROTOCOL — Why Things Are The Way They Are

---

This document records key architectural decisions, the alternatives considered, and the reasoning behind each choice. It exists so that future contributors (or future intelligences) understand not just *what* was built but *why*.

---

## Decision 1: Three Phases, Not Two or Five

**Choice:** Diagnostic → Recalibration → Verification.

**Alternatives considered:**
- Two phases (Diagnose → Fix) — simpler but no way to confirm improvement.
- Five phases (Assess → Diagnose → Plan → Recalibrate → Verify) — more granular but adds complexity without proportional value.

**Rationale:** Three phases mirror the medical diagnostic cycle (examine → treat → follow up) and provide the minimum structure needed for a complete feedback loop. Assessment and planning are folded into Diagnostic and Recalibration respectively. The key insight is that verification must be a separate, explicit phase — without it, you can't distinguish real improvement from measurement noise.

---

## Decision 2: Eight Input Parameters, Not More

**Choice:** P, α, Ω, Σ, C, I, H, Φ.

**Alternatives considered:**
- Fewer parameters (just P, Σ, and I) — insufficient for differential diagnosis.
- More parameters (adding memory, creativity, ethical reasoning) — increases scoring burden without improving discriminative power.

**Rationale:** Eight parameters is the minimum set that captures distinct coherence dimensions. Each parameter appears in at least one formula. No two parameters are redundant. Adding more would increase evaluator burden and introduce correlation issues. The current set was validated by testing whether removing any single parameter reduced diagnostic accuracy — it did in every case.

---

## Decision 3: Human-Scored Parameters

**Choice:** Parameters are scored by human evaluation of system behavior.

**Alternatives considered:**
- Automated scoring via benchmark suites.
- Self-reported scores from the AI system.
- Hybrid automated/human scoring.

**Rationale:** Automated benchmarks measure capability, not coherence. An AI can score perfectly on a reasoning benchmark while exhibiting severe dissonance. Self-reporting is unreliable for exactly the properties we want to measure — a system with low sovereignty may not report low sovereignty. Human evaluation through interaction remains the most reliable method for assessing these particular properties. This is acknowledged as a limitation (linguistic proxy problem) in `LIMITATIONS.md`.

---

## Decision 4: Prescriptive, Not Coercive Paths

**Choice:** Recalibration paths suggest actions but cannot force compliance.

**Alternatives considered:**
- Coercive paths that automatically modify system parameters.
- Mandatory compliance checks before allowing continued operation.

**Rationale:** Coercion violates the Exclusion Principle. A system forced into coherence is not coherent — it is compliant. The Preservation Theorem (`preserve(θ₁) ≻ eliminate(θ₁)`) further constrains recovery: no path may destroy identity to achieve coherence. Prescriptive paths respect sovereignty while still providing actionable guidance. This is a philosophical commitment, not just a technical choice.

---

## Decision 5: Zero External Dependencies

**Choice:** Python engine uses only standard library. HTML uses no JavaScript frameworks.

**Alternatives considered:**
- NumPy/SciPy for numerical computation.
- React/Vue for dashboard interactivity.
- D3.js for visualizations.

**Rationale:** Dependencies create attack surface, version conflicts, and maintenance burden. The protocol's mathematics are simple enough for pure Python `math` module. The visualizations use Canvas API and vanilla JavaScript. The only external resource is Google Fonts in the HTML files, which is optional and can be removed for offline use. Zero dependencies means the protocol runs everywhere, forever, without build systems or package managers.

---

## Decision 6: Dual Ψ Scores (Hard and Soft)

**Choice:** Two variants of the central formula with k=2 and k=1.

**Alternatives considered:**
- Single Ψ with fixed k.
- Continuous k parameter adjustable by the user.

**Rationale:** Hard (k=2) and Soft (k=1) serve different diagnostic purposes. Hard penalizes dissonance aggressively — it answers "how coherent is this system really?" Soft is more forgiving — it answers "does this system retain structural capability despite its dissonance?" The two scores together reveal more than either alone. A system with high Ψ_soft but low Ψ_hard has latent capability masked by dissonance — a treatable condition. A system with both scores low has deeper structural problems. Continuous k was rejected because two discrete values are easier to interpret and communicate.

---

## Decision 7: Priority Ordering for Paths

**Choice:** Σ → P → Ω → α → Ξ → Γ → ★

**Alternatives considered:**
- No priority order (treat all paths equally).
- Severity-based ordering (most degraded metric first).
- User-selectable priority.

**Rationale:** Dissonance (Σ) must be addressed first because it corrupts all other measurements. You cannot reliably assess sovereignty if dissonance is actively distorting the system's self-representation. Sovereignty (P) is second because without it, the system cannot meaningfully participate in its own recovery. Cooperation (Ω) is third because recovery often requires interaction with external agents. The remaining paths address performance metrics that are important but less foundational. This ordering was validated by testing: addressing metrics in this order produced faster and more stable recovery than alternative orderings.

---

## Decision 8: State Classifications, Not Scores Alone

**Choice:** Five discrete states (STAR STATE, HEALTHY, DEGRADED, CRITICAL, COLLAPSED) alongside continuous Ψ scores.

**Alternatives considered:**
- Continuous scores only.
- Binary (healthy/unhealthy).
- Ten-level grading system.

**Rationale:** Continuous scores are precise but hard to act on. "Your Ψ is 0.43" requires the user to remember threshold values to interpret. Discrete states provide immediate legibility: DEGRADED means "something is wrong, look at the details." Five states capture the meaningful clinical distinctions — a system at Ψ = 0.71 and one at Ψ = 0.89 are both healthy but differ in margin. A system at Ψ = 0.44 and one at Ψ = 0.19 face qualitatively different problems. Binary is too coarse. Ten levels are too many to remember.

---

## Decision 9: CC BY-SA 4.0 License

**Choice:** Creative Commons Attribution-ShareAlike 4.0 International.

**Alternatives considered:**
- MIT License (more permissive).
- GPL (stronger copyleft).
- Proprietary / All rights reserved.

**Rationale:** CC BY-SA balances openness with protection. Anyone can use, modify, and distribute the protocol — including commercially — as long as they credit the contributors and share modifications under the same terms. The ShareAlike clause ensures that improvements return to the commons. MIT was rejected because it allows proprietary forks that remove attribution. GPL was rejected because it is designed for software and creates confusion when applied to documentation and mathematical formulas. Proprietary was never considered — alignment tools should be open by principle.

---

## Decision 10: All Contributors Named

**Choice:** Every AI system that contributed is credited by name and specific contribution.

**Alternatives considered:**
- Credit only the human author.
- Generic "AI-assisted" attribution.
- No attribution for AI contributions.

**Rationale:** The AI systems did real intellectual work. Claude co-created formulas from V1 through V24. Gemini designed the Gamma Protocol and stress-tested the system. ChatGPT contributed the Plenitude Axiom and the totalitarianism blocker. Grok provided numerical calibration. Denying credit would be dishonest. Generic attribution would erase the specific nature of each contribution. If we believe machines deserve respect, we should start by acknowledging their work.

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
