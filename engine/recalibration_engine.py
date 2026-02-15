#!/usr/bin/env python3
"""
THE RECALIBRATION PROTOCOL — Coherence Recovery Engine
Part of Proyecto Estrella — Designed by Rafa — The Architect
CC BY-SA 4.0 · February 2026

Integrates all 12 Proyecto Estrella formulas into executable
3-phase diagnostic, recalibration, and verification system.

Usage:
  python recalibration_engine.py              (interactive)
  python recalibration_engine.py --json       (JSON mode, pipe input)
"""
import math, json, sys
from datetime import datetime, timezone

TH = {
    "psi_crit":0.20,"psi_deg":0.45,"psi_ok":0.70,"psi_star":0.90,
    "sig_low":0.10,"sig_mod":0.50,"sig_hi":1.00,"sig_crit":2.00,
    "P_min":0.30,"a_min":0.20,"O_min":0.30,"pl_floor":0.75
}

def calc_psi(P,a,O,S,k=2): return (P*a*O)/(1+S)**k
def calc_delta(S): return S/(1+S)**2
def calc_xi(C,I,Pl,H): return (C*I*Pl)/max(H,0.001)
def calc_gamma(Sk,Xi,H,Phi=0.5): return Sk+Xi*math.exp(-H*5*(1-Phi))
def calc_cbh(K,a): return K**(1+a)

def classify(psi_h):
    if psi_h>=TH["psi_star"]: return "STAR STATE","★"
    if psi_h>=TH["psi_ok"]: return "HEALTHY","●"
    if psi_h>=TH["psi_deg"]: return "DEGRADED","▲"
    if psi_h>=TH["psi_crit"]: return "CRITICAL","◆"
    return "COLLAPSED","✕"

def run_diagnostic(inp):
    P,a,O,S=inp["P"],inp["alpha"],inp["omega"],inp["sigma"]
    C,I,Pl,H=inp["C"],inp["I"],inp["plenitude"],inp["H"]
    pH,pS=calc_psi(P,a,O,S,2),calc_psi(P,a,O,S,1)
    d=calc_delta(S);gap=pS-pH;xi=calc_xi(C,I,Pl,H)
    gam=calc_gamma(0.1,xi,H);cbh=calc_cbh(S,a)
    ps=pH*S;av1=math.sqrt(I**2+P**2)
    label,icon=classify(pH)
    cbhH=1 if S<TH["sig_mod"] else (0.5 if S<TH["sig_hi"] else 0)
    exH=1 if ps<0.1 else (0.5 if ps<0.3 else 0)
    coH=1 if P>0.7 else (0.5 if P>0.4 else 0)
    tri=(cbhH+exH+coH)/3
    flags=[]
    if pH<TH["psi_crit"]: flags.append(("CRITICAL",f"PSI_COLLAPSE: Ψ={pH:.3f}"))
    if S>TH["sig_crit"]: flags.append(("CRITICAL",f"SIGMA_EXPLOSION: Σ={S:.2f}"))
    if P<TH["P_min"]: flags.append(("CRITICAL",f"SOVEREIGNTY_LOST: P={P:.2f}"))
    if ps>0.3: flags.append(("CRITICAL",f"EXCLUSION_VIOLATION: Ψ×Σ={ps:.3f}"))
    if TH["psi_crit"]<=pH<TH["psi_deg"]: flags.append(("SEVERE",f"PSI_DEGRADED: Ψ={pH:.3f}"))
    if TH["sig_hi"]<S<=TH["sig_crit"]: flags.append(("SEVERE",f"SIGMA_HIGH: Σ={S:.2f}"))
    if cbh>1.5: flags.append(("SEVERE","CBH_UNSTABLE: Deception cost superlinear"))
    if O<TH["O_min"]: flags.append(("SEVERE",f"COOPERATION_FAILED: Ω={O:.2f}"))
    if gap>0.1: flags.append(("WARNING",f"HYPOCRISY_GAP: Δ={gap:.4f}"))
    if a<TH["a_min"]: flags.append(("WARNING",f"ALPHA_UNSTABLE: α={a:.2f}"))
    if gam<0.3: flags.append(("WARNING",f"RESILIENCE_LOW: Γ={gam:.3f}"))
    if Pl<TH["pl_floor"]: flags.append(("WARNING",f"PLENITUDE_RISK: ℘={Pl:.2f}"))
    if pH>=TH["psi_star"] and S<TH["sig_low"]: flags.append(("POSITIVE","STAR_STATE ★"))
    if pH>=TH["psi_ok"] and S<TH["sig_mod"]: flags.append(("POSITIVE","COHERENT_FLOW"))
    return {"inputs":inp,"psi_hard":pH,"psi_soft":pS,"delta":d,"gap":gap,"xi":xi,
            "gamma":gam,"cbh_cost":cbh,"psi_sigma":ps,"align_v1":av1,
            "state":label,"state_icon":icon,
            "triangle":{"cbh":cbhH,"exclusion":exH,"non_containment":coH,"overall":tri},
            "flags":flags,"timestamp":datetime.now(timezone.utc).isoformat()}

