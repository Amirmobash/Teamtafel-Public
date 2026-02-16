@echo off
echo Starting Employee Management System - Management App...
cd /d "%~dp0ManagementApp"

REM Check if ManagementApp.exe exists
if not exist "ManagementApp.exe" (
    echo ERROR: ManagementApp.exe not found in %CD%
    pause
    exit /b 1
REM Check if the process is running
tasklist /FI "IMAGENAME eq ManagementApp.exe" 2>NUL | find /I /N "ManagementApp.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo Management App started successfully!
    echo The ap





