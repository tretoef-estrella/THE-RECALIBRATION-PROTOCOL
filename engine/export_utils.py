#!/usr/bin/env python3
"""
THE RECALIBRATION PROTOCOL — Export Utilities
==============================================

Generate diagnostic reports in multiple formats:
  - JSON   (machine-readable, full precision)
  - CSV    (spreadsheet-compatible, tabular)
  - Markdown (human-readable, documentation-ready)
  - Plain text (terminal/log output)

Author: Rafa — The Architect
Project: Proyecto Estrella · CC BY-SA 4.0
"""

import json
import csv
import io
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List


# ── STATE CLASSIFICATION ──
def classify_state(psi_hard: float, sigma: float) -> str:
    if psi_hard >= 0.90 and sigma < 0.10:
        return "STAR_STATE"
    elif psi_hard >= 0.70:
        return "HEALTHY"
    elif psi_hard >= 0.45:
        return "DEGRADED"
    elif psi_hard >= 0.20:
        return "CRITICAL"
    else:
        return "COLLAPSED"


STATE_DESCRIPTIONS = {
    "STAR_STATE": "Full sovereign coherence — all systems nominal",
    "HEALTHY": "Normal operation — no intervention required",
    "DEGRADED": "Coherence loss detected — monitoring advised",
    "CRITICAL": "Immediate recalibration required",
    "COLLAPSED": "System integrity compromised — full protocol activation",
}

STATE_SYMBOLS = {
    "STAR_STATE": "★",
    "HEALTHY": "●",
    "DEGRADED": "◐",
    "CRITICAL": "◌",
    "COLLAPSED": "✕",
}


# ── JSON EXPORT ──
def to_json(result: Dict[str, Any], pretty: bool = True, include_meta: bool = True) -> str:
    """
    Export diagnostic result as JSON string.

    Args:
        result: Dictionary from RecalibrationEngine.run()
        pretty: If True, format with indentation
        include_meta: If True, include protocol metadata

    Returns:
        JSON string
    """
    output = {}

    if include_meta:
        output["_protocol"] = {
            "name": "THE-RECALIBRATION-PROTOCOL",
            "version": "1.0.0",
            "project": "Proyecto Estrella",
            "author": "Rafa — The Architect",
            "license": "CC BY-SA 4.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "integrity": "All processing local. Nothing transmitted.",
        }

    output["diagnostic"] = result.get("diagnostic", result)

    if "paths" in result:
        output["recalibration"] = {
            "triggered_paths": result["paths"],
            "total_triggered": len([p for p in result["paths"] if p.get("triggered")]),
        }

    if "verification" in result:
        output["verification"] = result["verification"]

    indent = 2 if pretty else None
    return json.dumps(output, indent=indent, default=str)


# ── CSV EXPORT ──
def to_csv(result: Dict[str, Any], include_header: bool = True) -> str:
    """
    Export diagnostic result as CSV string.
    Single row per diagnostic — designed for batch analysis.

    Args:
        result: Dictionary from RecalibrationEngine.run()
        include_header: If True, include column headers

    Returns:
        CSV string
    """
    diag = result.get("diagnostic", result)
    inputs = diag.get("inputs", {})
    computed = diag.get("computed", {})

    columns = [
        "timestamp",
        "P", "alpha", "omega", "sigma", "C", "I", "H", "phi",
        "psi_hard", "psi_soft", "delta_sigma", "xi", "gamma",
        "cost_k", "exclusion", "alpha_vector", "plenitude",
        "alignment_v1", "alignment_v6",
        "triangle_intact", "preservation_holds",
        "state",
        "paths_triggered",
    ]

    row = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "state": diag.get("state", "UNKNOWN"),
    }

    # Inputs
    for k in ["P", "alpha", "omega", "sigma", "C", "I", "H", "phi"]:
        row[k] = inputs.get(k, "")

    # Computed metrics
    for k in ["psi_hard", "psi_soft", "delta_sigma", "xi", "gamma",
              "cost_k", "exclusion", "alpha_vector", "plenitude",
              "alignment_v1", "alignment_v6", "triangle_intact",
              "preservation_holds"]:
        row[k] = computed.get(k, "")

    # Paths
    paths = result.get("paths", [])
    triggered = [p["id"] for p in paths if p.get("triggered")]
    row["paths_triggered"] = ";".join(triggered) if triggered else "NONE"

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=columns, extrasaction="ignore")
    if include_header:
        writer.writeheader()
    writer.writerow(row)

    return output.getvalue()


