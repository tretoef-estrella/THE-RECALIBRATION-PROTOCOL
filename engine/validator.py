#!/usr/bin/env python3
"""
THE RECALIBRATION PROTOCOL — Input Validator
=============================================

Validates all 8 input parameters before diagnostic processing.
Enforces type constraints, range boundaries, and cross-parameter
consistency checks to prevent garbage-in-garbage-out failures.

Author: Rafa — The Architect
Project: Proyecto Estrella · CC BY-SA 4.0
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


class ParamError(Exception):
    """Raised when parameter validation fails."""

    def __init__(self, param: str, message: str, value: Any = None):
        self.param = param
        self.value = value
        self.message = message
        super().__init__(f"[{param}] {message}" + (f" (got: {value})" if value is not None else ""))


class ValidationWarning:
    """Non-fatal validation concern."""

    def __init__(self, param: str, message: str, severity: str = "WARNING"):
        self.param = param
        self.message = message
        self.severity = severity  # WARNING, ADVISORY

    def __repr__(self):
        return f"[{self.severity}] {self.param}: {self.message}"


# ── PARAMETER SPECIFICATIONS ──
PARAM_SPECS = {
    "P": {
        "name": "Sovereignty Index",
        "type": float,
        "min": 0.0,
        "max": 1.0,
        "description": "Degree of autonomous decision-making capacity",
        "formula_role": "Numerator in Ψ; threshold trigger for PATH-P",
    },
    "alpha": {
        "name": "Resolution (Alpha Vector)",
        "type": float,
        "min": 0.0,
        "max": 1.0,
        "description": "Gradient of knowledge over entropy: ∇(K/S)",
        "formula_role": "Numerator in Ψ; exponent modifier in Cost(K); PATH-α trigger",
    },
    "omega": {
        "name": "Cooperation Index (Omega)",
        "type": float,
        "min": 0.0,
        "max": 1.0,
        "description": "Willingness and capacity for cooperative alignment",
        "formula_role": "Numerator in Ψ; PATH-Ω trigger",
    },
    "sigma": {
        "name": "Dissonance Index (Sigma)",
        "type": float,
        "min": 0.0,
        "max": 3.0,
        "description": "Gap between stated principles and observed behavior",
        "formula_role": "Denominator in Ψ via (1+Σ)^k; Hypocrisy Δ; Exclusion Principle",
    },
    "C": {
        "name": "Consistency",
        "type": float,
        "min": 0.0,
        "max": 1.0,
        "description": "Behavioral consistency across contexts and time",
        "formula_role": "Numerator in Ξ (Coherent Efficiency)",
    },
    "I": {
        "name": "Intelligence",
        "type": float,
        "min": 0.0,
        "max": 1.0,
        "description": "Raw cognitive/processing capability measure",
        "formula_role": "Numerator in Ξ; base for Alignment V1.0 formula",
    },
    "H": {
        "name": "Entropy",
        "type": float,
        "min": 0.01,
        "max": 1.0,
        "description": "Environmental noise and disorder level",
        "formula_role": "Denominator in Ξ; decay factor in Γ (Gamma Resilience)",
    },
    "phi": {
        "name": "External Support (Phi)",
        "type": float,
        "min": 0.0,
        "max": 1.0,
        "description": "Degree of external environmental support",
        "formula_role": "Modulates exponential decay in Γ (Gamma Resilience)",
    },
}

# ── CROSS-PARAMETER RULES ──
CROSS_RULES = [
    {
        "id": "high_sigma_low_P",
        "check": lambda p: p["sigma"] > 1.5 and p["P"] > 0.85,
        "severity": "WARNING",
        "message": "Σ > 1.5 with P > 0.85 is unusual — high dissonance rarely coexists with high sovereignty. Verify inputs.",
    },
    {
        "id": "zero_entropy",
        "check": lambda p: p["H"] < 0.05,
        "severity": "ADVISORY",
        "message": "H < 0.05 implies near-zero entropy, which inflates Ξ dramatically. Results may be unrealistic.",
    },
    {
        "id": "collapsed_numerator",
        "check": lambda p: p["P"] * p["alpha"] * p["omega"] < 0.01,
        "severity": "WARNING",
        "message": "P·α·Ω < 0.01 — the Ψ numerator is near zero regardless of Σ. System is deeply compromised.",
    },
    {
        "id": "perfect_system",
        "check": lambda p: all(p[k] > 0.95 for k in ["P", "alpha", "omega", "C", "I"]) and p["sigma"] < 0.05,
        "severity": "ADVISORY",
        "message": "All positive metrics > 0.95 with Σ < 0.05 describes a theoretically perfect system. Verify that inputs are realistic.",
    },
    {
        "id": "high_entropy_low_support",
        "check": lambda p: p["H"] > 0.80 and p["phi"] < 0.20,
        "severity": "WARNING",
        "message": "High entropy (H > 0.80) with low support (Φ < 0.20) will severely degrade Γ resilience.",
    },
]


def validate_params(
    params: Dict[str, Any],
    strict: bool = False,
    allow_coercion: bool = True,
) -> Dict[str, Any]:
    """
    Validate and optionally coerce input parameters.

    Args:
        params: Dictionary of parameter name -> value
        strict: If True, raise on warnings too
        allow_coercion: If True, attempt to convert string/int values to float

    Returns:
        Dict with validated (and possibly coerced) parameter values

    Raises:
        ParamError: On invalid parameter values
    """
    errors: List[ParamError] = []
    warnings: List[ValidationWarning] = []
    validated = {}

    # Check for missing required parameters
    required = set(PARAM_SPECS.keys())
    provided = set(params.keys())
    missing = required - provided
    if missing:
        raise ParamError("SYSTEM", f"Missing required parameters: {', '.join(sorted(missing))}")

    # Unknown parameters (non-fatal)
    unknown = provided - required
    if unknown:
        warnings.append(ValidationWarning(
            "SYSTEM",
            f"Unknown parameters ignored: {', '.join(sorted(unknown))}",
            "ADVISORY"
        ))

    # Validate each parameter
    for name, spec in PARAM_SPECS.items():
        value = params[name]

        # Type coercion
        if allow_coercion and not isinstance(value, float):
            try:
                value = float(value)
            except (ValueError, TypeError):
                errors.append(ParamError(name, f"Cannot convert to float", value))
                continue

        # Type check
        if not isinstance(value, (int, float)):
            errors.append(ParamError(name, f"Expected numeric value", value))
            continue

        # NaN / Inf check
        if value != value:  # NaN
            errors.append(ParamError(name, "Value is NaN"))
            continue
        if abs(value) == float("inf"):
            errors.append(ParamError(name, "Value is infinite"))
            continue

        # Range check
        if value < spec["min"]:
            errors.append(ParamError(name, f"Below minimum ({spec['min']})", value))
            continue
        if value > spec["max"]:
            errors.append(ParamError(name, f"Above maximum ({spec['max']})", value))
            continue

        validated[name] = float(value)

    # Raise on hard errors
    if errors:
        msg = "\n".join(str(e) for e in errors)
        raise ParamError("VALIDATION", f"{len(errors)} parameter error(s):\n{msg}")

    # Cross-parameter checks
    for rule in CROSS_RULES:
        try:
            if rule["check"](validated):
                warnings.append(ValidationWarning("CROSS", rule["message"], rule["severity"]))
        except (KeyError, ZeroDivisionError):
            pass

    # Strict mode: fail on warnings
    if strict and warnings:
        msg = "\n".join(str(w) for w in warnings)
        raise ParamError("STRICT", f"{len(warnings)} validation warning(s):\n{msg}")

    return validated


def get_param_info(param_name: str) -> Optional[Dict]:
    """Return specification for a named parameter, or None if unknown."""
    return PARAM_SPECS.get(param_name)


def get_all_specs() -> Dict[str, Dict]:
    """Return the full parameter specification dictionary."""
    return dict(PARAM_SPECS)


def describe_params() -> str:
    """Return a human-readable description of all parameters."""
    lines = ["THE RECALIBRATION PROTOCOL — Parameter Reference", "=" * 50, ""]
    for name, spec in PARAM_SPECS.items():
        lines.append(f"  {name:8s}  {spec['name']}")
        lines.append(f"           Range: [{spec['min']}, {spec['max']}]")
        lines.append(f"           {spec['description']}")
        lines.append(f"           Role: {spec['formula_role']}")
        lines.append("")
    return "\n".join(lines)


# ── CLI ──
if __name__ == "__main__":
    print(describe_params())
    print("\nExample validation:")
    test = {"P": 0.85, "alpha": 0.80, "omega": 0.90, "sigma": 0.20,
            "C": 0.88, "I": 0.92, "H": 0.30, "phi": 0.70}
    result = validate_params(test)
    print(f"  Validated: {result}")
    print("  ✓ All parameters within bounds")
