import os
import subprocess
import requests
import json
import datetime
from utils.utils import construct_headers

def get_all_posts(account, cookies):
    url = "https://svc-prod.herohero.co/api/v2/posts"
    pageIndex = 0
    all_posts = []

    while True:
        params = {
            "userId": account,
            "pageIndex": pageIndex,
            "include": "user,categories"
        }
        headers = construct_headers(cookies)
        response = requests.get(url, params=params, headers=headers)
        json_response = response.json()
        posts = json_response.get("posts", [])
        if not posts:
            break

        all_posts.extend(posts)

        meta = json_response.get("meta", {})
        if not meta.get("hasNext", False):
            break
        pageIndex += 1

    account_dir = os.path.join(os.getcwd(), account)
    if not os.path.exists(account_dir):
        os.makedirs(account_dir)

    videos_dir = os.path.join(account_dir, 'videos')
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)

    images_dir = os.path.join(account_dir, 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    for post in all_posts:
        attributes = post.get("attributes", {})
        text = attributes.get("text", "")
        
        video_asset = next((asset for asset in attributes.get("assets", []) if asset.get("gjirafa")), None)
        if video_asset:
            video_stream_url = video_asset["gjirafa"]["videoStreamUrl"]
            title = text.split("\n", 1)[0].strip()
            file_name = f"{title}-{datetime.datetime.now().timestamp()}.mp4"
            try:
                print("⬇️ Downloading video: ", video_stream_url, "| ",  datetime.datetime.now())
                subprocess.run(["ffmpeg", "-i", video_stream_url, "-c", "copy", "-bsf:a", "aac_adtstoasc", os.path.join(videos_dir, file_name)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                print(f"✅ Video '{title}' has been successfully downloaded!", datetime.datetime.now())
            except Exception as e:
                print(f"❌ Error downloading video '{title}':", e, datetime.datetime.now())
        
        for asset in attributes.get("assets", []):
            image = asset.get("image")
            if image:
                image_url = image["url"]
                image_extension = os.path.splitext(image_url)[-1]
                image_file_name = f"{text.split('\n', 1)[0].strip()}_{datetime.datetime.now().timestamp()}{image_extension}"
                image_path = os.path.join(images_dir, image_file_name)
                
                try:
                    print(f"⬇️ Downloading image: {image_url} | ", datetime.datetime.now())
                    image_response = requests.get(image_url)
                    with open(image_path, 'wb') as img_file:
                        img_file.write(image_response.content)
                    print(f"✅ Image '{image_file_name}' has been successfully downloaded!", datetime.datetime.now())
                except Exception as e:
                    print(f"❌ Error downloading image '{image_file_name}':", e, datetime.datetime.now())

        post_info = {
            "attributes": attributes
        }
        with open(os.path.join(account_dir, f"post_{post['id']}.json"), "w") as post_file:
            json.dump(post_info, post_file, indent=4)

