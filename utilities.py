import requests
import time
import functools
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