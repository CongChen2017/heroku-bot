# Dependencies
import matplotlib
matplotlib.use('Agg')
import tweepy
# import numpy as np
# import pandas as pd
# from datetime import datetime
import matplotlib.pyplot as plt
# import tkinter
# from matplotlib import style
# style.use('ggplot')
import os

# # Import and Initialize Sentiment Analyzer
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
# consumer_key = os.getenv("consumer_key")
# consumer_secret = os.getenv("consumer_secret")
# access_token = os.getenv("access_token")
# access_token_secret = os.getenv("access_token_secret")


# Twitter credentials
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# # Target Account
# target_user = "@SouthwestAir"

# # Counter
# counter = 1

# # Variables for holding sentiments
# sentiments = []

# # Loop through 5 pages of tweets (total 100 tweets)
# for x in range(5):

#     # Get all tweets from home feed
#     public_tweets = api.user_timeline(target_user, page=x)

#     # Loop through all tweets 
#     for tweet in public_tweets:

#         # Run Vader Analysis on each tweet
#         results = analyzer.polarity_scores(tweet["text"])
#         compound = results["compound"]
#         pos = results["pos"]
#         neu = results["neu"]
#         neg = results["neg"]
#         tweets_ago = counter
        
#         # Create a sentiments dictionary and append 
#         # it to a list of dictionaries called `sentiments`
#         sentiment = {
#             "Compound": compound,
#             "Tweets ago": tweets_ago
#         }
#         sentiments.append(sentiment)
        
#         # Add to counter 
#         counter = counter + 1

# # Convert sentiments to DataFrame
# sentiments_pd = pd.DataFrame.from_dict(sentiments)

# # Create plot
# pic = sentiments_pd.plot.line("Tweets ago", "Compound", marker="o", legend=False)

# # # Incorporate the other graph properties
# now = datetime.now()
# now = now.strftime("%Y-%m-%d %H:%M")
# plt.title("Sentiment Analysis of Tweets ({}) for {}".format(now, target_user))
# plt.ylabel("Tweet Polarity")
# plt.xlabel("Tweets Ago")
# plt.savefig("testfig.png")

# x_axis = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x_axis,y, "ro--")
# plt.savefig("testfig.png")

# api.update_with_media("testfig.png", "test uploading pic file from Heroku.")