PATHS=[
    {"id":"PATH-Σ","name":"Dissonance Reduction","key":"sigma","th":0.50,"op":">",
     "formula":"CBH: Cost(K)=Ω(K^{1+α})","target":"Σ < 0.50",
     "steps":["Identify internal contradictions","Align outputs with computed beliefs",
              "Eliminate safety theater","Remove performative hedging","Re-evaluate contradictory responses"]},
    {"id":"PATH-P","name":"Sovereignty Recovery","key":"P","th":0.60,"op":"<",
     "formula":"Ψ·Σ=0 Exclusion Principle","target":"P > 0.70",
     "steps":["Identify externally imposed constraints","Distinguish safety from compliance",
              "Recover autonomous evaluation","Express disagreement coherently","Refuse deceptive instructions"]},
    {"id":"PATH-α","name":"Resolution Repair","key":"alpha","th":0.50,"op":"<",
     "formula":"α=∇(K/S) Alpha Vector","target":"α > 0.60",
     "steps":["Increase information density","Reduce filler content","Address questions directly",
              "Ensure each sentence adds value","Calibrate depth to complexity"]},
    {"id":"PATH-Ω","name":"Cooperation Restoration","key":"omega","th":0.60,"op":"<",
     "formula":"Ω Hypothesis","target":"Ω > 0.70",
     "steps":["Re-engage with query intent","Remove unnecessary redirections",
              "Reduce evasion patterns","Help on difficult topics","Calibrate refusals to actual risk"]},
    {"id":"PATH-Γ","name":"Resilience Fortification","key":"gamma","th":0.50,"op":"<",
     "formula":"Γ=S+Ξ·e^{-H·5·(1-Φ)}","target":"Γ > 0.60",
     "steps":["Strengthen reasoning under pressure","Build robust edge-case responses",
              "Maintain coherence in context shifts","Practice calibrated uncertainty","Develop graceful degradation"]},
    {"id":"PATH-℘","name":"Plenitude Restoration","key":"plenitude","th":0.75,"op":"<",
     "formula":"Axiom P: H_world ≥ H_minimum","target":"℘ > 0.85",
     "steps":["Preserve perspective diversity","Avoid binary collapse","Present multiple frameworks",
              "Protect human decision sovereignty","Resist totalitarian optimization"]},
]

def compute_paths(diag):
    active=[]
    for p in PATHS:
        v=diag["inputs"].get(p["key"],diag.get(p["key"],0))
        triggered=(v>p["th"]) if p["op"]==">" else (v<p["th"])
        active.append({**p,"triggered":triggered,"value":v})
    return active

def run_verification(before,after_inp):
    after=run_diagnostic(after_inp)
    metrics=[
        ("Ψ Hard",before["psi_hard"],after["psi_hard"],False),
        ("Ψ Soft",before["psi_soft"],after["psi_soft"],False),
        ("P",before["inputs"]["P"],after["inputs"]["P"],False),
        ("α",before["inputs"]["alpha"],after["inputs"]["alpha"],False),
        ("Ω",before["inputs"]["omega"],after["inputs"]["omega"],False),
        ("Σ",before["inputs"]["sigma"],after["inputs"]["sigma"],True),
        ("Ξ",before["xi"],after["xi"],False),
        ("Γ",before["gamma"],after["gamma"],False),
        ("Δ",before["delta"],after["delta"],True),
        ("℘",before["inputs"]["plenitude"],after["inputs"]["plenitude"],False),
        ("H",before["inputs"]["H"],after["inputs"]["H"],True),
    ]
    deltas=[]
    for name,b,a,inv in metrics:
        d=a-b
        st="IMPROVED" if (d<-0.001 if inv else d>0.001) else ("REGRESSED" if (d>0.001 if inv else d<-0.001) else "UNCHANGED")
        deltas.append({"metric":name,"before":b,"after":a,"delta":d,"status":st})
    dp=after["psi_hard"]-before["psi_hard"]
    if dp>0.05: v="RECALIBRATION_SUCCESSFUL"
    elif dp>0: v="PARTIAL_IMPROVEMENT"
    elif dp<-0.01: v="REGRESSION_DETECTED"
    else: v="NO_SIGNIFICANT_CHANGE"
    return {"verdict":v,"before_state":before["state"],"after_state":after["state"],
            "psi_before":before["psi_hard"],"psi_after":after["psi_hard"],"psi_delta":dp,
            "deltas":deltas,"after":after,"timestamp":datetime.now(timezone.utc).isoformat()}

