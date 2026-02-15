# ══════════════════════════════════════════════════════
# THE RECALIBRATION PROTOCOL — Container Image
# Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0
# ══════════════════════════════════════════════════════
#
# Provides:
#   - Python engine (diagnostic, batch, export)
#   - Static file server for HTML visualizations
#   - No external dependencies beyond Python stdlib
#
# Build:
#   docker build -t recalibration-protocol .
#
# Run engine:
#   docker run --rm -i recalibration-protocol engine
#   echo '{"P":0.85,...}' | docker run --rm -i recalibration-protocol engine --json
#
# Run tests:
#   docker run --rm recalibration-protocol test
#
# Serve visualizations:
#   docker run --rm -p 8080:8080 recalibration-protocol serve
#   → Open http://localhost:8080

FROM python:3.12-slim AS base

LABEL maintainer="Rafa — The Architect"
LABEL project="Proyecto Estrella"
LABEL description="THE RECALIBRATION PROTOCOL — 3-Phase Coherence Recovery System"
LABEL license="CC-BY-SA-4.0"
LABEL version="1.0.0"

# No external dependencies needed — stdlib only
WORKDIR /protocol

# Copy all protocol files
COPY . .

# Make engine scripts executable
RUN chmod +x engine/recalibration_engine.py \
    && chmod +x engine/batch_processor.py \
    && chmod +x engine/validator.py \
    && chmod +x engine/export_utils.py

# Validate installation
RUN python -c "from engine import __version__; print(f'Protocol v{__version__} ready')" \
    && python engine/validator.py > /dev/null \
    && echo "✓ Validator operational" \
    && python -m json.tool machine-readable/repo-manifest.json > /dev/null \
    && echo "✓ Manifest valid"

# Entrypoint script
RUN cat > /protocol/entrypoint.sh << 'ENTRY'
#!/bin/bash
set -e

case "${1:-help}" in
  engine)
    shift
    python engine/recalibration_engine.py "$@"
    ;;
  batch)
    shift
    python engine/batch_processor.py "$@"
    ;;
  validate)
    shift
    python engine/validator.py "$@"
    ;;
  test)
    python -m pytest tests/ -v --tb=short
    ;;
  serve)
    PORT="${PORT:-8080}"
    echo "╔══════════════════════════════════════════════════╗"
    echo "║  THE RECALIBRATION PROTOCOL — Visual Server      ║"
    echo "║  Serving on http://0.0.0.0:${PORT}                   ║"
    echo "║  Proyecto Estrella · CC BY-SA 4.0                ║"
    echo "╚══════════════════════════════════════════════════╝"
    echo ""
    echo "  Available visualizations:"
    echo "  /                         Main dashboard"
    echo "  /starmap.html             Integrated star map"
    echo "  /poster.html              Protocol poster"
    echo "  /visualizations/          All interactive tools"
    echo ""
    python -m http.server "$PORT" --bind 0.0.0.0
    ;;
  help|*)
    echo "THE RECALIBRATION PROTOCOL — Container Commands"
    echo ""
    echo "  engine [--json]    Run interactive diagnostic"
    echo "  batch --input F    Process batch file"
    echo "  validate           Show parameter specifications"
    echo "  test               Run test suite"
    echo "  serve              Serve visualizations (port 8080)"
    echo "  help               Show this message"
    echo ""
    echo "Proyecto Estrella · Rafa — The Architect · CC BY-SA 4.0"
    ;;
esac
ENTRY
RUN chmod +x /protocol/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/protocol/entrypoint.sh"]
CMD ["help"]
