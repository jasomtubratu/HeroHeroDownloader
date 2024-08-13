import json
import os
import requests
from utils.download_all import create_directory, save_post_info
from utils.utils import construct_headers
import re


def get_post(post_id, access_token):
    url_pattern = r"https://herohero.co/\w+/post/\w+"
    if not re.match(url_pattern, post_id):
        print("❌ Error: Invalid post_id URL")
        return False

    formatted_post_id = re.search(r"https://herohero.co/\w+/post/(\w+)", post_id).group(1)
    url = f"https://svc-prod.herohero.co/api/v2/posts?parentId={formatted_post_id}"
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

    post_dir = os.path.join(json_response["attributes"]["relationships"]["user"]["id"], "posts")
    create_directory(post_dir)
    
    save_post_info(json_response, post_dir)
    
    return True