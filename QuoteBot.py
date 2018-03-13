# Dependencies
import tweepy
import time
import os


# Twitter API Keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    
# Create quotes to tweet
quote_list = [
    "Don't cry because it's over, smile because it happened. -- Dr. Seuss",
    "Be yourself; everyone else is already taken. -- Oscar Wilde" ,
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. -- Albert Einstein",
    "A room without books is like a body without a soul. -- Marcus Tullius Cicero"    
]


# Create function for tweeting
def QuoteItUp(quote):

    # Tweet the next quote
    api.update_status(quote)
    # Print success message
    print("Tweet out successfully")


# Create a loop that tweets one quote per minute until
# all of the quotes have been tweeted
for quote in quote_list:
    
    QuoteItUp(quote)
    time.sleep(30)

