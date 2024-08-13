import os
import requests
import json
import datetime
from utils.utils import construct_headers

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_json_to_file(data, directory, file_name):
    with open(os.path.join(directory, file_name), 'w') as f:
        json.dump(data, f, indent=4)

def save_image_to_file(image_url, directory, file_name):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(directory, file_name), 'wb') as img_file:
            img_file.write(response.content)
    else:
        print(f"❌ Error: Failed to download image, status code {response.status_code}")

def get_user_data(account, access_token, download_all):
    print(f"📦 Downloading user data for {account}...")
    
    if len(account.split()) == 1:
        if not account.startswith("https://herohero.co/"):
            print("❌ Error: Invalid account format")
            return False
        account = account.replace("https://herohero.co/", "")

    url = f"https://svc-prod.herohero.co/api/v2/users?path={account}"
    headers = construct_headers(access_token)
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Error: Received status code {response.status_code}")
        print(response.text)
        return False
    
    if not response.content.strip():
        print("❌ Error: Received empty response")
        return False

    try:
        json_response = response.json()
    except json.JSONDecodeError as e:
        print(f"❌ Error: Failed to decode JSON response - {e}")
        print(response.text)
        return False

    user_id = json_response["users"][0]["id"]
    json_response.pop("meta", None)

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"attributes-{account}-{current_datetime}.json"
    
    user_dir = os.path.join(user_id, 'attributes')
    create_directory(user_dir)

    save_json_to_file(json_response, user_dir, file_name)
    
    image_url = json_response["users"][0]["attributes"]["image"]["id"]
    image_file_name = f"user_image_{user_id}.jpeg"
    save_image_to_file(image_url, user_dir, image_file_name)

    if download_all:
        return str(user_id)
    else:
        print("🚪 Exiting...")
        return True
