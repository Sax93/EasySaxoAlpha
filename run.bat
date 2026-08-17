@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] No se encontro el ejecutable Python en .venv\Scripts\python.exe
    echo Por favor, verifica el nombre de tu entorno virtual o crealo con: python -m venv .venv
    pause
    exit /b
)

".venv\Scripts\python.exe" -m easysaxo.main
pause