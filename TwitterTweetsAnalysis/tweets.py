#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import csv
 
f = open ("tweets.csv", "w", encoding="utf-8") 
wr = csv.writer(f)
wr.writerow(['tweet_id', 'username','hashtags','timestamp','language', 'text'])

# Add the keywords you want to track. They can be cashtags, hashtags, or words.
keywords = ['#DilliChaleModiKeSaath','#दिल्ली_में_योगी_की_दहाड़']

# Optional - Only grab tweets of specific language
language = ['en','hi']

# You need to replace these with your own values that you get after creating an app on Twitter's developer portal.

consumer_key= 'ZKavl1xdcgzbGfb2'
consumer_secret= 'Cg7psk5vUA'
access_token= '62252281U5qNzTHeWhY9SOh2'
access_token_secret= 'M6mlAcrjwE7023GoSw'

# The below code will get Tweets from the stream and store only the important fields to your database
class StdOutListener(StreamListener):

    def on_data(self, data):

        # Load the Tweet into the variable "t"
        t = json.loads(data)
        tweet_id = t['id_str']  # The Tweet ID from Twitter in string format
        username = t['user']['screen_name']  # The username of the Tweet author
        if hasattr(t,'extended_tweet'):
                text = t['extended_tweet']['full_text']
        elif hasattr(t, 'retweeted_status'):
                text = t['retweeted_status']['full_text']
        else:
                text = t['text']
        hashtags = t['entities']['hashtags']  # Any hashtags used in the Tweet
        dt = t['created_at']  # The timestamp of when the Tweet was created
        language = t['lang']  # The language of the Tweet
        print(tweet_id + " " + text)
        wr.writerow([tweet_id, username, hashtags, dt, language, text])

        return True

    # Prints the reason for an error to your console
    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=keywords, languages=language)
