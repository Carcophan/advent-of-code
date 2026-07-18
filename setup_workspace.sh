#!/usr/bin/env bash
set -e

echo "=== Initializing Python Workspace ==="

# 1. Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment (.venv)..."
    python3 -m venv .venv
else
    echo "Virtual environment (.venv) already exists."
fi

# 2. Upgrade pip and install development dependencies
echo "Installing/upgrading package dependencies..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .[dev]

# 3. Verify workspace setup by running pytest and ruff
echo "Running pytest verification..."
.venv/bin/pytest

echo "Running ruff formatting and linting..."
.venv/bin/ruff format src/ tests/
.venv/bin/ruff check --fix src/ tests/

echo "=== Workspace Setup Complete ==="
echo "To activate the virtual environment, run:"
echo "source .venv/bin/activate"
