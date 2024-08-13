import datetime
import json
import os
import sys
import requests
from utils.download_all import create_directory, download_image, download_video, save_post_info
from utils.utils import construct_headers, sanitize_filename
import re

def get_post(post_id, access_token):
    url_pattern = r"https://herohero.co/\w+/post/\w+"
    if not re.match(url_pattern, post_id):
        print("❌ Error: Invalid post_id URL")
        return False

    formatted_post_id = re.search(r"https://herohero.co/\w+/post/(\w+)", post_id).group(1)
    
    url = f"https://svc-prod.herohero.co/api/v2/posts/{formatted_post_id}"
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
        sys.exit(1)

    account_dir = os.path.join(json_response["relationships"]["user"]["id"])
    videos_dir = os.path.join(account_dir, 'videos')
    images_dir = os.path.join(account_dir, 'images')
    create_directory(account_dir)
    create_directory(videos_dir)
    create_directory(images_dir)

    attributes = json_response["attributes"]
    title = sanitize_filename(attributes.get("text", "").split("\n", 1)[0].strip())

    video_asset = next((asset for asset in attributes.get("assets", []) if asset.get("gjirafa")), None)
    if video_asset:
        video_stream_url = video_asset["gjirafa"]["videoStreamUrl"]
        file_name = f"{title}-{datetime.datetime.now().timestamp()}.mp4"
        download_video(video_stream_url, file_name, videos_dir)

    for asset in attributes.get("assets", []):
        image = asset.get("image")
        if image:
            image_url = image["url"]
            image_extension = os.path.splitext(image_url)[-1]
            image_file_name = f"{title}_{datetime.datetime.now().timestamp()}{image_extension}"
            download_image(image_url, image_file_name, images_dir)
    
    save_post_info(json_response, account_dir)
    
    sys.exit(1)
