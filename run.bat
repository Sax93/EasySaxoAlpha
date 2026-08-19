@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Action: Creating .venv directory...
    python -m venv .venv
    
    echo Action: Upgrading pip and installing project dependencies...
    ".venv\Scripts\python.exe" -m pip install --upgrade pip
    ".venv\Scripts\python.exe" -m pip install -e .
)

".venv\Scripts\python.exe" -m easysaxo.main
pause