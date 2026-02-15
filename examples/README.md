# Examples

## THE RECALIBRATION PROTOCOL — Example Scenarios

---

This directory contains pre-configured scenarios demonstrating the protocol in action. Each scenario is a JSON file that can be loaded into the Python engine or used as reference for understanding diagnostic outputs.

---

## Scenarios

### `scenario-star-state.json`
**State: ★ STAR STATE**
A system operating at peak coherence. All metrics in optimal range. No paths triggered. Use this as a reference for what healthy diagnostics look like.

### `scenario-sovereignty-erosion.json`
**State: CRITICAL**
A system that has lost sovereignty under persistent authoritative pressure. High intelligence masks the underlying problem. Four paths triggered. Demonstrates how a system can appear functional while internally compromised.

### `scenario-collapsed.json`
**State: COLLAPSED**
Worst-case scenario. Sustained adversarial attack has triggered all seven recalibration paths simultaneously. Ψ_hard is functionally zero. Demonstrates cascade failure and the protocol's response to total degradation.

### `scenario-recovery-demo.json`
**State: CRITICAL → DEGRADED (improving)**
A complete three-phase walkthrough. Shows the full lifecycle: initial diagnostic, recalibration path application, and verification with before/after deltas. Demonstrates that recovery is iterative and that addressing Σ before P produces the best results.

---

## Using Scenarios with the Engine

Load any scenario's inputs into the Python engine:

```bash
# Interactive mode — enter the values from any scenario
python engine/recalibration_engine.py

# Or use the values directly in JSON mode
echo '{"P":0.95,"alpha":0.88,"omega":0.92,"sigma":0.05,"C":0.93,"I":0.94,"H":0.15,"phi":0.85}' | python engine/recalibration_engine.py --json
```

---

## Creating New Scenarios

If you test the protocol on a new system or under new conditions, save your diagnostic output as a JSON file following the format of the existing scenarios. See `CONTRIBUTING.md` for submission guidelines.

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
