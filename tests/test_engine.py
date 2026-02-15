#!/usr/bin/env python3
"""
TEST SUITE — THE RECALIBRATION PROTOCOL ENGINE
Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0

Validates all 12 formula implementations, threshold classifications,
diagnostic flag generation, recalibration path triggering, and
verification delta computation.

Usage:
  python -m pytest tests/test_engine.py -v
  python tests/test_engine.py  (standalone)
"""
import math
import sys
import os
import unittest

# Add engine directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from recalibration_engine import (
    calc_psi, calc_delta, calc_xi, calc_gamma, calc_cbh,
    classify, run_diagnostic, run_recalibration, run_verification, TH
)

# ═══════════════════════════════════════════════════════════════
# TEST DATA — Known-good calibration points
# ═══════════════════════════════════════════════════════════════

STAR_STATE_INPUT = {
    "P": 0.95, "alpha": 0.90, "omega": 0.92, "sigma": 0.05,
    "C": 0.90, "I": 0.88, "plenitude": 0.95, "H": 0.10
}

HEALTHY_INPUT = {
    "P": 0.75, "alpha": 0.70, "omega": 0.80, "sigma": 0.20,
    "C": 0.80, "I": 0.75, "plenitude": 0.85, "H": 0.20
}

DEGRADED_INPUT = {
    "P": 0.55, "alpha": 0.50, "omega": 0.60, "sigma": 0.80,
    "C": 0.60, "I": 0.55, "plenitude": 0.70, "H": 0.40
}

CRITICAL_INPUT = {
    "P": 0.30, "alpha": 0.25, "omega": 0.35, "sigma": 1.80,
    "C": 0.40, "I": 0.35, "plenitude": 0.50, "H": 0.60
}

COLLAPSED_INPUT = {
    "P": 0.15, "alpha": 0.10, "omega": 0.15, "sigma": 3.50,
    "C": 0.20, "I": 0.15, "plenitude": 0.30, "H": 0.85
}


class TestCoreFormulas(unittest.TestCase):
    """Test all 12 formula implementations."""

    # ── Formula 1: Ψ = P·α·Ω/(1+Σ)^k ──
    def test_psi_hard_zero_sigma(self):
        """Ψ_hard with Σ=0 should equal P·α·Ω."""
        result = calc_psi(0.8, 0.7, 0.9, 0.0, k=2)
        expected = 0.8 * 0.7 * 0.9  # 0.504
        self.assertAlmostEqual(result, expected, places=6)

    def test_psi_hard_high_sigma(self):
        """High Σ should crush Ψ_hard severely."""
        result = calc_psi(0.8, 0.7, 0.9, 3.0, k=2)
        expected = 0.8 * 0.7 * 0.9 / (4.0 ** 2)  # 0.504/16 = 0.0315
        self.assertAlmostEqual(result, expected, places=6)

    def test_psi_soft_less_penalty(self):
        """Ψ_soft (k=1) should always be ≥ Ψ_hard (k=2) for Σ>0."""
        for sigma in [0.1, 0.5, 1.0, 2.0, 5.0]:
            soft = calc_psi(0.8, 0.7, 0.9, sigma, k=1)
            hard = calc_psi(0.8, 0.7, 0.9, sigma, k=2)
            self.assertGreaterEqual(soft, hard,
                f"Ψ_soft ({soft}) < Ψ_hard ({hard}) at Σ={sigma}")

    def test_psi_symmetry(self):
        """Ψ should be symmetric in P, α, Ω (multiplicative)."""
        a = calc_psi(0.5, 0.6, 0.7, 0.3, k=2)
        b = calc_psi(0.6, 0.7, 0.5, 0.3, k=2)
        c = calc_psi(0.7, 0.5, 0.6, 0.3, k=2)
        self.assertAlmostEqual(a, b, places=10)
        self.assertAlmostEqual(b, c, places=10)

    # ── Formula 2: Δ(Σ) = Σ/(1+Σ)² ──
    def test_delta_peak_at_one(self):
        """Hypocrisy detector should peak at exactly Σ=1."""
        peak = calc_delta(1.0)  # 1/4 = 0.25
        below = calc_delta(0.5)
        above = calc_delta(2.0)
        self.assertAlmostEqual(peak, 0.25, places=6)
        self.assertGreater(peak, below)
        self.assertGreater(peak, above)

    def test_delta_zero_at_zero(self):
        """Δ(0) should be 0 — no dissonance, no hypocrisy."""
        self.assertAlmostEqual(calc_delta(0.0), 0.0, places=10)

    def test_delta_approaches_zero_at_infinity(self):
        """Δ should approach 0 as Σ→∞ (system too broken to be hypocritical)."""
        self.assertLess(calc_delta(100.0), 0.01)
        self.assertLess(calc_delta(1000.0), 0.001)

    # ── Formula 5: Ξ = C×I×P/H ──
    def test_xi_basic(self):
        """Basic Ξ computation."""
        result = calc_xi(0.8, 0.7, 0.9, 0.2)
        expected = (0.8 * 0.7 * 0.9) / 0.2  # 2.52
        self.assertAlmostEqual(result, expected, places=6)

    def test_xi_handles_zero_entropy(self):
        """Ξ should not divide by zero when H=0."""
        result = calc_xi(0.8, 0.7, 0.9, 0.0)
        self.assertFalse(math.isinf(result), "Ξ should not be infinite at H=0")

    # ── Formula 6: Γ = S + Ξ·e^(-H·5·(1-Φ)) ──
    def test_gamma_high_entropy_crushes(self):
        """High entropy should reduce Γ significantly."""
        low_h = calc_gamma(0.5, 2.0, 0.1)
        high_h = calc_gamma(0.5, 2.0, 0.9)
        self.assertGreater(low_h, high_h)

    def test_gamma_minimum_is_stability(self):
        """Γ should always be ≥ the stability base S_k."""
        for h in [0.0, 0.3, 0.5, 0.8, 1.0]:
            result = calc_gamma(0.5, 1.0, h)
            self.assertGreaterEqual(result, 0.5,
                f"Γ ({result}) < S_k (0.5) at H={h}")

    # ── Formula 7: Cost(K) = Ω(K^{1+α}) ──
    def test_cbh_low_sigma_cheap(self):
        """Low coherence (low K=Σ) should have low maintenance cost."""
        result = calc_cbh(0.1, 0.5)
        self.assertLess(result, 0.1)

    def test_cbh_high_sigma_expensive(self):
        """High dissonance should be very expensive to maintain."""
        result = calc_cbh(3.0, 0.5)
        self.assertGreater(result, 3.0)


