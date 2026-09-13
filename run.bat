@echo off
cd /d "%~dp0"

set "PYTHON_ENV=.venv\Scripts\python.exe"

if not exist "%PYTHON_ENV%" (
    echo Action: Creating .venv directory...
    py -3 -m venv .venv

    if not exist "%PYTHON_ENV%" (
        echo.
        echo Error: Virtual environment python.exe was not created in %PYTHON_ENV%.
        echo Please ensure official Python is installed from python.org.
        pause
        exit /b 1
    )
    
    echo Action: Upgrading pip and installing project dependencies...
    "%PYTHON_ENV%" -m pip install --upgrade pip setuptools wheel
    "%PYTHON_ENV%" -m pip install -e .
)

"%PYTHON_ENV%" -m easysaxo.main
pause
