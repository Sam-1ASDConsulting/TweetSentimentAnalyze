#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 11:41:16 2018
@author: loudsunday
"""
# use Twitter (tweepy), textblob for NLP, csv for output csv file 
import tweepy
from textblob import TextBlob
import csv

# Connect to your Twitter App you setup on https://developer.twitter.com
consumer_key = 'TiQDxYoWZn51dlwYfrXPCxBqF'
consumer_secret = 'ZSUBv8MOXys83Jopky0hjpdAf7BfqPlCYnV0nLRLoh44hqk1XU'

access_token = '2508050690-wsi2RV8x44alpywunE3quaVnjJK77pFZjhNxSJS'
access_token_secret = 'gZpprbdyDgRj6g0KTmpBCg5QMu7x8Bh5nxK9fg03Q9Wvo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get tweets of your subject
subject = 'Trump'
public_tweets = api.search(subject)

# Setup a CSV output file to output to
csv_file = open('TweetSentOut.csv', 'w')
output = csv.writer(csv_file)

# NLP analyze tweets one at a time and output to CSV file
for tweet in public_tweets:
	text = tweet.text.encode('utf-8').strip()
	analysis = TextBlob(tweet.text)
	polarity = analysis.sentiment.polarity
	if polarity > 0.1 :
		output.writerow([text, polarity, " :)  POSITIVE"])
	else :
		output.writerow([text, polarity, " :(  NEGATIVE"])

print("See tweets and sentiment in the TweetSentOut.csv file")