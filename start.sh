#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Check if API key is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    if [ -f .env ]; then
        export $(cat .env | grep -v '^#' | xargs)
    else
        echo "⚠️  WARNING: ANTHROPIC_API_KEY not set!"
        echo ""
        echo "Please either:"
        echo "1. Create a .env file with: ANTHROPIC_API_KEY=your-key-here"
        echo "2. Or run: export ANTHROPIC_API_KEY='your-key-here'"
        echo ""
        echo "Get your API key from: https://console.anthropic.com/"
        echo ""
        exit 1
    fi
fi

# Start the server
echo "🐄 Starting Hoof Analyzer..."
echo "📱 Open your browser to: http://localhost:5000"
echo ""
python app.py
