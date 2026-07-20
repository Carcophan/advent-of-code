#!/usr/bin/env bash

# This script spawns a new shell session with the virtual environment activated,
# allowing you to run it directly (e.g., `./activate_venv.sh`) instead of using `source`.

VENV_PATH="/home/joachim/projects/aoc/.venv"

if [ ! -d "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found at $VENV_PATH"
    echo "Please run ./setup_workspace.sh first."
    exit 1
fi

echo "Activating virtual environment in a new bash session..."
echo "Type 'exit' or press Ctrl+D to leave the virtual environment."

# Replace the current process with a new bash shell that loads your .bashrc and then activates the venv
exec bash --init-file <(echo "[[ -f ~/.bashrc ]] && source ~/.bashrc; source '$VENV_PATH/bin/activate'")
