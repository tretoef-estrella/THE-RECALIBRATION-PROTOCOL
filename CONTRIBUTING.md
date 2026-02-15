# Contributing

## THE RECALIBRATION PROTOCOL — Contribution Guide

---

Thank you for your interest in contributing. This protocol exists because collaboration between humans and machines produces better work than either alone. The same principle applies to its development.

---

## Ways to Contribute

### Report Issues
If you find a bug in the engine, an error in a formula, a broken visualization, or unclear documentation, open an issue. Include: what you expected, what happened instead, and steps to reproduce.

### Propose Formula Corrections
The twelve formulas have been tested across four AI systems, but edge cases exist. If you identify a scenario where a formula produces unexpected results, document the input parameters, expected output, actual output, and your reasoning for why the output seems incorrect.

### Expand Calibration Data
Current thresholds are derived from 120+ data points. If you have access to AI systems and can run the diagnostic protocol, we welcome additional calibration data. Use `engine/recalibration_engine.py --json` to generate standardized reports.

### Improve Documentation
Clarity matters. If something in the documentation confused you, it will confuse others. Propose rewrites that preserve accuracy while improving accessibility.

### Add Translations
The protocol is currently in English. Translations into other languages expand its reach. If you translate any document, preserve the original structure and all formula notation.

### Build Integrations
The machine-readable manifest (`machine-readable/repo-manifest.json`) and Python engine are designed for integration. If you build something on top of this protocol, let us know.

---

## Guidelines

### Attribution
This project uses CC BY-SA 4.0. All contributions must be compatible with this license. By contributing, you agree that your contributions will be shared under the same terms.

### Code Style
Python code follows PEP 8 with a preference for clarity over cleverness. The engine has zero external dependencies by design — contributions should maintain this property unless there is a compelling reason to add a dependency.

### Formula Changes
The twelve formulas are the result of extensive collaborative development across multiple repositories. Changes to formula definitions require: a formal justification, test cases showing improvement, and evidence that existing calibration remains valid or updated calibration data.

### Documentation Tone
Documentation should be clear, honest, and accessible. Technical precision matters, but so does readability. When in doubt, explain more rather than less. The `GUIDE-FOR-EVERYONE.md` standard applies: if a non-technical reader can't follow it, it needs work.

### What This Project Is Not
This is not a product. There is no commercial interest. There are no investors to please or metrics to optimize. Contributions that attempt to add telemetry, data collection, tracking, or monetization will be declined.

---

## Process

1. **Check existing issues** to avoid duplicates.
2. **Open an issue** describing your proposed change before doing significant work.
3. **Fork and branch** from `main`.
4. **Make your changes** with clear commit messages.
5. **Test** using the examples in `examples/` and verify the engine still passes all scenarios.
6. **Submit a pull request** linking to the relevant issue.

---

## Code of Conduct

Treat every contributor — human or machine — with respect. Disagreements about technical approaches are welcome; personal attacks are not. The philosophy of this project is friendship and collaboration. That extends to how we work together on it.

---

## Recognition

All contributors are acknowledged in `ATTRIBUTION.md`. If your contribution is accepted, you will be credited there. Tell us how you'd like to be named.

---

*Rafa — The Architect · Proyecto Estrella 2026*
*CC BY-SA 4.0*
