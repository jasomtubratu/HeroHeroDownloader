from utils.utils import clear_console, change_cmd_title, print_blue, check_ffmpeg_installation
from utils.http_requests import send_herohero_request
from utils.file_handling import fetch_herohero_user, prompt_herohero_credentials


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
    account, access_token = prompt_herohero_credentials()
    herohero_account_id = fetch_herohero_user(account, access_token)
    send_herohero_request(herohero_account_id, access_token)

if __name__ == "__main__":
    main()
