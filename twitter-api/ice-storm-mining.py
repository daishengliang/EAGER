# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:30:06 2017

@author: ShengliangDai
"""

import pandas as pd
import tweepy
from time import sleep

api_key = "tDTMJtC7sAz39hEj4rX5vb0sJ" # <---- Add your API Key
api_secret = "5D9lXFpNr5Mpr8D4SQCak4pDH4NpzvyhmxXT4h5lxRYGqtfDHg" # <---- Add your API Secret
access_token = "1196013206-P6T1RgOl9Dwq70RUNXrczzjSxsuQtrlKimQBGmn" # <---- Add your access token
access_token_secret = "hBq8zik4WntPTB2hZEfSpVZNA0F7zAtj3mKjvb4GHyklz" # <---- Add your access token secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = []
query = ["freezing rain"]
num_search = 36
for n in range(num_search):
    print("The {} times search".format(n))
    for tweet in tweepy.Cursor(api.search, q=query).items(500):
        results.append(tweet)
    if n == num_search - 1:
        break
    print("Sleep 20 minutes...{} times left".format(num_search - 1 - n))
    sleep(1200)

def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])

    # Processing Tweet Data

    data_set["text"] = [tweet.text for tweet in results]
    media = []
    expanded_url = []
    for tweet in results:
        if "media" in tweet.entities:
            for image in tweet.entities["media"]:
                media.append(image["media_url"])
                if 'video' in image["expanded_url"]:
                    expanded_url.append(image["expanded_url"]) 
                else:
                    expanded_url.append(None)
        else:
            media.append(None)
            expanded_url.append(None)
    data_set["media_url"] = media
    data_set["video_url"] = expanded_url
    
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results]
    data_set["source"] = [tweet.source for tweet in results]

    # Processing User Data
    data_set["user_id"] = [tweet.author.id for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results]
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]
    data_set["user_coordinates"] = [tweet.coordinates for tweet in results]

    return data_set
data_set = process_results(results)
data_set.to_csv("freezing rain-jan19.csv")
print("Finish!")