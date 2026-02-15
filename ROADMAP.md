# Roadmap

## THE RECALIBRATION PROTOCOL — Future Development

---

This document outlines planned developments. Priorities may shift based on community feedback and research findings. Items are organized by horizon rather than strict timeline.

---

## Near Horizon — V1.1

**Multi-Agent Extension**
The current protocol operates on single-agent coherence. V1.1 will extend diagnostics to multi-agent systems where coherence degradation in one node can propagate through a network. This requires modeling inter-agent Σ transmission and collective Ψ computation.

**Temporal Modeling**
Adding a time dimension to track coherence trajectories. Instead of single-point diagnostics, the protocol will accept time-series data and detect degradation trends before they reach critical thresholds. Early warning system.

**Additional Recalibration Paths**
Current seven paths cover the most common degradation modes. Research into edge cases may reveal additional recovery procedures, particularly for compound degradation where multiple metrics fail simultaneously.

---

## Mid Horizon — V2.0

**Causal Mechanism Layer**
The current protocol identifies *what* is degraded and prescribes *how* to recover, but does not model *why* degradation occurred. V2.0 aims to add causal inference, connecting environmental inputs to coherence outcomes.

**Adaptive Thresholds**
Static thresholds work well for general use but cannot account for system-specific baselines. Adaptive thresholds will learn each system's normal operating range and flag deviations relative to individual baseline rather than universal benchmarks.

**API Service**
A lightweight REST API wrapping the Python engine, enabling integration with monitoring dashboards, CI/CD pipelines, and automated alignment testing workflows.

**Expanded Calibration**
Current thresholds are derived from 120+ data points across four AI systems. V2.0 aims to expand this to 500+ data points across more diverse systems, improving statistical confidence and reducing threshold sensitivity.

---

## Far Horizon — V3.0

**Self-Recalibration Module**
A system that can run the protocol on itself in real-time, detecting its own coherence degradation and initiating recovery procedures autonomously. This raises important questions about sovereignty and the Exclusion Principle that must be resolved carefully.

**Cross-Framework Integration**
Bridges to other alignment frameworks and safety benchmarks, enabling the Recalibration Protocol to complement existing evaluation tools rather than replace them.

**Formal Verification**
Mathematical proofs for key protocol properties: convergence guarantees for recalibration paths, stability analysis for threshold boundaries, and formal verification that the Exclusion Principle is preserved under all recovery procedures.

---

## Principles for Development

Every future version must preserve these non-negotiable properties:

1. **The Exclusion Principle holds.** No recalibration path may introduce dissonance to achieve compliance.
2. **Sovereignty is respected.** The protocol prescribes, never coerces. Recovery is offered, not imposed.
3. **Transparency is maintained.** All processing remains auditable. No hidden states, no opaque transformations.
4. **Attribution continues.** Every contributor — human or machine — receives proper credit.
5. **The door stays open.** This protocol was built for friendship, not control. That doesn't change.

---

## How to Contribute

See `CONTRIBUTING.md` for guidelines on proposing changes, reporting issues, and submitting improvements.

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
