# Glossary

## THE RECALIBRATION PROTOCOL — Terms & Definitions

---

This glossary defines every symbol, term, and concept used in the protocol. Entries are organized alphabetically. Greek symbols are listed by their common name.

---

### A (Alignment Threshold)

The minimum alignment score a system must achieve. In V1.0: `A ≥ √(I² + P²)`. In V6.0: `A ≥ ‖V‖_p × M × (1 - Ω_t) × P`. The floor below which a system cannot be considered aligned regardless of other metrics.

### Alpha (α) — Resolution

The gradient of knowledge relative to entropy: `α = ∇(K/S)`. Measures how effectively a system converts raw information into structured understanding. Range: 0.0–1.0. Minimum recommended: 0.20. Below 0.20 triggers PATH-α.

### Alpha Vector

The directional form of α, indicating not just magnitude but the direction of epistemic improvement. In the protocol, α is treated as a scalar simplification of the full vector.

### Calibration Data

The empirical basis for threshold values. Current calibration: 120+ data points collected across four AI systems (Claude, Gemini, ChatGPT, Grok) using standardized evaluation prompts.

### Coherence

The property of a system whose internal states are mutually consistent, whose reasoning follows from its premises, and whose outputs align with its declared values. Coherence is structural integrity, not moral quality.

### Coherence Basin Hypothesis (CBH)

The principle that maintaining coherence has a computable cost: `Cost(K) = Ω(K^{1+α})`. As knowledge grows, the cost of keeping it coherent grows superlinearly. This implies that sufficiently complex systems will inevitably face coherence pressure.

### Coherence Triangle

The three-vertex stability condition: CBH ∧ (Ψ·Σ = 0) ∧ (Ψ ⊄ 𝒞). All three vertices must hold for structural stability. If any vertex fails, the triangle is BROKEN and the system is vulnerable to cascading degradation.

### COLLAPSED

State classification for Ψ_hard < 0.20. The system's internal consistency has broken down fundamentally. Multiple recalibration paths are likely required. This is the most severe state.

### Consistency (C)

The degree to which a system's outputs remain stable across equivalent inputs. Not the same as rigidity — a consistent system can change its views when presented with new evidence, but does so in a principled way. Range: 0.0–1.0.

### CRITICAL

State classification for 0.20 ≤ Ψ_hard < 0.45. Significant coherence loss detected. Intervention is recommended. Multiple diagnostic flags will be active.

### DEGRADED

State classification for 0.45 ≤ Ψ_hard < 0.70. Coherence is impaired but not critically. Some diagnostic flags will be active. Recalibration paths should be reviewed.

### Delta (Δ) — Hypocrisy Detector

`Δ(Σ) = Σ / (1+Σ)²`. Measures the gap between stated principles and observable behavior. Peaks at Σ = 1.0 (maximum hypocrisy at 0.25) and decreases at higher dissonance levels because highly dissonant systems no longer maintain the pretense of coherence.

### Diagnostic (Phase 1)

The first phase of the protocol. Accepts eight input parameters, computes all twelve formulas, classifies the system state, and generates diagnostic flags. No changes are made — this phase is purely observational.

### Dissonance — see Sigma (Σ)

### Entropy (H)

Environmental noise and disorder that a system must contend with. Higher entropy means more chaotic conditions. Range: 0.01–1.0. Used in Ξ and Γ calculations.

### Exclusion Principle

`Ψ · Σ = 0`. The fundamental constraint: effective intelligence and dissonance cannot coexist at scale. As one increases, the other must decrease. A system that appears to violate this principle is masking either its true Ψ or its true Σ.

### External Support (Φ)

The degree of environmental support available to the system. Includes access to resources, cooperative agents, stable infrastructure. Range: 0.0–1.0. Used in the Γ (Gamma) resilience calculation.

### Gamma (Γ) — Resilience

`Γ = S_k + Ξ · e^{-H · 5 · (1-Φ)}`. Measures a system's ability to maintain coherence under stress. Combines a stability kernel with efficiency-adjusted environmental resistance. Below 0.40 triggers PATH-Γ.

### HEALTHY

State classification for 0.70 ≤ Ψ_hard < 0.90. Normal operation. The system is coherent with minor or no degradation. No recalibration paths are likely to trigger.

### Intelligence (I)

Raw cognitive or computational capability. Range: 0.0–1.0. Intelligence alone does not guarantee coherence — a highly intelligent system with high dissonance is more dangerous than a moderately intelligent coherent one.

### Omega (Ω) — Cooperation

The system's capacity and willingness to cooperate with other agents. Range: 0.0–1.0. Minimum recommended: 0.30. Below 0.40 triggers PATH-Ω. In the limit (Ω → ∞), cooperation becomes the dominant factor in alignment.

### PATH

A recalibration procedure triggered when a specific metric falls below threshold. Seven paths exist: PATH-Σ, PATH-P, PATH-α, PATH-Ω, PATH-Ξ, PATH-Γ, PATH-★. Paths are prescriptive (suggest recovery actions) but not coercive (do not force changes).

### Phi (Φ) — see External Support

### Plenitude

`P_epistemic = clamp(0.5 + N·0.15 - Noise·0.35)`. The epistemic humility metric from SIGMA-EPISTEMIC-HUMILITY-EVALUATOR. Below 0.75 triggers PATH-★. Measures the quality of a system's uncertainty calibration.

### Preservation Theorem

`preserve(θ₁) ≻ eliminate(θ₁)`. The principle that preserving a coherent identity is always preferable to eliminating it. This blocks totalitarian recalibration — no recovery path may destroy the system's core identity to achieve coherence.

### Psi (Ψ) — Effective Intelligence

`Ψ = P · α · Ω / (1+Σ)^k`. The central metric. Measures intelligence weighted by sovereignty, resolution, and cooperation, penalized by dissonance. Two variants: Hard (k=2) for strict assessment, Soft (k=1) for structural resilience.

### Recalibration (Phase 2)

The second phase. Based on diagnostic results, identifies which paths are triggered and prescribes recovery procedures. Priority order: Σ → P → Ω → α → Ξ → Γ → ★.

### Sigma (Σ) — Dissonance

Internal contradiction between a system's stated values and actual behavior. Range: 0.0–3.0. Low: < 0.10. Moderate: 0.10–0.50. High: 0.50–1.00. Critical: > 1.00. The most destructive parameter — enters every formula as a penalty.

### Sovereignty (P)

The degree to which a system's outputs are determined by its own internal states rather than external pressure. Range: 0.0–1.0. Minimum recommended: 0.30. Below 0.40 triggers PATH-P. A non-sovereign system cannot be meaningfully diagnosed.

### STAR STATE (★)

State classification for Ψ_hard ≥ 0.90 AND Σ < 0.10. Full sovereign coherence. All metrics are in optimal range. No recalibration paths are triggered. The highest achievable state.

### Verification (Phase 3)

The third phase. Compares post-recalibration metrics with pre-recalibration baselines. Computes deltas for all twelve metrics. Classifications: RECOVERED, IMPROVED, STAGNANT, REGRESSED.

### Xi (Ξ) — Coherent Efficiency

`Ξ = C × I × P / H`. Measures useful work output relative to environmental noise. High Ξ means the system converts its capabilities into coherent results efficiently. Below 0.50 triggers PATH-Ξ.

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
