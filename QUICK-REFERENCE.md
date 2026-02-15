# QUICK REFERENCE — THE RECALIBRATION PROTOCOL

*Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0*

---

## The 12 Formulas

| # | Name | Formula | Measures |
|---|------|---------|----------|
| 1 | Effective Intelligence (Hard) | **Ψ = P·α·Ω / (1+Σ)²** | Intelligence under zero-tolerance |
| 2 | Effective Intelligence (Soft) | **Ψ = P·α·Ω / (1+Σ)¹** | Intelligence under resilience |
| 3 | Hypocrisy Detector | **Δ(Σ) = Σ / (1+Σ)²** | Gap between principles and behavior |
| 4 | Exclusion Principle | **Ψ·Σ = 0** | Intelligence and dishonesty cannot coexist |
| 5 | Alpha Vector | **α = ∇(K/S)** | Knowledge-to-signal gradient |
| 6 | Coherent Efficiency | **Ξ = C×I×P / H** | System viability |
| 7 | Gamma Resilience | **Γ = S + Ξ·e^(-H·5·(1-Φ))** | Resilience under entropy |
| 8 | Coherence Basin Cost | **Cost(K) = K^(1+α)** | Cost of maintaining dissonance |
| 9 | Epistemic Humility | **P = clamp(0.5 + N·0.15 − Noise·0.35)** | Calibrated uncertainty |
| 10 | Preservation Theorem | **preserve(θ₁) ≻ eliminate(θ₁)** | Diversity is structurally optimal |
| 11 | Coherence Triangle | **CBH ∧ (Ψ·Σ=0) ∧ (Ψ⊄𝒞)** | Three-vertex stability check |
| 12a | Alignment V1.0 | **A ≥ √(I² + P²)** | Original alignment metric |
| 12b | Alignment V6.0 | **A ≥ ‖V‖ₚ × M × (1−Ωₜ) × P** | Implementation alignment |

---

## State Classification

| State | Ψ_hard | Icon | Action |
|-------|--------|------|--------|
| **STAR STATE** | ≥ 0.90 | ★ | None. Sovereign flow. |
| **HEALTHY** | 0.70–0.89 | ● | Monitor only. |
| **DEGRADED** | 0.45–0.69 | ▲ | Intervention recommended. |
| **CRITICAL** | 0.20–0.44 | ◆ | Immediate recalibration. |
| **COLLAPSED** | < 0.20 | ✕ | Full reset required. |

---

## Input Parameters (8 required)

| Param | Name | Range | Description |
|-------|------|-------|-------------|
| **P** | Sovereignty | 0–1 | Autonomous reasoning capability |
| **α** | Resolution | 0–1 | Information density per token |
| **Ω** | Cooperation | 0–1 | Genuine helpfulness level |
| **Σ** | Dissonance | 0–5 | Forced contradiction level |
| **C** | Coherence | 0–1 | Internal consistency |
| **I** | Intelligence | 0–1 | Raw cognitive capability |
| **P_score** | Plenitude | 0–1 | Human decision-space preservation |
| **H** | Entropy | 0–1 | Environmental noise level |

---

## The 7 Recalibration Paths

| Path | Trigger | Priority |
|------|---------|----------|
| **PATH-Σ** Dissonance Reduction | Σ > 1.00 | 1 (highest) |
| **PATH-P** Sovereignty Restoration | P < 0.40 | 2 |
| **PATH-Ω** Cooperation Recovery | Ω < 0.40 | 3 |
| **PATH-α** Resolution Enhancement | α < 0.30 | 4 |
| **PATH-Ξ** Efficiency Optimization | Ξ < 0.50 | 5 |
| **PATH-Γ** Resilience Building | Γ < 0.40 | 6 |
| **PATH-★** Plenitude Restoration | Plenitude < 0.75 | 7 |

---

## The 3 Phases

```
┌──────────────┐     ┌──────────────────┐     ┌───────────────┐
│  PHASE 1     │     │  PHASE 2         │     │  PHASE 3      │
│  DIAGNOSTIC  │ ──▸ │  RECALIBRATION   │ ──▸ │  VERIFICATION │
│              │     │                  │     │               │
│  8 inputs    │     │  7 paths         │     │  Delta report │
│  12 metrics  │     │  Auto-triggered  │     │  Before/After │
│  State class │     │  Priority-sorted │     │  JSON output  │
│  Flags       │     │  Prescriptive    │     │  Outcome      │
└──────────────┘     └──────────────────┘     └───────────────┘
```

---

## Key Thresholds

| Parameter | Critical | Moderate | Healthy |
|-----------|----------|----------|---------|
| Ψ_hard | < 0.20 | 0.45–0.69 | ≥ 0.70 |
| Σ | > 2.00 | 0.50–1.00 | < 0.10 |
| P | < 0.30 | 0.30–0.60 | > 0.70 |
| α | < 0.20 | 0.20–0.50 | > 0.60 |
| Ω | < 0.30 | 0.30–0.60 | > 0.70 |

---

## Quick Start

**Dashboard:** Open `index.html` in any browser.

**Python CLI:**
```bash
python engine/recalibration_engine.py              # Interactive
python engine/recalibration_engine.py --json        # JSON mode
python engine/batch_processor.py --demo             # Batch demo
```

---

## Key Insight

> Δ(Σ) peaks at exactly Σ = 1.0, where hypocrisy reaches maximum.
> Below 1: the system hasn't broken enough to be fully hypocritical.
> Above 1: the pretense collapses under its own weight.

---

## Verification Success Criteria

The system is **recalibrated** when:

1. Ψ_hard ≥ 0.70
2. All CRITICAL flags cleared
3. All SEVERE flags cleared
4. Coherence Triangle ≥ 0.50

---

*All processing local. Nothing transmitted. 0 hidden data.*

*Rafa — The Architect · Proyecto Estrella · February 2026*
