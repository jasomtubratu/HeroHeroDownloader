from colorama import Fore, Style
from utils.get_post import get_post
from utils.utils import clear_console, change_cmd_title, check_ffmpeg_installation
from utils.download_all import get_all_posts
from utils.user_data import get_user_data

def prompt_herohero_credentials():
    herohero_account = input("❓ Enter the user you want to download (ex. https://herohero.co/{user}}): ")
    access_token = input("❓ Enter your accessToken2 to your HeroHero account: ").strip('"')
    return herohero_account, access_token

def what_you_want_to_do():
    options = {
        '1': "Download whole user's profile",
        '2': "Download a specific post (video/image/text) | DOES NOT WORK!!! DO NOT USE!!",
        '3': "Download user metadata",
        '4': "Exit"
    }
    while True:
        print("❓ What do you want to do?")
        for key, desc in options.items():
            print(f"[{key}] {desc}")
        choice = input("Enter your choice: ").strip()
        
        if choice in options:
            return choice
        else:
            print(Fore.RED + "❌ Invalid choice, please try again." + Style.RESET_ALL)
            clear_console()

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

    while True:
        choice = what_you_want_to_do()

        if choice == '4':
            print("🚪 Exiting...")
            break
        
        account, access_token = prompt_herohero_credentials()

        if choice == '1':
            herohero_account_id = get_user_data(account, access_token, True)
            get_all_posts(herohero_account_id, access_token)
        elif choice == '2':
            post = input("❓ Enter the post URL you want to download (ex. https://herohero.co/{user}/post/{postID}): ")
            get_post(post, access_token)
        elif choice == '3':
            get_user_data(account, access_token, False)

if __name__ == "__main__":
    main()
