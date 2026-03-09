@echo off
echo Syncing dependencies...
uv sync
if %ERRORLEVEL% neq 0 (
    echo Sync failed. Please ensure 'uv' is installed.
    pause
    exit /b %ERRORLEVEL%
)

echo Starting the Quantitative Finance Flash Cards app...
echo The app will be available at http://127.0.0.1:5000
uv run python run.py
pause
