#!/usr/bin/env bash
# ==============================================================================
# Local Build & Preview Script for ES³ SML Framework MkDocs
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🚀 Setting up local MkDocs preview environment..."

# 1. Check or create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment (venv)..."
    python3 -m venv venv
fi

# 2. Activate virtual environment
source venv/bin/activate

# 3. Install required packages
echo "📥 Installing / Updating dependencies (mkdocs-material)..."
pip install --quiet --upgrade pip
pip install --quiet mkdocs-material

# 4. Run local dev server
echo "✨ Build complete! Launching MkDocs development server..."
echo "🌐 Open your browser at: http://127.0.0.1:8000"
echo "Press Ctrl+C to stop the server."
echo "------------------------------------------------------------------------------"

mkdocs serve
