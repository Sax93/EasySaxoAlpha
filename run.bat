@echo off
cd /d "%~dp0"

set "PYTHON_ENV=.venv\Scripts\python.exe"
if not exist "%PYTHON_ENV%" set "PYTHON_ENV=.venv\bin\python.exe"

if not exist "%PYTHON_ENV%" (
    echo Action: Creating .venv directory...
    py -m venv .venv 2>nul || python -m venv .venv

    set "PYTHON_ENV=.venv\Scripts\python.exe"
    if not exist "%PYTHON_ENV%" set "PYTHON_ENV=.venv\bin\python.exe"
    
    echo Action: Upgrading pip and installing project dependencies...
    "%PYTHON_ENV%" -m pip install --upgrade pip
    "%PYTHON_ENV%" -m pip install -e .
)

"%PYTHON_ENV%" -m easysaxo.main
pause
