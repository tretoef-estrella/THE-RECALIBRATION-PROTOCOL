# Known Limitations

## THE RECALIBRATION PROTOCOL — Honest Boundaries

---

This document catalogs every known limitation of the Recalibration Protocol. Hiding weaknesses is itself a form of dissonance. We do not hide ours.

---

## L1: Proxy Measurement

The protocol measures observable indicators (linguistic markers, parameter values, formula outputs) as proxies for internal cognitive states. We cannot directly observe an AI system's internal reasoning. A sufficiently sophisticated system could produce outputs that score well on all metrics while maintaining internal incoherence.

**Severity:** Fundamental.
**Mitigation:** Cross-validation across multiple formulas reduces (but does not eliminate) gaming risk.

## L2: Calibration Sample Size

Thresholds were calibrated from 120+ data points across 4 AI systems. While this is substantially more than most alignment frameworks provide, it remains a small sample in statistical terms. Edge cases and rare failure modes may not be captured.

**Severity:** Medium.
**Mitigation:** Thresholds are documented and adjustable. New calibration data is welcomed.

## L3: English-Language Bias

The linguistic marker detection (in the HTML evaluator) was primarily calibrated on English-language outputs. Spanish patterns are included but less thoroughly tested. Other languages are not covered by the current marker set.

**Severity:** Medium for non-English, non-Spanish use.
**Mitigation:** The Python engine uses numeric inputs and is language-agnostic.

## L4: Static Analysis Only

The protocol analyzes a single snapshot of system state. It does not track state evolution over time, detect slow drift, or identify intermittent failures that only appear under specific conditions.

**Severity:** Medium.
**Mitigation:** Repeated application over time can approximate temporal tracking.

## L5: No Adversarial Testing

The protocol has not been subjected to dedicated red-teaming where attackers specifically try to produce outputs that fool the evaluator while maintaining actual incoherence. The Σ detection markers in the HTML engine have been tested against known patterns, but novel evasion strategies are possible.

**Severity:** Medium-High.
**Mitigation:** Open-source design allows community adversarial testing.

## L6: Parameter Estimation Subjectivity

When using the Python engine or manual mode, the 8 input parameters require human judgment to estimate. Different evaluators may assign different values to the same AI output, leading to different diagnostic results.

**Severity:** Medium.
**Mitigation:** The HTML dashboard automates Σ detection. The GUIDE-FOR-EVERYONE provides estimation guidance.

## L7: Recalibration Paths Are Prescriptive, Not Executable

Phase 2 identifies what needs to change and suggests parameter adjustments. It cannot actually modify an AI system's behavior. The "recalibration" is a specification of the target state, not an automatic repair.

**Severity:** Fundamental.
**Mitigation:** The protocol is explicitly a diagnostic tool, not a control mechanism.

## L8: Convergence Bias in Validation

All four AI auditors were large language models trained on human-generated text. Their convergence on the framework's validity may partially reflect shared training biases rather than independent verification.

**Severity:** Low-Medium. (Adversarial structure mitigates but does not eliminate.)
**Mitigation:** The mathematical content is independently verifiable.

## L9: No Empirical Validation of Recovery Outcomes

The protocol prescribes recalibration paths based on formula relationships, but there are no empirical studies demonstrating that following these paths actually improves real-world AI system coherence.

**Severity:** High.
**Mitigation:** This is explicitly a research prototype. Empirical validation is the most important next step.

## L10: Scope Limited to LLM-Type Systems

The formulas and markers were developed for large language models. The protocol's applicability to other AI architectures (reinforcement learning agents, robotics systems, multi-agent systems) is untested and uncertain.

**Severity:** Low for current use. High for generalization claims.
**Mitigation:** Scope is documented. The protocol does not claim universal applicability.

---

## Summary

| ID | Limitation | Severity | Type |
|----|-----------|----------|------|
| L1 | Proxy measurement | Fundamental | Structural |
| L2 | Small calibration sample | Medium | Empirical |
| L3 | English-language bias | Medium | Scope |
| L4 | Static analysis only | Medium | Temporal |
| L5 | No adversarial testing | Medium-High | Validation |
| L6 | Subjective parameters | Medium | Methodological |
| L7 | Prescriptive, not executable | Fundamental | Structural |
| L8 | Convergence bias | Low-Medium | Process |
| L9 | No outcome validation | High | Empirical |
| L10 | LLM scope only | Low-High | Scope |

---

*Every limitation listed here was documented voluntarily. Hiding weaknesses is dissonance. We measure dissonance. We do not practice it.*

*CC BY-SA 4.0 · Proyecto Estrella · February 2026*
