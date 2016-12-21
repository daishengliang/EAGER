#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
This script uses Twitter RESTful API to collect the most recent tweets.

Command line: python restful.py -q "queries" -n 1000 -of "data/filename.csv"

Arguments:

    -q|--queries|str|required||User provided queries
    -n|--num_of_tweets|int|required||the number of tweets
    -of|--output_file|str|required, default: None||the output file for the tweets
"""

import numpy as np
import pandas as pd
import tweepy
import argparse
import sys

def parse_args():
    """Parse the arguments.
    Parse the command line arguments/options using the argparse module
    and return the parsed arguments (as an argparse.Namespace object,
    as returned by argparse.parse_args()).
    Returns:
        argparse.Namespace: the parsed arguments
    """

    # Parse command line options/arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--queries', required=True,
                        help='User provided queries')
                   
    parser.add_argument('-n', '--num_of_tweets', required=True, type=int)

    parser.add_argument('-of', '--output_file', required=True)


    args = parser.parse_args()

    return args



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


def main(argv=None):
    """This is the main function.
    """
    api_key = "tDTMJtC7sAz39hEj4rX5vb0sJ" # <---- Add your API Key
    api_secret = "5D9lXFpNr5Mpr8D4SQCak4pDH4NpzvyhmxXT4h5lxRYGqtfDHg" # <---- Add your API Secret
    access_token = "1196013206-P6T1RgOl9Dwq70RUNXrczzjSxsuQtrlKimQBGmn" # <---- Add your access token
    access_token_secret = "hBq8zik4WntPTB2hZEfSpVZNA0F7zAtj3mKjvb4GHyklz" # <---- Add your access token secret

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    results = []
    args = parse_args()
    query = [args.queries]
    for tweet in tweepy.Cursor(api.search, q=query).items(args.num_of_tweets):
        results.append(tweet)

    data_set = process_results(results)
    data_set.to_csv(args.output_file, index = False)
    print("Finish!")

if __name__=="__main__":
    sys.exit(main())
