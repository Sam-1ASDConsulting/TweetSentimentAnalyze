#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 11:41:16 2018 @author loudsunday
Updated on Tue Jul 15 14:10:00 2019 @author 1asdconsulting
"""
# Imports for Twitter, CSV files, dataframe management, diagrams, series
import tweepy
from textblob import TextBlob
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Runtime Configuration variables
LOCAL_FILE_PATH = './TweetSentOut.csv'
# Add your Twitter dev credentials for your https://developer.twitter.com account
consumer_key = 'add your twitter dev consumer key here'
consumer_secret = 'add your twitter dev consumer secret here'
access_token = 'add your twitter dev access token here'
access_token_secret = 'add your twitter dev access token secret here'


# Connect to your Twitter dev account at https://developer.twitter.com
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Ask for a subject/topic and search for relevent tweets
subject = input("Hi! What subject or topic of tweets do you want to find and analyze for sentiment? ===>  ")  
print(">>>>> OK. Looking for tweets about ", subject, "..........") 
public_tweets = api.search(q=subject, count=100) # max at retrieving 50 tweets

# Setup file to write with a CSV format the tweets returned from search 
csv_file = open(LOCAL_FILE_PATH, 'w')
output = csv.writer(csv_file)

# NLP analyze each tweet for sentiment write out to the CSV file
for tweet in public_tweets:
    text = tweet.text.encode('utf-8').strip()
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.0 :
        output.writerow(["POSITIVE", polarity, text])
    elif polarity < 0.0 :
        output.writerow(["NEGATIVE", polarity, text])
    else :
        output.writerow(["NEUTRAL", polarity, text])

# Close file after storing all tweets
csv_file.close()
        
# Collect tweets in csv output file, reasd it into a dataframe and show some analysis
print("=============================================================================")
print("Tweets and sentiment output to ", LOCAL_FILE_PATH)
print("=============================================================================")

tweet_df = pd.read_csv(LOCAL_FILE_PATH, header=None, names=['Sentiment', 'Polarity','Tweet' ])
print("==== Tweet Sentiment Rating and text snippets ===")
print("=================================================")
print(tweet_df)

print("=================================================")
print("=========== Full text Tweet output ==============")
print("=================================================")
pd.set_option('display.max_colwidth', -1)
print(tweet_df[['Sentiment','Tweet']])

# Create histogram of total tweets classified for each sentiment
total_tweets = len(tweet_df)
count = tweet_df['Sentiment'].value_counts()
print(count)

x = np.arange(3)
plt.bar(x, height=count,color=['gray', 'green', 'red'])
plt.title('Sentiment Chart for '+str(total_tweets)+' latest '+subject+' Tweets')
plt.xticks(x, ['Neutral','Positive','Negative'])
plt.xlabel('Sentiment')
plt.ylabel('Counts');
plt.show()