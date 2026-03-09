#!/bin/bash

# Sync dependencies
echo "Syncing dependencies..."
if ! uv sync; then
    echo "Sync failed. Please ensure 'uv' is installed."
    exit 1
fi

# Start the application
echo "Starting the Quantitative Finance Flash Cards app..."
echo "The app will be available at http://127.0.0.1:5000"
uv run python run.py
