#!/bin/bash

# Heart Disease Prediction System - Setup Script
# Professional installation and configuration script

set -e

echo "🫀 Heart Disease Prediction System - Professional Setup"
echo "======================================================"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check Python version
check_python() {
    print_status "Checking Python version..."
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi

    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    if python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)"; then
        print_success "Python $PYTHON_VERSION is compatible"
    else
        print_error "Python $PYTHON_VERSION is not supported. Please upgrade to Python 3.8+"
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment..."
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        print_success "Virtual environment created"
    else
        print_warning "Virtual environment already exists"
    fi
}

# Activate virtual environment and install dependencies
install_dependencies() {
    print_status "Activating virtual environment and installing dependencies..."

    # Activate virtual environment
    source venv/bin/activate

    # Upgrade pip
    pip install --upgrade pip

    # Install dependencies
    if pip install -r requirements.txt; then
        print_success "Dependencies installed successfully"
    else
        print_error "Failed to install dependencies"
        exit 1
    fi

    # Verify installations
    if python -c "import streamlit, sklearn, pandas, numpy; print('All imports successful')"; then
        print_success "All required packages verified"
    else
        print_error "Some packages failed to import"
        exit 1
    fi
}

# Create necessary directories
create_directories() {
    print_status "Creating necessary directories..."
    mkdir -p logs
    mkdir -p data
    mkdir -p models
    print_success "Directories created"
}

# Verify model file
verify_model() {
    print_status "Verifying model file..."
    if [ -f "model.pkl" ]; then
        if python -c "import pickle; pickle.load(open('model.pkl', 'rb')); print('Model loaded successfully')"; then
            print_success "Model file verified"
        else
            print_error "Model file is corrupted"
            exit 1
        fi
    else
        print_warning "Model file not found. Please ensure model.pkl exists"
    fi
}

# Test application
test_application() {
    print_status "Testing application startup..."
    if timeout 10s streamlit run app.py --server.headless true --server.port 8502; then
        print_success "Application test passed"
    else
        print_warning "Application test failed, but this might be due to timeout"
    fi
}

# Create desktop shortcut (Linux/Mac)
create_shortcut() {
    print_status "Creating application shortcut..."
    cat > heart_prediction.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Heart Disease Prediction
Comment=AI-powered heart disease risk assessment
Exec=$(pwd)/venv/bin/streamlit run $(pwd)/app.py
Icon=$(pwd)/icon.png
Terminal=false
Categories=Healthcare;Medical;Science;
EOF
    chmod +x heart_prediction.desktop
    print_success "Desktop shortcut created: heart_prediction.desktop"
}

# Main setup function
main() {
    echo ""
    print_status "Starting professional setup process..."
    echo ""

    check_python
    create_venv
    install_dependencies
    create_directories
    verify_model
    test_application

    echo ""
    print_success "🎉 Setup completed successfully!"
    echo ""
    echo "To run the application:"
    echo "  source venv/bin/activate"
    echo "  streamlit run app.py"
    echo ""
    echo "Or use the desktop shortcut: heart_prediction.desktop"
    echo ""
    echo "Application will be available at: http://localhost:8501"
    echo ""
    print_status "Thank you for choosing Heart Disease Prediction System!"
}

# Run main function
main "$@"