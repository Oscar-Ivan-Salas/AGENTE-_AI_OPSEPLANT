#!/bin/bash

echo "🔁 Desinstalando posibles versiones incompatibles..."
pip uninstall -y python-telegram-bot telegram

echo "🧹 Limpiando cachés..."
pip cache purge

echo "📦 Instalando versión compatible: python-telegram-bot==20.3..."
pip install python-telegram-bot==20.3 --user

echo "✅ Instalación completada."