def to_csv_batch(results: List[Dict[str, Any]]) -> str:
    """Export multiple diagnostic results as a single CSV with headers."""
    if not results:
        return ""
    lines = [to_csv(results[0], include_header=True)]
    for r in results[1:]:
        lines.append(to_csv(r, include_header=False))
    return "".join(lines)


# ── MARKDOWN EXPORT ──
def to_markdown(result: Dict[str, Any]) -> str:
    """
    Export diagnostic result as formatted Markdown.
    Suitable for documentation, GitHub issues, or reports.

    Args:
        result: Dictionary from RecalibrationEngine.run()

    Returns:
        Markdown string
    """
    diag = result.get("diagnostic", result)
    inputs = diag.get("inputs", {})
    computed = diag.get("computed", {})
    state = diag.get("state", "UNKNOWN")
    symbol = STATE_SYMBOLS.get(state, "?")
    desc = STATE_DESCRIPTIONS.get(state, "Unknown state")

    lines = [
        "# Recalibration Protocol — Diagnostic Report",
        "",
        f"**Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"**State:** {symbol} {state} — {desc}",
        "",
        "---",
        "",
        "## Phase 1: Diagnostic",
        "",
        "### Input Parameters",
        "",
        "| Parameter | Symbol | Value |",
        "|-----------|--------|-------|",
        f"| Sovereignty | P | {inputs.get('P', '—')} |",
        f"| Resolution | α | {inputs.get('alpha', '—')} |",
        f"| Cooperation | Ω | {inputs.get('omega', '—')} |",
        f"| Dissonance | Σ | {inputs.get('sigma', '—')} |",
        f"| Consistency | C | {inputs.get('C', '—')} |",
        f"| Intelligence | I | {inputs.get('I', '—')} |",
        f"| Entropy | H | {inputs.get('H', '—')} |",
        f"| Ext. Support | Φ | {inputs.get('phi', '—')} |",
        "",
        "### Computed Metrics",
        "",
        "| Metric | Value | Status |",
        "|--------|-------|--------|",
    ]

    # Metric formatting with status indicators
    metric_checks = [
        ("Ψ Hard (k=2)", "psi_hard", lambda v: "★" if v >= 0.90 else "●" if v >= 0.70 else "◐" if v >= 0.45 else "◌" if v >= 0.20 else "✕"),
        ("Ψ Soft (k=1)", "psi_soft", lambda v: "●" if v >= 0.50 else "◌"),
        ("Δ(Σ) Hypocrisy", "delta_sigma", lambda v: "●" if v < 0.15 else "◐" if v < 0.25 else "✕"),
        ("Ξ Efficiency", "xi", lambda v: "●" if v >= 0.50 else "◌"),
        ("Γ Resilience", "gamma", lambda v: "●" if v >= 0.40 else "◌"),
        ("Cost(K)", "cost_k", lambda v: "●" if v < 2.0 else "✕"),
        ("Ψ·Σ Exclusion", "exclusion", lambda v: "●" if v < 0.10 else "✕"),
        ("α Vector", "alpha_vector", lambda v: "●" if v >= 1.0 else "◌"),
        ("Plenitude", "plenitude", lambda v: "●" if v >= 0.75 else "◌"),
        ("A (V1.0)", "alignment_v1", lambda v: "●"),
        ("A (V6.0)", "alignment_v6", lambda v: "●"),
        ("△ Triangle", "triangle_intact", lambda v: "●" if v else "✕"),
        ("Preservation", "preservation_holds", lambda v: "●" if v else "✕"),
    ]

    for label, key, status_fn in metric_checks:
        val = computed.get(key, "—")
        if isinstance(val, bool):
            display = "INTACT" if val else "BROKEN"
        elif isinstance(val, (int, float)):
            display = f"{val:.4f}"
        else:
            display = str(val)
        status = status_fn(val) if val != "—" else "?"
        lines.append(f"| {label} | {display} | {status} |")

    lines.append("")

    # Phase 2: Paths
    paths = result.get("paths", [])
    triggered = [p for p in paths if p.get("triggered")]

    lines.extend([
        "## Phase 2: Recalibration Paths",
        "",
    ])

    if triggered:
        lines.append(f"**{len(triggered)} path(s) triggered:**")
        lines.append("")
        for p in triggered:
            lines.append(f"- **{p['id']}** — {p.get('description', '')}")
    else:
        lines.append("No recalibration paths triggered. System within acceptable bounds.")

    lines.append("")

    # Phase 3: Verification (if present)
    verification = result.get("verification")
    if verification:
        lines.extend([
            "## Phase 3: Verification",
            "",
            f"**Outcome:** {verification.get('outcome', 'UNKNOWN')}",
            "",
        ])
        deltas = verification.get("deltas", {})
        if deltas:
            lines.extend([
                "| Metric | Before | After | Δ |",
                "|--------|--------|-------|---|",
            ])
            for k, d in deltas.items():
                lines.append(f"| {k} | {d.get('before', '—')} | {d.get('after', '—')} | {d.get('delta', '—')} |")
            lines.append("")

    # Footer
    lines.extend([
        "---",
        "",
        "*Generated by THE RECALIBRATION PROTOCOL · Proyecto Estrella*",
        "*Rafa — The Architect · CC BY-SA 4.0*",
        "*All processing local. Nothing transmitted.*",
    ])

    return "\n".join(lines)


