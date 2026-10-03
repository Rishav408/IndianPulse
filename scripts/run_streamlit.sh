#!/bin/bash

# India Economic Dashboard - Streamlit Launcher
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "🇮🇳 Starting Streamlit dashboard..."
echo "📍 Dashboard will open at: http://localhost:8501"
echo "Press Ctrl+C to stop the dashboard"
echo ""

# Run Streamlit
streamlit run app/dashboard.py
