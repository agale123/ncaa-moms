import json
import csv
import pandas as pd
from google.cloud import language_v1

# Read in data
data = pd.read_csv('tweets.csv')

def analyze_text(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    return client.analyze_sentiment(request={'document': document}).document_sentiment


with open('sentiment.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['id', 'score', 'magnitude'])

    # Read in all non-retweet text to avoid duplicates
    for index, line in data[data['is_retweet']==False].iterrows():
        try:
            sentiment = analyze_text(line['text'])
            writer.writerow([line['id'], sentiment.score, sentiment.magnitude])
            
        except:
            continue
