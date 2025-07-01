import requests
import time
import functools
import yt_dlp
functools.lru_cache(maxsize=None)
def downloadTestImage():
    print("Requesting url...")
    time.sleep(1)
    response = requests.get("https://abdielkengne.vercel.app/logo.png")
    print("URL fetched.")
    if response.ok:
        time.sleep(1)
        print("Response Status : OK")
        with open("test.png","wb") as f:
            print("Writing image file")
            f.write(response.content)
            time.sleep(2)
            print("File downloaded successfully!")
    else:
        print(f"Error: Bad status code ({response.status_code})")

def downloadVideo(url:str,filename:str):
    

    givenUrl = url # Replace with actual Xvideos URL

    ydl_opts = {
        'outtmpl': f'{filename}.%(ext)s',  # Save file as downloaded_video.mp4 (or whatever format)
        'format': 'bestvideo+bestaudio/best',  # Download best video + best audio or best combined
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([givenUrl])
