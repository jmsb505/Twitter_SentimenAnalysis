import textblob as tb
import tweepy as tp
import os

import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
api_key= os.environ.get('Twitter_API_Key')
api_key_secret= os.environ.get('Twitter_API_S_Key')
access_token = os.environ.get('Twitter_API_A-Token')
secret_access_token=os.environ.get('Twitter_API_S-A-Token')

auth_handler = tp.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,secret_access_token)

api= tp.API(auth_handler)

search_term ="Tesla"
tweet_amount= 1000
polarity=0.00000
positive=0
negative=0
neutral=0
sid_obj=SentimentIntensityAnalyzer()
tweets = tp.Cursor(api.search_tweets, q = search_term, lang = 'en',tweet_mode='extended').items(tweet_amount)
for tweet in tweets:
   final_text = tweet.full_text.replace("RT","")
   if final_text.startswith(' @'):
       position = final_text.index(':')
       final_text=final_text[position+2:]
   if final_text.startswith('@'):
       position = final_text.index(' ')
       final_text=final_text[position+2:]
   sentiment_dic=sid_obj.polarity_scores(final_text)
   positive+=sentiment_dic['pos']
   negative+=sentiment_dic['neg']
   neutral+=sentiment_dic['neu']
   polarity+=sentiment_dic['compound']
   print(final_text)
   print(sentiment_dic)


if polarity/1000>=0.05:
    print('Positive')
elif polarity/1000<=-0.05:
    print('Negative')
else:
    print('Neutral')


print(positive," ",negative," ",neutral)







