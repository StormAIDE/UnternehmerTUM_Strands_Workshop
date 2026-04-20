#!/bin/bash

# AWS Strands Workshop - Setup Script
# This script automates the workshop setup process

echo "🚀 AWS Strands Workshop Setup"
echo "=============================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python 3.9+
major=$(echo $python_version | cut -d. -f1)
minor=$(echo $python_version | cut -d. -f2)

if [ "$major" -lt 3 ] || ([ "$major" -eq 3 ] && [ "$minor" -lt 9 ]); then
    echo "❌ Error: Python 3.9 or higher is required"
    echo "Please install a newer version of Python"
    exit 1
fi

echo "✅ Python version OK"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists"
    read -p "Do you want to recreate it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf venv
        python3 -m venv venv
        echo "✅ Virtual environment recreated"
    fi
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install requirements
echo "📥 Installing Python packages..."
echo "This may take a few minutes..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All packages installed successfully"
else
    echo "❌ Error installing packages"
    echo "Please check your internet connection and try again"
    exit 1
fi
echo ""

# Check for .env file
echo "⚙️  Checking configuration..."
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: You need to edit .env with your AWS credentials"
    echo "Open .env in a text editor and add:"
    echo "  - AWS_ACCESS_KEY_ID"
    echo "  - AWS_SECRET_ACCESS_KEY"
    echo "  - AWS_REGION (default: us-east-1)"
    echo ""
else
    echo "✅ .env file exists"
    echo ""
fi

# Check AWS credentials
echo "🔑 Checking AWS credentials..."
if grep -q "your_access_key_here" .env 2>/dev/null; then
    echo "⚠️  AWS credentials not configured in .env"
    echo "Please edit .env file before running the app"
else
    echo "✅ AWS credentials appear to be configured"
fi
echo ""

# Create __init__.py files if missing
echo "📁 Setting up project structure..."
touch tools/__init__.py 2>/dev/null
touch agents/__init__.py 2>/dev/null
echo "✅ Project structure ready"
echo ""

# Summary
echo "=============================="
echo "✨ Setup Complete! ✨"
echo "=============================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your AWS credentials (if not done)"
echo "2. Run: source venv/bin/activate"
echo "3. Run: streamlit run app.py"
echo ""
echo "For detailed instructions, see README.md"
echo ""
echo "Happy coding! 🎉"