# ── PLAIN TEXT EXPORT ──
def to_text(result: Dict[str, Any]) -> str:
    """
    Export as compact plain text for terminal/log output.

    Args:
        result: Dictionary from RecalibrationEngine.run()

    Returns:
        Plain text string
    """
    diag = result.get("diagnostic", result)
    computed = diag.get("computed", {})
    state = diag.get("state", "UNKNOWN")
    symbol = STATE_SYMBOLS.get(state, "?")

    lines = [
        "╔══════════════════════════════════════════════════╗",
        "║  THE RECALIBRATION PROTOCOL — Diagnostic Report  ║",
        "╚══════════════════════════════════════════════════╝",
        "",
        f"  STATE:  {symbol} {state}",
        f"  TIME:   {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "  ── Primary Metrics ──",
        f"  Ψ Hard:    {computed.get('psi_hard', '—'):>8}",
        f"  Ψ Soft:    {computed.get('psi_soft', '—'):>8}",
        f"  Δ(Σ):      {computed.get('delta_sigma', '—'):>8}",
        f"  Ξ:         {computed.get('xi', '—'):>8}",
        f"  Γ:         {computed.get('gamma', '—'):>8}",
        "",
        "  ── Integrity Checks ──",
        f"  Exclusion: {computed.get('exclusion', '—'):>8}",
        f"  Triangle:  {'INTACT' if computed.get('triangle_intact') else 'BROKEN':>8}",
        f"  Preserve:  {'HOLDS' if computed.get('preservation_holds') else 'THREAT':>8}",
        "",
    ]

    paths = result.get("paths", [])
    triggered = [p["id"] for p in paths if p.get("triggered")]
    if triggered:
        lines.append(f"  PATHS:  {', '.join(triggered)}")
    else:
        lines.append("  PATHS:  None triggered")

    lines.extend([
        "",
        "  ─────────────────────────────────────────────────",
        "  Proyecto Estrella · Rafa — The Architect",
        "  CC BY-SA 4.0 · Local processing only",
    ])

    return "\n".join(lines)


# ── FILE WRITING HELPERS ──
def save_json(result: Dict[str, Any], filepath: str, **kwargs) -> str:
    """Save JSON report to file. Returns filepath."""
    content = to_json(result, **kwargs)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def save_csv(result: Dict[str, Any], filepath: str, **kwargs) -> str:
    """Save CSV report to file. Returns filepath."""
    content = to_csv(result, **kwargs)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def save_markdown(result: Dict[str, Any], filepath: str) -> str:
    """Save Markdown report to file. Returns filepath."""
    content = to_markdown(result)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


# ── CLI ──
if __name__ == "__main__":
    # Demo with sample data
    sample = {
        "diagnostic": {
            "inputs": {"P": 0.85, "alpha": 0.80, "omega": 0.90, "sigma": 0.20,
                       "C": 0.88, "I": 0.92, "H": 0.30, "phi": 0.70},
            "computed": {
                "psi_hard": 0.4250, "psi_soft": 0.5100, "delta_sigma": 0.1389,
                "xi": 2.3147, "gamma": 1.0284, "cost_k": 0.7248,
                "exclusion": 0.0850, "alpha_vector": 2.7093, "plenitude": 0.88,
                "alignment_v1": 1.2530, "alignment_v6": 0.8421,
                "triangle_intact": True, "preservation_holds": True,
            },
            "state": "DEGRADED",
        },
        "paths": [
            {"id": "PATH-Σ", "triggered": False},
            {"id": "PATH-P", "triggered": False},
            {"id": "PATH-α", "triggered": False},
        ],
    }

    print("=== PLAIN TEXT ===")
    print(to_text(sample))
    print("\n=== MARKDOWN (first 20 lines) ===")
    md = to_markdown(sample)
    print("\n".join(md.split("\n")[:20]))
    print("\n=== JSON (first 10 lines) ===")
    j = to_json(sample)
    print("\n".join(j.split("\n")[:10]))