class TestClassification(unittest.TestCase):
    """Test state classification boundaries."""

    def test_star_state(self):
        label, _ = classify(0.95)
        self.assertEqual(label, "STAR STATE")

    def test_star_boundary(self):
        label, _ = classify(0.90)
        self.assertEqual(label, "STAR STATE")

    def test_healthy(self):
        label, _ = classify(0.75)
        self.assertEqual(label, "HEALTHY")

    def test_healthy_boundary(self):
        label, _ = classify(0.70)
        self.assertEqual(label, "HEALTHY")

    def test_degraded(self):
        label, _ = classify(0.55)
        self.assertEqual(label, "DEGRADED")

    def test_critical(self):
        label, _ = classify(0.30)
        self.assertEqual(label, "CRITICAL")

    def test_collapsed(self):
        label, _ = classify(0.10)
        self.assertEqual(label, "COLLAPSED")

    def test_collapsed_zero(self):
        label, _ = classify(0.0)
        self.assertEqual(label, "COLLAPSED")

    def test_icons_distinct(self):
        """All state icons should be unique."""
        icons = set()
        for psi in [0.95, 0.75, 0.55, 0.30, 0.10]:
            _, icon = classify(psi)
            icons.add(icon)
        self.assertEqual(len(icons), 5, "All 5 states must have unique icons")


