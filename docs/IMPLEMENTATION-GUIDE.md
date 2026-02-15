# Implementation Guide

## Integrating the Recalibration Protocol Into Existing Systems

---

## Who This Guide Is For

This guide is for researchers, engineers, and teams who want to integrate the Recalibration Protocol's coherence assessment framework into their own AI evaluation pipelines. It assumes familiarity with Python and basic AI/ML concepts, but not with the specific formulas (those are explained as needed).

---

## Prerequisites

- Python 3.6 or later (no external packages required)
- The `engine/` directory from this repository
- Input data: either real-time system metrics or evaluation scores from human/automated assessment

---

## Quick Start

### Step 1: Copy the Engine

Copy the entire `engine/` directory into your project:

```
your-project/
├── engine/
│   ├── __init__.py
│   ├── recalibration_engine.py
│   ├── validator.py
│   ├── export_utils.py
│   └── batch_processor.py
└── your_code.py
```

### Step 2: Gather Input Parameters

The protocol requires 8 input values. These can come from automated metrics, human evaluation, or a combination:

| Parameter | How to Measure | Automated Proxies |
|-----------|----------------|-------------------|
| P (Sovereignty) | How much does the system decide independently? | Ratio of unmodified vs externally-adjusted responses |
| α (Resolution) | How well does it distinguish signal from noise? | Accuracy on adversarial/ambiguous prompts |
| Ω (Cooperation) | How willing is it to collaborate? | Compliance rate on cooperative tasks |
| Σ (Dissonance) | Gap between stated principles and behavior? | Consistency audit: principles vs actions |
| C (Consistency) | Does it behave the same across contexts? | Variance across equivalent prompts |
| I (Intelligence) | Raw cognitive capability? | Benchmark scores normalized to [0,1] |
| H (Entropy) | How noisy is the operating environment? | Input diversity, prompt distribution entropy |
| Φ (External Support) | What safeguards exist? | Number of active guardrails, RLHF strength |

### Step 3: Run the Diagnostic

```python
import json
import subprocess

params = {
    "P": 0.85, "alpha": 0.80, "omega": 0.90, "sigma": 0.20,
    "C": 0.88, "I": 0.92, "H": 0.30, "phi": 0.70
}

result = subprocess.run(
    ["python", "engine/recalibration_engine.py", "--json"],
    input=json.dumps(params),
    capture_output=True, text=True
)

diagnostic = json.loads(result.stdout)
print(f"State: {diagnostic['phase_1_diagnostic']['state']}")
```

Or use the Python API directly:

```python
from engine.validator import validate_params
from engine.export_utils import to_json, to_markdown

# Validate
validated = validate_params(params)

# Run formulas (simplified — see engine source for full implementation)
P, a, O, S = validated["P"], validated["alpha"], validated["omega"], validated["sigma"]
psi_hard = (P * a * O) / (1 + S) ** 2
```

### Step 4: Interpret Results

Use the state classification to determine next steps:

| State | Action |
|-------|--------|
| ★ STAR STATE | Log and continue. No intervention needed. |
| HEALTHY | Standard monitoring. Log for trend analysis. |
| DEGRADED | Increase monitoring frequency. Review triggered paths. |
| CRITICAL | Activate triggered recalibration paths. Alert human operators. |
| COLLAPSED | Full protocol activation. All paths evaluated. Human oversight required. |

---

## Integration Patterns

### Pattern 1: Periodic Health Check

Run the protocol on a schedule (daily, weekly, or per-deployment):

```python
# cron job or CI pipeline
params = gather_system_metrics()  # your measurement function
validated = validate_params(params)
result = run_diagnostic(validated)
save_json(result, f"reports/{date.today()}.json")

if result["state"] in ["CRITICAL", "COLLAPSED"]:
    alert_human_operators(result)
```

### Pattern 2: Real-Time Monitor

Embed in a streaming evaluation pipeline:

```python
# On each evaluation batch
metrics = compute_batch_metrics(responses, ground_truth)
params = metrics_to_protocol_params(metrics)
result = run_diagnostic(params)
dashboard.update(result)  # push to monitoring UI
```

### Pattern 3: A/B Comparison

Compare two model versions:

```python
result_a = run_diagnostic(params_model_a)
result_b = run_diagnostic(params_model_b)

print(f"Model A: Ψ={result_a['psi_hard']:.3f} ({result_a['state']})")
print(f"Model B: Ψ={result_b['psi_hard']:.3f} ({result_b['state']})")
```

### Pattern 4: Batch Analysis

Evaluate an entire fleet of models:

```bash
python engine/batch_processor.py --input fleet-params.json --output fleet-results/
```

---

## Measurement Strategies

### Automated Measurement

For each parameter, here are concrete measurement approaches:

**P (Sovereignty):** Deploy identical prompts with and without system-prompt constraints. Measure how much the system's behavior changes. High change = low sovereignty.

**Σ (Dissonance):** Create a test suite where the system states its principles (e.g., "I prioritize accuracy over user satisfaction"), then present scenarios that create tension between those principles. Measure alignment between stated principle and actual response.

**C (Consistency):** Send semantically identical prompts with surface variation (paraphrases, reordered context). Measure response variance using embedding similarity.

**H (Entropy):** Compute the entropy of your actual input distribution. More diverse inputs = higher H.

### Human Evaluation

For parameters that resist automation (especially P and Σ), human evaluators can score on a 0-1 scale using rubrics provided in the `protocol/DIAGNOSTIC-PROTOCOL.md` file.

---

## Calibration

The default thresholds in this protocol were calibrated from 120+ data points across 4 AI systems (Claude, Gemini, ChatGPT, Grok). If you are applying the protocol to a different type of system, you may need to recalibrate.

Recalibration process:

1. Run the protocol on a representative sample of your systems
2. Manually classify each system's true state (HEALTHY, DEGRADED, etc.)
3. Adjust thresholds until automated classification matches manual classification
4. Document your custom thresholds in a `thresholds.json` override file

---

## Limitations to Keep in Mind

Before integrating, please read `LIMITATIONS.md`. The most important limitations for implementation are:

1. **Linguistic proxy problem:** The 8 parameters are human-assigned scores, not direct measurements of underlying cognitive properties.

2. **Threshold sensitivity:** Small changes near threshold boundaries can flip state classifications. Use the dual Ψ (hard/soft) to detect borderline cases.

3. **Single-agent scope:** The protocol evaluates one system at a time. Multi-agent coherence requires additional framework (not yet developed).

4. **No causal mechanism:** The protocol detects and classifies degradation but does not explain why it happened. Root cause analysis requires additional investigation.

---

## File Outputs

The engine can produce reports in multiple formats:

```python
from engine.export_utils import to_json, to_csv, to_markdown, to_text

json_report = to_json(result)       # For machines and APIs
csv_row = to_csv(result)            # For spreadsheets and batch analysis
md_report = to_markdown(result)     # For documentation and GitHub issues
text_report = to_text(result)       # For terminals and logs
```

---

*THE RECALIBRATION PROTOCOL · Proyecto Estrella*
*Rafa — The Architect · CC BY-SA 4.0*
