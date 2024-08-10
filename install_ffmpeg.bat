@echo off
REM This script installs FFmpeg using Chocolatey.
REM Chocolatey is a package manager for Windows.
REM FFmpeg is a multimedia framework that can encode, decode, transcode, mux, demux, stream, filter, and play almost anything that humans and machines have created.
REM -----------------------------------------------------------------------------------
REM Script created for https://github.com/jasomtubratu/HeroHeroDownloader by Tomáš
REM -----------------------------------------------------------------------------------
title Install FFmpeg using Chocolatey
echo Installing FFmpeg...

net session >nul 2>&1
if %errorLevel% == 0 (
    echo User has administrative privileges.
    goto continue
) else (
    echo User does not have administrative privileges. Please run this script as an administrator.
    pause
    exit
)

:continue
echo Checking if FFmpeg is already installed...
ffmpeg -version >nul 2>&1
if %errorLevel% == 0 (
    echo FFmpeg is already installed.
    pause
    exit
)

echo Checking if chocolatey is installed...
choco -v >nul 2>&1
if %errorLevel% == 0 (
    echo Chocolatey is already installed.
    goto install_ffmpeg
) else (
    echo Installing Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    if %errorLevel% == 0 (
        echo Chocolatey has been installed.
        goto install_ffmpeg
    ) else (
        echo Failed to install Chocolatey.
        pause
        exit
    )
)

:install_ffmpeg
echo Installing FFmpeg...
choco install ffmpeg -y
if %errorLevel% == 0 (
    echo FFmpeg has been installed.
    pause
    exit
) else (
    echo Failed to install FFmpeg.
    pause
    exit
)