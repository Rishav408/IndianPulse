#!/bin/bash

# India Economic Dashboard - Web Application Launcher
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "🇮🇳 Starting India Economic Dashboard Web App..."
echo "🌐 Server running at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""

# Run Flask server
python3 api_server.py
