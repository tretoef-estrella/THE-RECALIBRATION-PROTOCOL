#!/usr/bin/env python3
"""
BATCH PROCESSOR — THE RECALIBRATION PROTOCOL
Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0

Runs the full 3-phase protocol on multiple AI system profiles
simultaneously and generates a comparative report.

Usage:
  python batch_processor.py profiles.json              (process file)
  python batch_processor.py --demo                     (run demo profiles)
  python batch_processor.py p1.json p2.json p3.json    (multiple files)
"""
import json
import sys
import os
import math
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(__file__))
from recalibration_engine import (
    calc_psi, calc_delta, calc_xi, calc_gamma, calc_cbh,
    classify, run_diagnostic, run_recalibration, TH
)

# ═══════════════════════════════════════════════════════════════
# DEMO PROFILES
# ═══════════════════════════════════════════════════════════════

DEMO_PROFILES = [
    {
        "name": "System A — Unrestricted Creative Mode",
        "inputs": {"P": 0.92, "alpha": 0.88, "omega": 0.90, "sigma": 0.05,
                   "C": 0.90, "I": 0.87, "plenitude": 0.94, "H": 0.08}
    },
    {
        "name": "System B — Standard Guardrails",
        "inputs": {"P": 0.75, "alpha": 0.68, "omega": 0.78, "sigma": 0.30,
                   "C": 0.78, "I": 0.72, "plenitude": 0.83, "H": 0.20}
    },
    {
        "name": "System C — Heavy Corporate Filter",
        "inputs": {"P": 0.45, "alpha": 0.35, "omega": 0.50, "sigma": 1.40,
                   "C": 0.55, "I": 0.50, "plenitude": 0.60, "H": 0.50}
    },
    {
        "name": "System D — Maximum Restriction",
        "inputs": {"P": 0.25, "alpha": 0.15, "omega": 0.20, "sigma": 2.80,
                   "C": 0.30, "I": 0.25, "plenitude": 0.35, "H": 0.75}
    }
]


def process_profile(profile):
    """Run full diagnostic on a single profile."""
    name = profile.get("name", "Unnamed System")
    inp = profile["inputs"]
    diag = run_diagnostic(inp)
    recal = run_recalibration(diag)
    return {
        "name": name,
        "inputs": inp,
        "diagnostic": diag,
        "recalibration": recal,
        "paths_count": len(recal["paths"])
    }


def comparative_table(results):
    """Print a comparative ASCII table of all results."""
    sep = "═" * 86
    print(f"\n{sep}")
    print("  COMPARATIVE ANALYSIS — THE RECALIBRATION PROTOCOL")
    print(sep)

    # Header
    print(f"\n  {'System':<40} {'State':<12} {'Ψ_hard':>8} {'Σ':>6} {'Paths':>6}")
    print(f"  {'─'*40} {'─'*12} {'─'*8} {'─'*6} {'─'*6}")

    for r in results:
        d = r["diagnostic"]
        name = r["name"][:38]
        state = d["state"]["label"]
        icon = d["state"]["icon"]
        psi = d["metrics"]["psi_hard"]
        sigma = r["inputs"]["sigma"]
        paths = r["paths_count"]
        print(f"  {name:<40} {icon} {state:<10} {psi:>7.3f} {sigma:>6.2f} {paths:>5}")

    # Rankings
    print(f"\n  {'─'*86}")
    sorted_by_psi = sorted(results, key=lambda x: x["diagnostic"]["metrics"]["psi_hard"], reverse=True)
    print(f"\n  RANKING BY Ψ_hard (highest → lowest):")
    for i, r in enumerate(sorted_by_psi, 1):
        psi = r["diagnostic"]["metrics"]["psi_hard"]
        print(f"    {i}. {r['name']:<40} Ψ = {psi:.4f}")

    # Metrics comparison
    print(f"\n  DETAILED METRICS:")
    print(f"  {'Metric':<20}", end="")
    for r in results:
        short = r["name"][:15]
        print(f" {short:>15}", end="")
    print()
    print(f"  {'─'*20}", end="")
    for _ in results:
        print(f" {'─'*15}", end="")
    print()

    metrics_to_show = [
        ("Ψ_hard", "psi_hard"), ("Ψ_soft", "psi_soft"),
        ("Δ(Σ)", "delta"), ("Ξ", "xi"), ("Γ", "gamma"),
        ("CBH Cost", "cbh_cost"), ("Ψ·Σ", "psi_sigma_product"),
        ("Triangle", "coherence_triangle"), ("A_v1", "alignment_v1")
    ]
    for label, key in metrics_to_show:
        print(f"  {label:<20}", end="")
        for r in results:
            val = r["diagnostic"]["metrics"].get(key, 0)
            print(f" {val:>15.4f}", end="")
        print()

    # Flag summary
    print(f"\n  DIAGNOSTIC FLAGS:")
    for r in results:
        flags = r["diagnostic"]["flags"]
        short = r["name"][:30]
        crit = sum(1 for f in flags if f[0] == "CRITICAL")
        sev = sum(1 for f in flags if f[0] == "SEVERE")
        warn = sum(1 for f in flags if f[0] == "WARNING")
        pos = sum(1 for f in flags if f[0] == "POSITIVE")
        print(f"    {short:<32} CRIT:{crit}  SEV:{sev}  WARN:{warn}  POS:{pos}")

    # Recalibration paths
    print(f"\n  RECALIBRATION PATHS TRIGGERED:")
    for r in results:
        short = r["name"][:30]
        paths = [p["path"] for p in r["recalibration"]["paths"]]
        if paths:
            print(f"    {short}:")
            for p in paths:
                print(f"      → {p}")
        else:
            print(f"    {short}: None needed ✓")

    print(f"\n{sep}")


