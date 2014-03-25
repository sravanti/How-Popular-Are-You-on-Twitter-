import tweepy

__author__ = 'sravantitekumalla'

import tweepy
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = "C5wXvaYmR6yslEv1tNtZlA"
consumer_secret = "XBxl7JehOueWu0C1ZMYdc39TbYOd2SuV4KMreWQuag"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = "50367900-ahdMGvMT2hCXfyp9gyahlEZzIGDU4QqoxbBLGWIDv"
access_token_secret = "OMee1Kt2WCDhJqjpljdSp7T1O9iYyQuOjjCHgupwQVsYf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)