import tweepy
import json
from random import * 

class Twitter(object):
    def __init__(self):
        with open('twitter/twitter_auth.json') as file:
            secrets = json.load(file)
        auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
        auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

        self.twitter = tweepy.API(auth)

    def tweet(self, message):
        self.twitter.update_status(message)

def main():
    twitter = Twitter()
    twitter.tweet("Testing Testing 1 2 3")

if __name__ == '__main__':
    main()
