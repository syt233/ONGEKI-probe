# %%
import requests
import json
import sys
import pandas as pd
url = "https://reiwa.f5.si/ongeki_const_all.json"
response = requests.get(url)
data = json.loads(response.text.encode('utf8')[3:].decode('utf8'))


# %%
music_id=[]
music_name=[]
music_artist=[]
music_difficulty=[]
for item in data:
    music_id.append(item["music_id"])
    music_name.append(item["title"])
    music_artist.append(item["artist"])
    if item["only_lunatic"]==True:
        music_difficulty.append([0,0,0,0,item["lunatic"]["const"]])
    else:
        music_difficulty.append([item["basic"]["const"],item["advanced"]["const"],item["expert"]["const"],item["master"]["const"],item["lunatic"]["const"]])


# export
df = pd.DataFrame({"music_id":music_id,"music_name":music_name,"music_artist":music_artist,"music_difficulty":music_difficulty})
df.to_csv("ongeki_music.csv",index=False)


