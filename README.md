# AOC Python Workspace

This workspace has been configured for Python development with Antigravity IDE.

## Getting Started

1. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate
   ```
2. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   # Install development packages in editable mode
   pip install -e .[dev]
   ```
3. **Run tests**:
   ```bash
   pytest
   ```
4. **Lint and format with Ruff**:
   ```bash
   ruff check .
   ruff format .
   ```
