#!/usr/bin/env bash
cd "$(dirname "$0")"

# Verificar si no existe el ejecutable dentro de .venv
if [ ! -f ".venv/bin/python" ]; then
    echo "Action: Creating .venv directory..."
    python3 -m venv .venv

    echo "Action: Upgrading pip and installing project dependencies..."
    ./.venv/bin/python -m pip install --upgrade pip
    ./.venv/bin/python -m pip install -e .
fi

./.venv/bin/python -m easysaxo.main