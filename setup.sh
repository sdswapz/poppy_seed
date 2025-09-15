#!/bin/bash

# Poppy Seed - Android Static Analyzer Setup Script
# This script sets up and runs the Poppy Seed Django application

echo "🌱 Poppy Seed - Android Static Analyzer Setup"
echo "=============================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION detected"

# Navigate to Django directory
if [ ! -d "Django" ]; then
    echo "❌ Django directory not found. Please run this script from the poppy_seed root directory."
    exit 1
fi

cd Django
echo "📁 Changed to Django directory"

# Check if Django is installed
if ! python3 -c "import django" &> /dev/null; then
    echo "📦 Installing Django..."
    pip3 install django
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Django. Please install it manually: pip3 install django"
        exit 1
    fi
    echo "✅ Django installed successfully"
else
    echo "✅ Django is already installed"
fi

# Run migrations
echo "🗄️  Running database migrations..."
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo "❌ Database migration failed. Please check the error messages above."
    exit 1
fi
echo "✅ Database migrations completed"

# Start the development server
echo "🚀 Starting Poppy Seed development server..."
echo ""
echo "📱 Access the application at:"
echo "   • Main Interface: http://127.0.0.1:8000/"
echo "   • Upload Page: http://127.0.0.1:8000/"
echo "   • About Page: http://127.0.0.1:8000/about/"
echo "   • Repository: http://127.0.0.1:8000/repo/"
echo "   • Admin Panel: http://127.0.0.1:8000/admin/"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo ""

python3 manage.py runserver
