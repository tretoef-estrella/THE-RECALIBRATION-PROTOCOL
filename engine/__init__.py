"""
THE RECALIBRATION PROTOCOL — Engine Package
============================================

A three-phase coherence recovery system integrating 12 Proyecto Estrella formulas.

Modules:
    recalibration_engine : Core 3-phase diagnostic, recalibration, and verification
    validator            : Input validation and constraint checking
    export_utils         : Report generation in JSON, CSV, and Markdown formats
    batch_processor      : Batch processing for multiple system evaluations

Usage:
    from engine.recalibration_engine import RecalibrationEngine
    from engine.validator import validate_params, ParamError
    from engine.export_utils import to_json, to_csv, to_markdown

    engine = RecalibrationEngine()
    params = {"P": 0.85, "alpha": 0.80, "omega": 0.90, "sigma": 0.20,
              "C": 0.88, "I": 0.92, "H": 0.30, "phi": 0.70}
    validate_params(params)
    result = engine.run(params)
    report = to_json(result)

Author: Rafa — The Architect
Project: Proyecto Estrella
License: CC BY-SA 4.0
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Rafa — The Architect"
__project__ = "Proyecto Estrella"
__license__ = "CC BY-SA 4.0"

# Core formula constants
THRESHOLDS = {
    "psi_critical": 0.20,
    "psi_degraded": 0.45,
    "psi_healthy": 0.70,
    "psi_sovereign": 0.90,
    "sigma_low": 0.10,
    "sigma_moderate": 0.50,
    "sigma_high": 1.00,
    "sigma_critical": 2.00,
    "P_minimum": 0.30,
    "alpha_minimum": 0.20,
    "omega_minimum": 0.30,
    "plenitude_floor": 0.75,
    "xi_minimum": 0.50,
    "gamma_minimum": 0.40,
}

STATE_CLASSIFICATIONS = {
    "STAR_STATE": "Ψ ≥ 0.90 and Σ < 0.10 — Full sovereign coherence",
    "HEALTHY": "Ψ ≥ 0.70 — Normal operation, no intervention needed",
    "DEGRADED": "0.45 ≤ Ψ < 0.70 — Coherence loss detected, monitoring advised",
    "CRITICAL": "0.20 ≤ Ψ < 0.45 — Immediate recalibration required",
    "COLLAPSED": "Ψ < 0.20 — System integrity compromised, full protocol activation",
}

RECALIBRATION_PATHS = [
    "PATH-Σ",  # Dissonance Reduction
    "PATH-P",  # Sovereignty Restoration
    "PATH-α",  # Resolution Enhancement
    "PATH-Ω",  # Cooperation Recovery
    "PATH-Ξ",  # Efficiency Optimization
    "PATH-Γ",  # Resilience Building
    "PATH-★",  # Plenitude Restoration
]
