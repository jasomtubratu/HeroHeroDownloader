from utils.utils import clear_console, change_cmd_title, print_blue, check_ffmpeg_installation
from utils.http_requests import send_herohero_request
from utils.file_handling import fetch_herohero_user

def prompt_herohero_credentials():
    herohero_account = input("❓ Enter the user you want to download (from the url): ")
    access_token = input("❓ Enter your accessToken to your HeroHero account: ")
    access_token = access_token.strip('"')
    return herohero_account, access_token

def what_you_want_to_do():
    print ("❓ What do you want to do?")
    print ("[1] Download whole user´s profile")
    print ("[2] Download a specific video")
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
    print_blue("""
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
                                                                                      
    """)

    check_ffmpeg_installation()
    choice = what_you_want_to_do()

    account, access_token = prompt_herohero_credentials()
    herohero_account_id = fetch_herohero_user(account, access_token)

    if choice == '1':
        send_herohero_request(herohero_account_id, access_token)
    elif choice == '2':
        print ("❌ Not implemented yet")
    elif choice == '3':
        print ("❌ Not implemented yet")
    elif choice == '4':
        print ("Exiting...")
        exit()



    #account, access_token = prompt_herohero_credentials()
    #herohero_account_id = fetch_herohero_user(account, access_token)
    #send_herohero_request(herohero_account_id, access_token)

if __name__ == "__main__":
    main()
