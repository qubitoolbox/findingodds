#import libraries
import tweepy
from textblob import TextBlob as tb

def apiCall(word):
  '''The keys can be generated at developer.twitter.com'''
  
  lkey = {'consumer_key':"ckey_goes_here"}
  lkey1 = {'consumer_secret':"csecr_goes_here"}
  akey = {'access_token':"keyhere"}
  akey1 = {'access_token_secret':"keyhere"}

  auth = tweepy.OAuthHandler(lkey['consumer_key'], lkey1['consumer_secret'])
  auth.set_access_token(akey['access_token'], akey1['access_token_secret'])
  api = tweepy.API(auth)
  public_tweets = api.search(word)
