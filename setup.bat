@echo off
REM -----------------------------------------------------------------------------------
REM Script created for https://github.com/jasomtubratu/HeroHeroDownloader by Tomáš
REM -----------------------------------------------------------------------------------
title Installation script for HeroHeroDownloader
color B

cls
echo Checking if Python is installed...
python --version
IF %ERRORLEVEL% NEQ 0 (
    ECHO Python is not installed. Please install Python and try again.
    EXIT /B 1
)

cls
echo Installing required Python packages...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    ECHO Failed to install required Python packages.
    EXIT /B 1
)
color f

cls
set /p install_ffmpeg=Do you want to install ffmpeg using Chocolatey? (Y/N)
IF /I "%install_ffmpeg%"=="Y" (
    install_ffmpeg.bat
) ELSE (
    ECHO FFmpeg is required to download videos. So please install it manually and run main.py
    EXIT /B 1
)

echo Setup completed successfully. Now you can run main.py