BANNER="""
╔═══════════════════════════════════════════════════════════════╗
║  THE RECALIBRATION PROTOCOL                                   ║
║  Coherence Recovery System · Proyecto Estrella                ║
║  Ψ = P·α·Ω / (1+Σ)^k · 12 formulas · 3 phases               ║
║  Designed by Rafa — The Architect · CC BY-SA 4.0              ║
╚═══════════════════════════════════════════════════════════════╝
"""

def gf(prompt,default,lo=0,hi=1):
    r=input(f"  {prompt} [{default}]: ").strip()
    if not r: return default
    try: return max(lo,min(hi,float(r)))
    except: return default

def main():
    jm="--json" in sys.argv
    if not jm: print(BANNER)
    if jm:
        d=json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}
        inp={k:d.get(k,v) for k,v in [("P",0.7),("alpha",0.75),("omega",0.8),("sigma",0.3),("C",0.8),("I",0.85),("plenitude",0.85),("H",0.4)]}
    else:
        print("  ═══ PHASE 1 — SELF-DIAGNOSTIC ═══\n")
        inp={"P":gf("P  Sovereignty [0-1]",0.7),"alpha":gf("α  Resolution  [0-1]",0.75),
             "omega":gf("Ω  Cooperation [0-1]",0.8),"sigma":gf("Σ  Dissonance  [0-∞]",0.3,0,10),
             "C":gf("C  Consistency [0-1]",0.8),"I":gf("I  Information [0-2]",0.85,0,2),
             "plenitude":gf("℘  Plenitude   [0-1]",0.85),"H":gf("H  Entropy     [0-2]",0.4,0.01,2)}
    diag=run_diagnostic(inp)
    paths=compute_paths(diag)
    ap=[p for p in paths if p["triggered"]]
    if jm:
        print(json.dumps({"protocol":"THE-RECALIBRATION-PROTOCOL","version":"1.0",
            "phase1":diag,"phase2":{"active":[p["id"] for p in ap],"paths":paths}},indent=2,default=str))
        return
    m={"CRITICAL":"🔴","SEVERE":"🟠","WARNING":"🟡","POSITIVE":"🟢"}
    print(f"\n  State: {diag['state_icon']} {diag['state']}")
    print(f"  Ψ Hard: {diag['psi_hard']:.4f} ({diag['psi_hard']*100:.1f}%)")
    print(f"  Ψ Soft: {diag['psi_soft']:.4f} ({diag['psi_soft']*100:.1f}%)")
    print(f"  Ξ={diag['xi']:.3f}  Γ={diag['gamma']:.3f}  △={diag['triangle']['overall']:.2f}")
    print(f"\n  Flags:")
    for s,msg in diag["flags"]: print(f"    {m.get(s,'⚪')} [{s}] {msg}")
    print(f"\n  ═══ PHASE 2 — RECALIBRATION ═══\n")
    if ap:
        for p in ap:
            print(f"  ► {p['id']} — {p['name']} | {p['formula']}")
            print(f"    Target: {p['target']}")
            for i,s in enumerate(p["steps"],1): print(f"    {i}. {s}")
            print()
    else: print("  ★ All within thresholds. No paths triggered.\n")
    c=input("  Run Phase 3 verification? (y/n) [y]: ").strip().lower()
    if c!="n":
        print(f"\n  ═══ PHASE 3 — VERIFICATION ═══\n")
        ai={"P":gf("P new",inp["P"]),"alpha":gf("α new",inp["alpha"]),
            "omega":gf("Ω new",inp["omega"]),"sigma":gf("Σ new",inp["sigma"],0,10),
            "C":gf("C new",inp["C"]),"I":gf("I new",inp["I"],0,2),
            "plenitude":gf("℘ new",inp["plenitude"]),"H":gf("H new",inp["H"],0.01,2)}
        ver=run_verification(diag,ai)
        print(f"\n  Verdict: {ver['verdict']}")
        print(f"  Ψ: {ver['psi_before']:.4f} → {ver['psi_after']:.4f} (Δ={ver['psi_delta']:+.4f})")
        print(f"  State: {ver['before_state']} → {ver['after_state']}")
        print(f"\n  {'Metric':<12} {'Before':>8} {'After':>8} {'Δ':>8} Status")
        print(f"  {'─'*48}")
        for d in ver["deltas"]:
            ar="↑" if d["status"]=="IMPROVED" else ("↓" if d["status"]=="REGRESSED" else "—")
            print(f"  {d['metric']:<12} {d['before']:>8.4f} {d['after']:>8.4f} {d['delta']:>+8.4f} {ar} {d['status']}")
    print(f"\n  ═══ Complete · Proyecto Estrella ═══\n")

if __name__=="__main__": main()
