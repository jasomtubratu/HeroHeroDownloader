import os
import subprocess
import requests
import json
import datetime
from utils.utils import construct_headers, create_directory, sanitize_filename
import sys
import re
import os


def download_video(video_url, file_name, download_dir):
    file_path = os.path.join(download_dir, file_name)
    try:
        print(f"⬇️ Downloading video: {video_url} | {datetime.datetime.now()}")
        subprocess.run(
            ["ffmpeg", "-i", video_url, "-c", "copy", "-bsf:a", "aac_adtstoasc", file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        print(f"✅ Video '{file_name}' has been successfully downloaded! |", datetime.datetime.now())
    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading video '{file_name}': {e}", datetime.datetime.now())

def download_image(image_url, file_name, download_dir):
    sanitized_file_name = sanitize_filename(file_name)
    file_path = os.path.join(download_dir, sanitized_file_name)
    
    try:
        print(f"⬇️ Downloading image: {image_url} | {datetime.datetime.now()}")
        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()
        
        with open(file_path, 'wb') as img_file:
            for chunk in image_response.iter_content(chunk_size=8192):
                img_file.write(chunk)
                
        print(f"✅ Image '{sanitized_file_name}' has been successfully downloaded! |", datetime.datetime.now())
    except requests.RequestException as e:
        print(f"❌ Error downloading image '{sanitized_file_name}': {e}", datetime.datetime.now())
    except OSError as e:
        print(f"❌ OS error: {e} | Filename: '{sanitized_file_name}'", datetime.datetime.now())

def save_post_info(post, download_dir):
    post_info = {"attributes": post.get("attributes", {})}
    with open(os.path.join(download_dir, f"post_{post['id']}.json"), "w") as post_file:
        json.dump(post_info, post_file, indent=4)

def get_all_posts(account, cookies):
    url = "https://svc-prod.herohero.co/api/v2/posts"
    page_index = 0
    all_posts = []

    while True:
        params = {
            "userId": account,
            "pageIndex": page_index,
            "include": "user,categories"
        }
        headers = construct_headers(cookies)
        response = requests.get(url, params=params, headers=headers)
        json_response = response.json()

        posts = json_response.get("posts", [])
        if not posts:
            break
        all_posts.extend(posts)

        if not json_response.get("meta", {}).get("hasNext", False):
            break
        page_index += 1

    account_dir = os.path.join(os.getcwd(), account)
    videos_dir = os.path.join(account_dir, 'videos')
    images_dir = os.path.join(account_dir, 'images')
    create_directory(videos_dir)
    create_directory(images_dir)

    for post in all_posts:
        attributes = post.get("attributes", {})
        title = sanitize_filename(attributes.get("text", "").split("\n", 1)[0].strip())

        video_asset = next((asset for asset in attributes.get("assets", []) if asset.get("gjirafa")), None)
        if video_asset:
            video_stream_url = video_asset["gjirafa"].get("videoStreamUrl")
            if video_stream_url:
                file_name = f"{title}-{datetime.datetime.now().timestamp()}.mp4"
                download_video(video_stream_url, file_name, videos_dir)
            else:
                print(f"❌ No video stream URL found for video asset in post '{post['id']}'")

        for asset in attributes.get("assets", []):
            image = asset.get("image")
            if image:
                image_url = image["url"]
                image_extension = os.path.splitext(image_url)[-1]
                image_file_name = f"{title}_{datetime.datetime.now().timestamp()}{image_extension}"
                download_image(image_url, image_file_name, images_dir)

        save_post_info(post, account_dir)
    print(f"✅ All posts have been successfully downloaded! | {datetime.datetime.now()}")
    sys.exit(1)