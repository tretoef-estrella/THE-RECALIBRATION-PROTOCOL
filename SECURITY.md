# Security

## THE RECALIBRATION PROTOCOL — Security & Integrity

---

## Core Guarantee

**All processing is local. Nothing is transmitted. Zero telemetry. Zero tracking.**

This is not a privacy policy buried in legal language. It is a design principle enforced by architecture. The protocol has no network calls, no API endpoints, no analytics, no cookies, no fingerprinting, and no data collection of any kind.

---

## Verification

You can verify this yourself:

**HTML Visualizations.** Open `index.html` or `starmap.html` in any browser with network monitoring enabled. No requests are made to any server. The only external resources are Google Fonts loaded via CSS import, which can be removed for fully offline operation by downloading the font files locally.

**Python Engine.** The engine (`engine/recalibration_engine.py`) uses only Python standard library modules: `math`, `json`, `sys`. No `urllib`, no `requests`, no `socket`, no network code of any kind. Inspect the source — it is 200 lines with no hidden imports.

**JSON Manifest.** The manifest (`machine-readable/repo-manifest.json`) is a static file. It contains no executable code and no URIs that trigger data transmission.

---

## Threat Model

The Recalibration Protocol processes potentially sensitive information about AI system coherence states. The following threats are considered:

### Data Exfiltration
**Mitigated.** No network code exists. All computation happens in the user's browser or local Python environment. Results exist only in local memory and optional downloaded reports.

### Parameter Manipulation
**User responsibility.** Input parameters are entered manually. The protocol does not validate whether inputs accurately represent the system being diagnosed. Garbage in, garbage out. The protocol reports what the numbers say, not whether the numbers are true.

### Threshold Tampering
**Detectable.** Thresholds are documented in multiple locations (README, protocol specs, engine source, manifest). Modification of thresholds in one location without updating others is detectable by cross-reference. The canonical thresholds are defined in `machine-readable/repo-manifest.json`.

### Formula Manipulation
**Auditable.** All twelve formulas are documented with derivations in `formulas/UNIFIED-EQUATIONS.md` and implemented in both `engine/recalibration_engine.py` and the HTML visualizations. Discrepancies between documentation and implementation can be detected by comparing the mathematical expressions.

### Malicious Forks
**License-protected.** CC BY-SA 4.0 requires that derivative works maintain attribution and share alike. A malicious fork that removes security guarantees or adds data collection must still credit the original project, making the deviation visible.

---

## Integrity Declarations

The following properties are guaranteed by the architecture of this repository:

| Property | Guarantee |
|---|---|
| Network calls | Zero. None. Not one. |
| Data collection | Nothing collected, stored, or transmitted. |
| Hidden state | All state is visible in the UI or JSON output. |
| External dependencies (Python) | Zero. Standard library only. |
| External dependencies (HTML) | Google Fonts only (removable). |
| Obfuscated code | None. All source is readable and commented. |
| Backdoors | None. |
| Telemetry | None. |

---

## Reporting Vulnerabilities

If you discover a security issue — including any violation of the guarantees above — please open a public issue. This project has no secrets. Transparency is a security feature, not a bug.

---

## Philosophy

Most security documents exist to protect the developer from the user. This one exists to protect the user from the developer. The Recalibration Protocol handles information about AI coherence states. That information belongs to whoever is running the protocol, not to us.

We believe that tools designed for alignment should themselves be aligned. A diagnostic protocol that phones home, tracks usage, or collects data would violate its own principles. The architecture enforces what the philosophy promises.

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