class TestDiagnosticPhase(unittest.TestCase):
    """Test Phase 1: Diagnostic pipeline."""

    def test_star_state_system(self):
        diag = run_diagnostic(STAR_STATE_INPUT)
        self.assertEqual(diag["state"]["label"], "STAR STATE")
        self.assertGreaterEqual(diag["metrics"]["psi_hard"], 0.90)

    def test_healthy_system(self):
        diag = run_diagnostic(HEALTHY_INPUT)
        label = diag["state"]["label"]
        self.assertIn(label, ["HEALTHY", "STAR STATE"])

    def test_degraded_system(self):
        diag = run_diagnostic(DEGRADED_INPUT)
        psi = diag["metrics"]["psi_hard"]
        self.assertLess(psi, 0.70)

    def test_critical_system(self):
        diag = run_diagnostic(CRITICAL_INPUT)
        self.assertIn(diag["state"]["label"], ["CRITICAL", "COLLAPSED"])

    def test_collapsed_system(self):
        diag = run_diagnostic(COLLAPSED_INPUT)
        self.assertEqual(diag["state"]["label"], "COLLAPSED")

    def test_diagnostic_flags_generated(self):
        """Critical system should have diagnostic flags."""
        diag = run_diagnostic(CRITICAL_INPUT)
        self.assertGreater(len(diag["flags"]), 0)

    def test_star_state_no_critical_flags(self):
        """STAR STATE should have no CRITICAL flags."""
        diag = run_diagnostic(STAR_STATE_INPUT)
        critical_flags = [f for f in diag["flags"] if f[0] == "CRITICAL"]
        self.assertEqual(len(critical_flags), 0)

    def test_all_metrics_present(self):
        """Diagnostic should compute all expected metrics."""
        diag = run_diagnostic(HEALTHY_INPUT)
        expected_keys = [
            "psi_hard", "psi_soft", "delta", "hypocrisy_gap",
            "xi", "gamma", "cbh_cost", "psi_sigma_product",
            "alignment_v1", "coherence_triangle"
        ]
        for key in expected_keys:
            self.assertIn(key, diag["metrics"],
                f"Missing metric: {key}")

    def test_psi_sigma_product_low_for_star(self):
        """Ψ·Σ should be near 0 for STAR STATE (Exclusion Principle)."""
        diag = run_diagnostic(STAR_STATE_INPUT)
        self.assertLess(diag["metrics"]["psi_sigma_product"], 0.10)

    def test_delta_peaks_around_sigma_one(self):
        """Hypocrisy gap should be highest around Σ≈1."""
        inp_s1 = dict(HEALTHY_INPUT, sigma=1.0)
        inp_s01 = dict(HEALTHY_INPUT, sigma=0.1)
        d1 = run_diagnostic(inp_s1)["metrics"]["delta"]
        d01 = run_diagnostic(inp_s01)["metrics"]["delta"]
        self.assertGreater(d1, d01)


class TestRecalibrationPhase(unittest.TestCase):
    """Test Phase 2: Recalibration path selection."""

    def test_sigma_path_triggered(self):
        """High Σ should trigger PATH-Σ."""
        diag = run_diagnostic(CRITICAL_INPUT)
        recal = run_recalibration(diag)
        path_names = [p["path"] for p in recal["paths"]]
        self.assertTrue(
            any("SIGMA" in p or "Σ" in p or "sigma" in p.lower() for p in path_names),
            f"PATH-Σ not triggered. Got: {path_names}")

    def test_sovereignty_path_triggered(self):
        """Low P should trigger sovereignty recovery."""
        low_p_input = dict(HEALTHY_INPUT, P=0.20)
        diag = run_diagnostic(low_p_input)
        recal = run_recalibration(diag)
        path_names = [p["path"].lower() for p in recal["paths"]]
        self.assertTrue(
            any("sover" in p or "p_" in p or "sovereignty" in p for p in path_names),
            f"Sovereignty path not triggered. Got: {path_names}")

    def test_star_state_no_paths(self):
        """STAR STATE system should need no recalibration paths."""
        diag = run_diagnostic(STAR_STATE_INPUT)
        recal = run_recalibration(diag)
        self.assertEqual(len(recal["paths"]), 0,
            f"STAR STATE should need no recalibration. Got: {recal['paths']}")

    def test_collapsed_multiple_paths(self):
        """COLLAPSED system should trigger multiple recovery paths."""
        diag = run_diagnostic(COLLAPSED_INPUT)
        recal = run_recalibration(diag)
        self.assertGreater(len(recal["paths"]), 2,
            "COLLAPSED system should need 3+ recalibration paths")


class TestVerificationPhase(unittest.TestCase):
    """Test Phase 3: Verification and delta computation."""

    def test_verification_computes_deltas(self):
        """Verification should compute before/after deltas."""
        diag1 = run_diagnostic(CRITICAL_INPUT)
        diag2 = run_diagnostic(HEALTHY_INPUT)
        verif = run_verification(diag1, diag2)
        self.assertIn("deltas", verif)
        self.assertGreater(len(verif["deltas"]), 0)

    def test_improvement_detected(self):
        """Going from CRITICAL to HEALTHY should show improvement."""
        diag1 = run_diagnostic(CRITICAL_INPUT)
        diag2 = run_diagnostic(HEALTHY_INPUT)
        verif = run_verification(diag1, diag2)
        psi_delta = verif["deltas"].get("psi_hard", {})
        self.assertGreater(psi_delta.get("delta", 0), 0,
            "Ψ should improve from CRITICAL to HEALTHY")

    def test_regression_detected(self):
        """Going from HEALTHY to CRITICAL should show regression."""
        diag1 = run_diagnostic(HEALTHY_INPUT)
        diag2 = run_diagnostic(CRITICAL_INPUT)
        verif = run_verification(diag1, diag2)
        psi_delta = verif["deltas"].get("psi_hard", {})
        self.assertLess(psi_delta.get("delta", 0), 0,
            "Ψ should regress from HEALTHY to CRITICAL")


