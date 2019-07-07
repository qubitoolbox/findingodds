#import libraries
import tweepy
from textblob import TextBlob as tb

def apiCall(word):
  '''The keys can be generated at developer.twitter.com'''
  #assign variables holding the key pair values
  lkey = {'consumer_key':"ckey_goes_here"}
  lkey1 = {'consumer_secret':"csecr_goes_here"}
  akey = {'access_token':"keyhere"}
  akey1 = {'access_token_secret':"keyhere"}
  #invoke post auth of key values.
  auth = tweepy.OAuthHandler(lkey['consumer_key'], lkey1['consumer_secret'])
  auth.set_access_token(akey['access_token'], akey1['access_token_secret'])
  api = tweepy.API(auth)
  #search for the word in twitter's API
  public_tweets = api.search(word)
