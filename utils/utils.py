import datetime
import subprocess
import platform
from colorama import Fore, Style

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
        "cookie": f"accessToken=\"{access_token}\"",
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

def print_blue(text):
    print(Fore.BLUE + text + Style.RESET_ALL)

def check_ffmpeg_installation():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("FFmpeg is installed. You can continue.")
    except subprocess.CalledProcessError:
        print("FFmpeg is not installed. Please install it.")
        return