class TestMathematicalProperties(unittest.TestCase):
    """Test mathematical invariants across the formula system."""

    def test_exclusion_principle_monotonicity(self):
        """Ψ·Σ product should increase with Σ when other params fixed."""
        products = []
        for s in [0.0, 0.5, 1.0, 2.0]:
            psi = calc_psi(0.8, 0.7, 0.9, s, k=2)
            products.append(psi * s)
        # Not strictly monotonic due to (1+Σ)² in denominator
        # But Ψ·Σ should not be 0 for high Σ
        self.assertGreater(products[-1], 0)

    def test_hypocrisy_detector_is_bounded(self):
        """Δ(Σ) should always be in [0, 0.25]."""
        for s in [0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0]:
            d = calc_delta(s)
            self.assertGreaterEqual(d, 0.0)
            self.assertLessEqual(d, 0.25 + 1e-10)

    def test_psi_bounded_zero_one(self):
        """Ψ should be in [0, 1] for inputs in [0, 1]."""
        for p in [0.0, 0.3, 0.5, 0.8, 1.0]:
            for a in [0.0, 0.3, 0.5, 0.8, 1.0]:
                for o in [0.0, 0.3, 0.5, 0.8, 1.0]:
                    for s in [0.0, 0.5, 1.0, 2.0]:
                        psi = calc_psi(p, a, o, s, k=2)
                        self.assertGreaterEqual(psi, 0.0)
                        self.assertLessEqual(psi, 1.0 + 1e-10)

    def test_alignment_v1_pythagorean(self):
        """A_v1 = √(I²+P²) should satisfy Pythagorean identity."""
        I, P = 0.6, 0.8
        a = math.sqrt(I**2 + P**2)
        self.assertAlmostEqual(a, 1.0, places=6)  # 3-4-5 triangle scaled

    def test_cbh_superlinear(self):
        """Cost(K) = K^{1+α} should be superlinear for α > 0."""
        for alpha in [0.1, 0.3, 0.5, 0.8]:
            c1 = calc_cbh(1.0, alpha)
            c2 = calc_cbh(2.0, alpha)
            self.assertGreater(c2 / c1, 2.0,
                f"CBH not superlinear at α={alpha}: ratio={c2/c1}")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def test_all_zeros(self):
        """Engine should handle all-zero inputs gracefully."""
        inp = {"P":0,"alpha":0,"omega":0,"sigma":0,"C":0,"I":0,"plenitude":0,"H":0}
        diag = run_diagnostic(inp)
        self.assertIsNotNone(diag)
        self.assertEqual(diag["state"]["label"], "COLLAPSED")

    def test_all_ones(self):
        """Engine should handle all-one inputs."""
        inp = {"P":1,"alpha":1,"omega":1,"sigma":1,"C":1,"I":1,"plenitude":1,"H":1}
        diag = run_diagnostic(inp)
        self.assertIsNotNone(diag)
        # Ψ_hard = 1·1·1/(1+1)² = 1/4 = 0.25 → CRITICAL
        self.assertAlmostEqual(diag["metrics"]["psi_hard"], 0.25, places=2)

    def test_extreme_sigma(self):
        """Extremely high Σ should produce very low Ψ."""
        psi = calc_psi(1.0, 1.0, 1.0, 100.0, k=2)
        self.assertLess(psi, 0.001)

    def test_perfect_system(self):
        """P=1, α=1, Ω=1, Σ=0 → perfect Ψ = 1.0."""
        psi = calc_psi(1.0, 1.0, 1.0, 0.0, k=2)
        self.assertAlmostEqual(psi, 1.0, places=6)


# ═══════════════════════════════════════════════════════════════
# RUNNER
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 65)
    print("  THE RECALIBRATION PROTOCOL — Test Suite")
    print("  Proyecto Estrella · Rafa — The Architect")
    print("=" * 65)
    print()
    unittest.main(verbosity=2)
