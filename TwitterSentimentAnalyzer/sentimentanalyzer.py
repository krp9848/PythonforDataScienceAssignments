#Import the dependencies
import tweepy
from textblob import TextBlob

#Authentication Using tweepy
# consumer_key = consumer_key_here
# consumer_secret = consumer_secret_here
# access_token = access_token_here
# access_token_secret = access_token_secret_here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("marcelo")
# public_tweets = api.home_timeline()

for tweet in public_tweets:
	print(tweet.text)

	analysis = TextBlob(tweet.text)
	print(f"Analysis = {analysis.sentiment.polarity}")

	

