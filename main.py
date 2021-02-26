import requests
import json
import time
headers = {"Authorization":"your-discord-token"}
data = {
    "custom_status" : {
        "text":"test"
    }
}
while True:
    try:
        data["custom_status"]["text"] = "ᕕ( ᐛ )ᕗ"
        response = requests.patch("https://discord.com/api/v8/users/@me/settings",json=data,headers=headers)
        print(response)
        time.sleep(3)
        data["custom_status"]["text"] = "ᕕ( ᐕ )ᕗ"
        response = requests.patch("https://discord.com/api/v8/users/@me/settings",json=data,headers=headers)
        print(response)
        time.sleep(3)
    except Exception as f:
        print(f)
