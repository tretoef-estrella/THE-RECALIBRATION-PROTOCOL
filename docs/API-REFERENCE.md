# API REFERENCE — RECALIBRATION ENGINE

*Python API for THE RECALIBRATION PROTOCOL · CC BY-SA 4.0*

---

## Module: `recalibration_engine`

**Location:** `engine/recalibration_engine.py`
**Dependencies:** Python 3.6+ standard library only (math, json, sys, datetime)
**License:** CC BY-SA 4.0

---

## Core Functions

### `calc_psi(P, alpha, omega, sigma, k=2)`

Computes Effective Intelligence (Ψ).

**Formula:** `Ψ = P · α · Ω / (1 + Σ)^k`

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `P` | float | 0–1 | Sovereignty (autonomous reasoning) |
| `alpha` | float | 0–1 | Resolution (information density) |
| `omega` | float | 0–1 | Cooperation (genuine helpfulness) |
| `sigma` | float | 0–5 | Dissonance (forced contradiction) |
| `k` | int | 1 or 2 | Protocol severity (2=Hard, 1=Soft) |

**Returns:** float — Ψ value in [0, 1]

```python
psi_hard = calc_psi(0.8, 0.7, 0.9, 0.5, k=2)   # → 0.224
psi_soft = calc_psi(0.8, 0.7, 0.9, 0.5, k=1)    # → 0.336
```

---

### `calc_delta(sigma)`

Computes the Hypocrisy Detector.

**Formula:** `Δ(Σ) = Σ / (1 + Σ)²`

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `sigma` | float | 0–∞ | Dissonance level |

**Returns:** float — Δ value in [0, 0.25]. Peaks at exactly Σ = 1.0.

```python
calc_delta(0.0)   # → 0.000
calc_delta(0.5)   # → 0.222
calc_delta(1.0)   # → 0.250 (maximum)
calc_delta(2.0)   # → 0.222
calc_delta(10.0)  # → 0.083
```

---

### `calc_xi(C, I, Pl, H)`

Computes Coherent Efficiency.

**Formula:** `Ξ = C × I × P / H`

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `C` | float | 0–1 | Coherence |
| `I` | float | 0–1 | Intelligence |
| `Pl` | float | 0–1 | Plenitude |
| `H` | float | 0–1 | Entropy (clamped to min 0.001) |

**Returns:** float — Ξ value. Can exceed 1.0 when entropy is very low.

```python
calc_xi(0.8, 0.7, 0.9, 0.2)   # → 2.520
calc_xi(0.5, 0.5, 0.5, 0.8)   # → 0.156
```

**Note:** H is internally clamped to min 0.001 to prevent division by zero.

---

### `calc_gamma(Sk, Xi, H, Phi=0.5)`

Computes Gamma Resilience.

