@echo off
echo Starting Heart Disease Prediction Application...
echo.

echo Installing backend dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing backend dependencies
    pause
    exit /b 1
)

echo.
echo Installing frontend dependencies...
cd frontend
npm install
if %errorlevel% neq 0 (
    echo Error installing frontend dependencies
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo Starting API server in background...
start "API Server" cmd /k "python api.py"

echo Waiting for API to start...
timeout /t 3 /nobreak > nul

echo.
echo Starting React frontend...
cd frontend
start "React Frontend" cmd /k "npm start"

echo.
echo Application started successfully!
echo - API Server: http://localhost:8000
echo - Frontend: http://localhost:3000
echo.
echo Press any key to close this window...
pause > nul