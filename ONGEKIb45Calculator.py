# %%
import requests
import json
import sys
import pandas as pd
import numpy as np

# Get data from csv file
play_data = pd.read_csv('ongeki.csv')
level_data = pd.read_csv('ongeki_music.csv')

def score2rating(level, tech_score):
    # 
    if tech_score>=1007500:
        return level+2.0
    elif tech_score>=1000000:
        return level+1.5+(tech_score-1000000)/15000.0
    elif tech_score>=970000:
        return level+(tech_score-970000)/20000.0
    else:
        return max(0,level-(970000-tech_score)/17500.0)

def score2rank(tech_score):
    if tech_score>=1007500:
        return 'SSS+'
    elif tech_score>=1000000:
        return 'SSS'
    elif tech_score>=990000:
        return 'SS'
    elif tech_score>=970000:
        return 'S'
    elif tech_score>=940000:
        return 'AAA'
    elif tech_score>=900000:
        return 'AA'
    else:
        return '<AA'

# %%
# process play log
new_version =[]
old_version =[]
level_name=['basic','advanced','expert','master','lunatic']
for i in range(play_data.shape[0]):
    entry = play_data.iloc[i]
    # find the corresponding music in level_data
    music = level_data.loc[level_data['music_name'] == entry['music_name']]
    if music.shape[0] == 0:
        print('Music not found:', entry['music_name'])
        continue
    music = music.iloc[0]
    level = int(entry['level'])# 0 basic, 1 advanced, 2 expert, 3 master, 10 lunatic
    if level==10:
        level = 4
    diff_list = eval(music['music_difficulty'])
    try:
        diff = diff_list[level]
    except Exception as e:
        print(diff_list,level,e)
    rating = score2rating(diff, entry['tech_score']).__round__(2)
    rank = score2rank(entry['tech_score'])
    # divide entry into two parts, music_id>=956 into new version, music_id<956 into old version
   
    if music['music_id']>=956:
        new_version.append([entry['music_name'], level_name[level], entry['tech_score'],rank,diff,rating])
    else:
        old_version.append([entry['music_name'], level_name[level], entry['tech_score'],rank,diff,rating])
# calculate 30 highest rating for old version, 15 highest rating for new version
# if duplicate, keep the highest rating
old_version = pd.DataFrame(old_version, columns=['music_name','level','tech_score','rank','diff','rating'])
new_version = pd.DataFrame(new_version, columns=['music_name','level','tech_score','rank','diff','rating'])
old_version = old_version.sort_values(by='rating',ascending=False)
new_version = new_version.sort_values(by='rating',ascending=False)
old_version = old_version.drop_duplicates(subset=['music_name','level'],keep='first')
new_version = new_version.drop_duplicates(subset=['music_name','level'],keep='first')
old_version.to_csv('old_version_full.csv',index=False)
new_version.to_csv('new_version_full.csv',index=False)
old_version = old_version.head(30)
new_version = new_version.head(15)
# calculate average rating for old version, new version and total
old_version_avg = old_version['rating'].mean().round(2)
new_version_avg = new_version['rating'].mean().round(2)
total_avg = (old_version['rating'].sum()+new_version['rating'].sum())/(old_version.shape[0]+new_version.shape[0])
total_avg = total_avg.round(2)
# export list and average rating into csv file
old_version.to_csv('best 30.csv',index=False)
new_version.to_csv('new 15.csv',index=False)
with open('rating.csv','w') as f:
    f.write('b30,n15,b45\n')
    f.write(str(old_version_avg)+','+str(new_version_avg)+','+str(total_avg)+'\n')