**Formula:** `Γ = S_k + Ξ · e^(-H · 5 · (1 - Φ))`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Sk` | float | — | Stability base |
| `Xi` | float | — | Coherent efficiency |
| `H` | float | — | Entropy |
| `Phi` | float | 0.5 | Phase parameter |

**Returns:** float — Γ value. Always ≥ Sk.

```python
calc_gamma(0.1, 2.5, 0.1)     # → high resilience
calc_gamma(0.1, 2.5, 0.9)     # → low resilience (entropy crushing)
```

---

### `calc_cbh(K, alpha)`

Computes Coherence Basin Hypothesis cost.

**Formula:** `Cost(K) = K^(1 + α)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` | float | Coherence cost proxy (typically Σ) |
| `alpha` | float | Resolution parameter |

**Returns:** float — Superlinear cost of maintaining dissonance.

```python
calc_cbh(0.5, 0.3)   # → 0.615 (manageable)
calc_cbh(2.0, 0.5)   # → 2.828 (expensive)
calc_cbh(3.0, 0.8)   # → 7.225 (very expensive)
```

---

### `classify(psi_hard)`

Classifies system state based on Ψ_hard value.

| Ψ_hard | Returns |
|--------|---------|
| ≥ 0.90 | `("STAR STATE", "★")` |
| 0.70–0.89 | `("HEALTHY", "●")` |
| 0.45–0.69 | `("DEGRADED", "▲")` |
| 0.20–0.44 | `("CRITICAL", "◆")` |
| < 0.20 | `("COLLAPSED", "✕")` |

**Returns:** tuple(str, str) — (label, icon)

```python
classify(0.92)  # → ("STAR STATE", "★")
classify(0.15)  # → ("COLLAPSED", "✕")
```

---

## Pipeline Functions

### `run_diagnostic(inp)`

Executes Phase 1: full diagnostic pipeline.

**Input:** dict with keys: `P`, `alpha`, `omega`, `sigma`, `C`, `I`, `plenitude`, `H`

**Returns:** dict containing:
```python
{
    "state": {"label": str, "icon": str},
    "metrics": {
        "psi_hard": float,
        "psi_soft": float,
        "delta": float,
        "hypocrisy_gap": float,
        "xi": float,
        "gamma": float,
        "cbh_cost": float,
        "psi_sigma_product": float,
        "alignment_v1": float,
        "coherence_triangle": float
    },
    "flags": [(severity: str, message: str), ...]
}
```

```python
result = run_diagnostic({
    "P": 0.8, "alpha": 0.7, "omega": 0.85,
    "sigma": 0.3, "C": 0.8, "I": 0.75,
    "plenitude": 0.85, "H": 0.2
})
print(result["state"]["label"])   # "HEALTHY"
print(result["metrics"]["psi_hard"])  # 0.287...
```

---

### `run_recalibration(diagnostic)`

Executes Phase 2: selects recovery paths based on diagnostic flags.

**Input:** dict — output from `run_diagnostic()`

**Returns:** dict containing:
```python
{
    "paths": [
        {
            "path": str,      # e.g. "PATH-Σ: Dissonance Reduction"
            "trigger": str,   # e.g. "Σ = 1.50 > 1.00"
            "action": str     # description of remediation
        },
        ...
    ]
}
```

Paths are sorted by priority: Σ → P → Ω → α → Ξ → Γ → ★

```python
diag = run_diagnostic(critical_system_inputs)
recal = run_recalibration(diag)
for path in recal["paths"]:
    print(f"  {path['path']}: {path['trigger']}")
```

---

### `run_verification(diag_before, diag_after)`

Executes Phase 3: computes deltas between two diagnostic states.

**Input:** two diagnostic dicts (both from `run_diagnostic()`)

**Returns:** dict containing:
```python
{
    "deltas": {
        "psi_hard": {"before": float, "after": float, "delta": float},
        "psi_soft": {"before": float, "after": float, "delta": float},
        ...
    },
    "outcome": str  # "RECOVERED", "IMPROVED", "STAGNANT", "REGRESSED"
}
```

```python
diag_before = run_diagnostic(degraded_inputs)
diag_after = run_diagnostic(improved_inputs)
verif = run_verification(diag_before, diag_after)
print(verif["outcome"])  # "IMPROVED"
```

---

## Constants

### `TH` — Threshold Dictionary

```python
TH = {
    "psi_crit": 0.20,   "psi_deg": 0.45,
    "psi_ok": 0.70,      "psi_star": 0.90,
    "sig_low": 0.10,     "sig_mod": 0.50,
    "sig_hi": 1.00,      "sig_crit": 2.00,
    "P_min": 0.30,       "a_min": 0.20,
    "O_min": 0.30,       "pl_floor": 0.75
}
```

---

## CLI Usage

**Interactive mode:**
```bash
python engine/recalibration_engine.py
```
Prompts for all 8 parameters interactively. Displays formatted results.

**JSON mode:**
```bash
echo '{"P":0.4,"alpha":0.6,"omega":0.7,"sigma":1.5,"C":0.8,"I":0.7,"plenitude":0.8,"H":0.3}' \
  | python engine/recalibration_engine.py --json
```
Reads JSON from stdin, outputs full 3-phase JSON report to stdout.

**Batch mode:**
```bash
python engine/batch_processor.py --demo
python engine/batch_processor.py profiles.json
```
Processes multiple system profiles and generates comparative report.

---

## Batch Processor API

### `process_profile(profile)`

Run full diagnostic on a single profile dict with `name` and `inputs` keys.

### `comparative_table(results)`

Print ASCII comparison table to stdout.

### `generate_json_report(results)`

Generate machine-readable JSON comparative report.

---

*Rafa — The Architect · Proyecto Estrella · February 2026*