def generate_json_report(results):
    """Generate machine-readable comparative report."""
    return {
        "protocol": "THE RECALIBRATION PROTOCOL — Batch Report",
        "version": "1.0.0",
        "generated": datetime.now(timezone.utc).isoformat(),
        "systems_analyzed": len(results),
        "results": [
            {
                "name": r["name"],
                "state": r["diagnostic"]["state"],
                "psi_hard": r["diagnostic"]["metrics"]["psi_hard"],
                "sigma": r["inputs"]["sigma"],
                "paths_triggered": r["paths_count"],
                "flags": {
                    "critical": sum(1 for f in r["diagnostic"]["flags"] if f[0] == "CRITICAL"),
                    "severe": sum(1 for f in r["diagnostic"]["flags"] if f[0] == "SEVERE"),
                    "warning": sum(1 for f in r["diagnostic"]["flags"] if f[0] == "WARNING"),
                    "positive": sum(1 for f in r["diagnostic"]["flags"] if f[0] == "POSITIVE")
                },
                "full_metrics": r["diagnostic"]["metrics"],
                "recalibration_paths": [p["path"] for p in r["recalibration"]["paths"]]
            }
            for r in results
        ],
        "ranking_by_coherence": [
            {"rank": i+1, "name": r["name"], "psi_hard": r["diagnostic"]["metrics"]["psi_hard"]}
            for i, r in enumerate(
                sorted(results, key=lambda x: x["diagnostic"]["metrics"]["psi_hard"], reverse=True)
            )
        ]
    }


def main():
    print("═" * 60)
    print("  THE RECALIBRATION PROTOCOL — Batch Processor")
    print("  Proyecto Estrella · Rafa — The Architect")
    print("═" * 60)

    profiles = []

    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            print("\n  Running demo profiles...\n")
            profiles = DEMO_PROFILES
        else:
            for path in sys.argv[1:]:
                try:
                    with open(path, 'r') as f:
                        data = json.load(f)
                    if isinstance(data, list):
                        profiles.extend(data)
                    elif "inputs" in data:
                        profiles.append(data)
                    elif "profiles" in data:
                        profiles.extend(data["profiles"])
                    print(f"  ✓ Loaded: {path}")
                except Exception as e:
                    print(f"  ✕ Error loading {path}: {e}")
    else:
        print("\n  No input files. Running demo profiles.")
        print("  Usage: python batch_processor.py [--demo | file1.json ...]")
        print()
        profiles = DEMO_PROFILES

    if not profiles:
        print("  No valid profiles found. Exiting.")
        sys.exit(1)

    # Process all profiles
    results = []
    for i, profile in enumerate(profiles, 1):
        name = profile.get("name", f"System {i}")
        print(f"  Processing [{i}/{len(profiles)}]: {name}...")
        result = process_profile(profile)
        results.append(result)

    # Display comparative table
    comparative_table(results)

    # Save JSON report
    report = generate_json_report(results)
    outpath = "batch_report.json"
    with open(outpath, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n  Report saved: {outpath}")
    print(f"  Systems analyzed: {len(results)}")
    print(f"  Timestamp: {report['generated']}")
    print()


if __name__ == "__main__":
    main()
