import os
import requests
import json
import datetime
from utils.utils import construct_headers


def fetch_herohero_user(account, access_token):
    url = f"https://herohero.co/services/user/v2/users?path={account}"
    headers = construct_headers(access_token)
    response = requests.get(url, headers=headers)
    json_response = response.json()
    user_id = json_response["users"][0]["id"]

    json_response.pop("meta", None)

    formatted_json = json.dumps(json_response, indent=4)

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    file_name = f"attributes-{account}-{current_datetime}.json"

    if not os.path.exists(user_id):
        os.makedirs(user_id)
    
    attributes_dir = os.path.join(user_id, 'attributes')
    if not os.path.exists(attributes_dir):
        os.makedirs(attributes_dir)

    with open(os.path.join(attributes_dir, file_name), 'w') as f:
        f.write(formatted_json)

    image_url = json_response["users"][0]["attributes"]["image"]["id"]
    image_response = requests.get(image_url)
    image_file_name = f"user_image_{user_id}.jpeg"
    with open(os.path.join(attributes_dir, image_file_name), 'wb') as img_file:
        img_file.write(image_response.content)

    return user_id

def prompt_herohero_credentials():
    herohero_account = input("Enter the user you want to download (you have to be subcribed): ")
    access_token = input("Enter your accessToken to your HeroHero account: ")
    return herohero_account, access_token
