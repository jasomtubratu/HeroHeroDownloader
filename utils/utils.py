import subprocess
import platform
import os
import sys
import time

def construct_headers(access_token):
    return {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "sec-ch-ua": '"Brave";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "cookie": f'accessToken2="{access_token}"',
        "Referer": "https://herohero.co/",
        "Referrer-Policy": "origin"
    }

def clear_console():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

def change_cmd_title(title):
    if os.name == "nt":
        subprocess.run(f"title {title}", shell=True)

def check_ffmpeg_installation():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError:
        print("⚠️ FFmpeg is installed but there was an issue running it.")
        time.sleep(5)
        sys.exit(1)
    except FileNotFoundError:
        print("❌ FFmpeg is not installed. Please install it.")
        time.sleep(5)
        sys.exit(1)
    else:
        print("✅ FFmpeg is installed.")
        return True
