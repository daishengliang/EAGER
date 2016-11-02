import numpy as np
import pandas as pd
import tweepy
import matplotlib.pyplot as plt
import pymongo
import ipywidgets as wgt
from IPython.display import display
from sklearn.feature_extraction.text import CountVectorizer
import re
from datetime import datetime


api_key = "tDTMJtC7sAz39hEj4rX5vb0sJ" # <---- Add your API Key
api_secret = "5D9lXFpNr5Mpr8D4SQCak4pDH4NpzvyhmxXT4h5lxRYGqtfDHg" # <---- Add your API Secret
access_token = "1196013206-P6T1RgOl9Dwq70RUNXrczzjSxsuQtrlKimQBGmn" # <---- Add your access token
access_token_secret = "hBq8zik4WntPTB2hZEfSpVZNA0F7zAtj3mKjvb4GHyklz" # <---- Add your access token secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        
    def on_error(self, status_code):
        if status_code == 420:
        #returning False in on_data disconnects the stream
            return False
        
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['trump', "hilton"])