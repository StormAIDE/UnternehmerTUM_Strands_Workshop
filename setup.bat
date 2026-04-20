@echo off
REM AWS Strands Workshop - Setup Script for Windows
REM This script automates the workshop setup process

echo ========================================
echo AWS Strands Workshop Setup
echo ========================================
echo.

REM Check Python version
echo Checking Python version...
python --version 2>NUL
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher
    pause
    exit /b 1
)
echo Python found!
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist "venv\" (
    echo Warning: Virtual environment already exists
    choice /C YN /M "Do you want to recreate it"
    if errorlevel 2 goto skipvenv
    if errorlevel 1 (
        rmdir /s /q venv
        python -m venv venv
        echo Virtual environment recreated
    )
) else (
    python -m venv venv
    echo Virtual environment created
)
:skipvenv
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Install requirements
echo Installing Python packages...
echo This may take a few minutes...
python -m pip install --upgrade pip >NUL 2>&1
pip install -r requirements.txt

if errorlevel 1 (
    echo Error installing packages
    echo Please check your internet connection and try again
    pause
    exit /b 1
)
echo All packages installed successfully
echo.

REM Check for .env file
echo Checking configuration...
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env >NUL
    echo .env file created
    echo.
    echo IMPORTANT: You need to edit .env with your AWS credentials
    echo Open .env in a text editor and add:
    echo   - AWS_ACCESS_KEY_ID
    echo   - AWS_SECRET_ACCESS_KEY
    echo   - AWS_REGION (default: us-east-1)
    echo.
) else (
    echo .env file exists
    echo.
)

REM Create __init__.py files
echo Setting up project structure...
type nul > tools\__init__.py 2>NUL
type nul > agents\__init__.py 2>NUL
echo Project structure ready
echo.

REM Summary
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file with your AWS credentials (if not done)
echo 2. Run: venv\Scripts\activate
echo 3. Run: streamlit run app.py
echo.
echo For detailed instructions, see README.md
echo.
echo Happy coding!
echo.
pause
