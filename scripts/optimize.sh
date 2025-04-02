#!/bin/bash
# Automatically run the image optimizer using the virtual environment

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"
OPTIMIZER="$SCRIPT_DIR/optimize_images.py"

# Activate virtual environment and run optimizer
"$VENV_PYTHON" "$OPTIMIZER" "$@"
