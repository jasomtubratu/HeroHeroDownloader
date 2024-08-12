import os
import requests
import json
import datetime
from utils.utils import construct_headers


def get_user_data(account, access_token, download_all=False):
    print(f"📦 Downloading user data for {account}...")
    url = f"https://svc-prod.herohero.co/api/v2/users?path={account}"
    headers = construct_headers(access_token)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)
        return False

    if not response.content.strip():
        print("Error: Received empty response")
        return False

    try:
        json_response = response.json()
    except json.decoder.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON response - {e}")
        print(response.text)
        return False

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

    if download_all:
        return user_id
    else:
        print("🚪 Exiting...")
        return True
