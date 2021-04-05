import csv
import itertools
import tweepy
import os
from dotenv import load_dotenv

# Load environement variables containing Twitter API keys
load_dotenv()

# Authorize Tweepy API
auth = tweepy.AppAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET_KEY'))
api = tweepy.API(auth)

# Generate the search query based on all combinations of these phrases
names = ['Adia Barnes', "Arizona coach"]
modifiers = ['mother', 'breastfeeding', 'pumping']
query = ' OR '.join(map(lambda x: x[0] + ' ' + x[1], itertools.product(names, modifiers)))

# Open a file for writing the tweets to
with open('tweets.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['text', 'id', 'created', 'is_retweet', 'favorites', 'retweets'])

    for tweet in tweepy.Cursor(api.search, q=query, lang='en-us').items():
        writer.writerow([tweet.text.encode(encoding='UTF-8',errors='strict'), tweet.id, tweet.created_at, tweet.text.startswith('RT @'), tweet.favorite_count, tweet.retweet_count])

