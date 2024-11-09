# %%
import requests
import json
import sys
import pandas as pd
home_url = "https://u.otogame.net/api/game/ongeki/playlog"
with open("Authorization.txt") as f:
    Authorization = f.read().strip()

headers = {
    "Authorization": Authorization,
    # "Cookie": Cookie,
}


# %%
page = 1
music_name = []
music_artist = []
tech_score = []
level = []
while True:
    url = home_url + "?page=" + str(page)
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
        print("Error: token is invalid")
        sys.exit()
    data = json.loads(req.text)
    data = data["data"]
    if data["data"] == []:
        print("Finish")
        break
    data = data["data"]
    for item in data:
        music = item["music"]
        music_name.append( music["name"])
        music_artist.append( music["artist"])
        tech_score.append( item["tech_score"])
        level.append( item["level"]) #basic 0, advanced 1, expert 2, master 3, lunatic 10
    page += 1

# export
df = pd.DataFrame({
    "music_name": music_name,
    "music_artist": music_artist,
    "tech_score": tech_score,
    "level": level,
})
df.to_csv("ongeki.csv", index=False)


