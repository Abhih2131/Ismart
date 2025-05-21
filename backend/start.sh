#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "▶️ Setting up Python virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run the FastAPI server
echo "🚀 Starting FastAPI server at http://127.0.0.1:8000 ..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
