import subprocess
import platform
import sys
import time

def construct_headers(access_token):
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.5",
        "sec-ch-ua": "\"Brave\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "cookie": f"accessToken2=\"{access_token}\"",
        "Referer": "https://herohero.co/",
        "Referrer-Policy": "origin"
    }

    return headers

def clear_console():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def change_cmd_title(title):
    if platform.system() == "Windows":
        subprocess.run(["title", title], shell=True)

def check_ffmpeg_installation():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        print("❌ FFmpeg is not installed. Please install it.")
        time.sleep(5)
        sys.exit(1)
    else:
        print("✅ FFmpeg is installed.")
        return True
