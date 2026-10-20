#!/bin/bash

# Resolve paths relative to this script so it works from any directory
cd "$(dirname "$(readlink -f "$0")")" || exit 1

# uv lives in ~/.local/bin, which is missing from PATH in non-login shells
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

# Sync dependencies
echo "Syncing dependencies..."
if ! uv sync; then
    echo "Sync failed. Please ensure 'uv' is installed."
    exit 1
fi

# Local development: the app refuses to start without SECRET_KEY unless debug is on
export FLASK_DEBUG=1

# Start the application
echo "Starting the Quantitative Finance Flash Cards app..."
echo "The app will be available at http://127.0.0.1:5000"
uv run python run.py
