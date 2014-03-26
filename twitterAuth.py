from __future__ import division
from decimal import *
__author__ = 'sravantitekumalla'


import auth


# == OAuth Authentication ==
api = auth.api
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status('Hehe now I can update my status w/o twitter app...cs is so cool')
#initialize some vars
class twitterAuth:
    numTweets = 0
    numFavs = 0
    numRTs = 0
    numFollowers = 0
    numFollowing = 0
    numMentions = 0
    popsum = 0
    username = ""
    results = ""
    name = ""

    def __init__(self, name):

        self.name = name
        self.username = api.get_user(name)
        self.results = api.user_timeline(name, count=800)
        for status in self.results:
            self.numRTs += status.retweet_count
            self.numFavs += status.favorite_count
        self.numTweets += self.results.__len__()
        self.numMentions = api.search("@"+name).__len__()
        self.numFollowers = self.username.followers_count
        self.numFollowing = self.username.friends_count
        self.averageFavs = self.numFavs/self.numTweets
        self.averageRTs = self.numRTs/self.numTweets
        self.friendRatio = self.numFollowers/self.numFollowing

    def getTweets(self):
        return self.numTweets

    def getMentions(self):
        return self.numMentions

    def getFollowers(self):
        return self.numFollowers

    def getFollowing(self):
        return self.numFollowing

    def getAverageFavs(self):
        return self.averageFavs

    def getAverageRTs(self):
        return self.averageRTs

    def getFriendRatio(self):
        return self.friendRatio

    def getName(self):
        return self.name

    def popularity(self):
        self.popsum += int(Decimal(self.numMentions)) * 10
        self.popsum += int(Decimal(self.averageFavs)) * 100
        self.popsum += int(Decimal(self.friendRatio)) * 100
        return self.popsum







