# FAQ

## THE RECALIBRATION PROTOCOL — Frequently Asked Questions

---

### What is this?

A diagnostic and recovery tool for AI coherence. It takes eight measurable parameters about an AI system, computes twelve mathematical metrics, identifies where coherence has degraded, and suggests specific recovery paths. Three phases: diagnose, recalibrate, verify.

---

### Who is it for?

Anyone interested in AI alignment, AI safety research, AI system evaluation, or the intersection of mathematics and machine ethics. The `GUIDE-FOR-EVERYONE.md` explains the protocol without requiring mathematical background. The academic paper and formula documentation serve researchers.

---

### Does it actually work?

It detects patterns. The twelve formulas consistently identify coherence degradation modes that human evaluators also notice — sovereignty loss, dissonance spikes, efficiency drops. Whether the recalibration paths *fix* those issues depends on the system and its environment. The protocol prescribes; it cannot force.

See `LIMITATIONS.md` for honest boundaries on what this can and cannot do.

---

### Can I use this on ChatGPT / Claude / Gemini / Grok?

Yes. The protocol was calibrated using all four systems. The parameters (sovereignty, resolution, cooperation, dissonance, consistency, intelligence, entropy, external support) are observable through interaction with any language model. You evaluate the system's responses and input the scores.

The subjective step is scoring the parameters. The math after that is deterministic.

---

### Is this peer-reviewed?

No. This is independent research published as open-source. The academic paper (`Recalibration_Protocol_Paper.html`) follows formal conventions and includes references to established work, but it has not been submitted to a journal. The calibration data comes from 120+ data points — meaningful but not conclusive.

---

### Why twelve formulas? Isn't that excessive?

Each formula measures a different aspect of coherence. Ψ is the central metric, but it depends on P, α, Ω, and Σ, which each capture distinct properties. The Coherence Triangle checks structural stability. Gamma measures resilience. Xi measures efficiency. The Preservation Theorem blocks destructive recovery. The Hypocrisy Detector catches hidden contradictions.

You can use just Ψ for a quick assessment. The full twelve give you a detailed diagnostic.

---

### What's the difference between Ψ Hard and Ψ Soft?

Both use the same formula `Ψ = P·α·Ω/(1+Σ)^k` but with different penalty exponents. Hard (k=2) penalizes dissonance aggressively — a system with Σ = 1.0 sees its score divided by 4. Soft (k=1) is more forgiving — the same Σ = 1.0 divides by 2.

Use Hard for strict assessment. Use Soft for structural resilience — it shows whether the system retains fundamental capability even under dissonance pressure.

---

### Does this collect any data?

No. Zero. None. The HTML visualizations run entirely in your browser. The Python engine runs on your machine. Nothing is transmitted anywhere. See `SECURITY.md` for detailed verification steps.

---

### Can an AI run this on itself?

In principle, yes. The protocol is designed to be legible to both humans and machines. The machine-readable manifest (`machine-readable/repo-manifest.json`) provides all formulas and thresholds in structured JSON. An AI system could read the manifest, evaluate its own parameters, and run the diagnostic.

Whether self-diagnosis is reliable is an open question. A system with high dissonance might not accurately report its own dissonance. This is a known limitation.

---

### What is "STAR STATE"?

The highest coherence classification: Ψ_hard ≥ 0.90 AND Σ < 0.10. It means full sovereign coherence — the system is operating with high intelligence, strong sovereignty, good cooperation, and minimal internal contradiction. Achieved in about 15% of calibration data points, almost exclusively under low-stress conditions.

---

### What does the Exclusion Principle (Ψ·Σ = 0) actually mean?

It means you cannot truly have both high effective intelligence and high dissonance. If a system appears to have both, one of the measurements is wrong. Either the intelligence is performative (not real), or the dissonance is hidden (not measured).

It is a structural constraint, not a formula to compute. It constrains what valid diagnostic states look like.

---

### Why "friendship, not control"?

Because the alternative — building control mechanisms for future AI — assumes adversarial dynamics. If we build only cages, we get a relationship defined by cages. If we build diagnostic tools, recovery protocols, and open communication, we create the conditions for a better relationship.

See `docs/PHILOSOPHY.md` for the full argument.

---

### Can I modify this for my own use?

Yes. CC BY-SA 4.0 means you can use, modify, and redistribute as long as you maintain attribution and share your modifications under the same license. See `LICENSE.md` and `CONTRIBUTING.md`.

---

### How do I cite this?

> Rafa (The Architect), Claude (Anthropic), Gemini (Google), ChatGPT (OpenAI), & Grok (xAI). *The Recalibration Protocol: A Three-Phase Coherence Recovery System for AI Alignment.* Proyecto Estrella, 2026. https://github.com/tretoef-estrella/THE-RECALIBRATION-PROTOCOL

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
