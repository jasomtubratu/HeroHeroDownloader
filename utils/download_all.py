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

    for post in all_posts:
        attributes = post.get("attributes", {})
        text = attributes.get("text", "")
        video_asset = next((asset for asset in attributes.get("assets", []) if asset.get("gjirafa")), None)
        if video_asset:
            video_stream_url = video_asset["gjirafa"]["videoStreamUrl"]
            title = text.split("\n", 1)[0].strip()
            file_name = f"{title}-{datetime.datetime.now().timestamp}.mp4"
            try:
                print ("Downloading the video: ", video_stream_url, "in: ", os.path.join(videos_dir, file_name), datetime.datetime.now())
                subprocess.run(["ffmpeg", "-i", video_stream_url, "-c", "copy", "-bsf:a", "aac_adtstoasc", os.path.join(videos_dir, file_name)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                print(f"Video '{title}' has been successfully downloaded!", datetime.datetime.now())
            except Exception as e:
                print(f"Error downloading video '{title}':", e, datetime.datetime.now())

        post_info = {
            "attributes": attributes
        }
        with open(os.path.join(account_dir, f"post_{post['id']}.json"), "w") as post_file:
            json.dump(post_info, post_file, indent=4)
