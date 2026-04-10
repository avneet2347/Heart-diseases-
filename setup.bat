@echo off
REM Heart Disease Prediction System - Windows Setup Script
REM Professional installation and configuration script

echo 🫀 Heart Disease Prediction System - Professional Setup
echo ======================================================

REM Check Python version
echo [INFO] Checking Python version...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [SUCCESS] Python %PYTHON_VERSION% detected

REM Create virtual environment
echo [INFO] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo [SUCCESS] Virtual environment created
) else (
    echo [WARNING] Virtual environment already exists
)

REM Activate virtual environment and install dependencies
echo [INFO] Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [SUCCESS] Dependencies installed successfully

REM Verify installations
python -c "import streamlit, sklearn, pandas, numpy; print('All imports successful')" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Some packages failed to import
    pause
    exit /b 1
)
echo [SUCCESS] All required packages verified

REM Create necessary directories
echo [INFO] Creating necessary directories...
if not exist logs mkdir logs
if not exist data mkdir data
if not exist models mkdir models
echo [SUCCESS] Directories created

REM Verify model file
echo [INFO] Verifying model file...
if exist model.pkl (
    python -c "import pickle; pickle.load(open('model.pkl', 'rb')); print('Model loaded successfully')" >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERROR] Model file is corrupted
        pause
        exit /b 1
    ) else (
        echo [SUCCESS] Model file verified
    )
) else (
    echo [WARNING] Model file not found. Please ensure model.pkl exists
)

REM Test application
echo [INFO] Testing application startup...
timeout /t 5 /nobreak >nul
start /b streamlit run app.py --server.headless true --server.port 8502
timeout /t 3 /nobreak >nul
taskkill /f /im streamlit.exe >nul 2>&1
echo [SUCCESS] Application test completed

echo.
echo 🎉 Setup completed successfully!
echo.
echo To run the application:
echo   venv\Scripts\activate.bat
echo   streamlit run app.py
echo.
echo Application will be available at: http://localhost:8501
echo.
echo [INFO] Thank you for choosing Heart Disease Prediction System!
echo.
pause