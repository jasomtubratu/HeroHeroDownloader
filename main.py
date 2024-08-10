from colorama import Fore, Style
from utils.utils import clear_console, change_cmd_title, check_ffmpeg_installation
from utils.download_all import get_all_videos
from utils.user_data import get_user_data

def prompt_herohero_credentials():
    herohero_account = input("❓ Enter the user you want to download (from the url): ")
    access_token = input("❓ Enter your accessToken to your HeroHero account: ")
    access_token = access_token.strip('"')
    return herohero_account, access_token

def what_you_want_to_do():
    print ("❓ What do you want to do?")
    print ("[1] Download whole user´s profile")
    print ("[2] Download a specific post (video/image/text)")
    print ("[3] Download user metadata")
    print ("[4] Exit")
    choice = input("Enter your choice: ")

    if choice not in ['1', '2', '3', '4']:
        clear_console()
        what_you_want_to_do()
    return choice

def main():
    clear_console()
    change_cmd_title("HeroHeroDownloader")
    print(Fore.BLUE + """
██╗  ██╗███████╗██████╗  ██████╗ ██╗  ██╗███████╗██████╗  ██████╗                     
██║  ██║██╔════╝██╔══██╗██╔═══██╗██║  ██║██╔════╝██╔══██╗██╔═══██╗                    
███████║█████╗  ██████╔╝██║   ██║███████║█████╗  ██████╔╝██║   ██║                    
██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══██║██╔══╝  ██╔══██╗██║   ██║                    
██║  ██║███████╗██║  ██║╚██████╔╝██║  ██║███████╗██║  ██║╚██████╔╝                    
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝                     
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                      
    """ + Style.RESET_ALL)

    check_ffmpeg_installation()
    choice = what_you_want_to_do()

    account, access_token = prompt_herohero_credentials()

    if choice == '1':
        herohero_account_id = get_user_data(account, access_token)
        get_all_videos(herohero_account_id, access_token)
    elif choice == '2':
        print ("❌ Not implemented yet")
    elif choice == '3':
        get_user_data(account, access_token)
    elif choice == '4':
        print ("🚪 Exiting...")
        exit()


if __name__ == "__main__":
    main()
