@echo off
REM Run script for NotePad Pro (Windows)

echo Starting NotePad Pro...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    
    echo Installing dependencies...
    call venv\Scripts\activate.bat
    pip install -q -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Run the application
python main.py
