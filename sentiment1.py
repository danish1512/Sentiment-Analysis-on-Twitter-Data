# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:21:07 2020

@author: ACER
"""

import textblob
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return float(part)/float(whole)*100

consumerKey="9pA9jxeA2lFUCkM1TagojrMqj"
consumerSecret="PGwZg9UkzgOOzrK3RahV9GrvVXOS9LRxsVrw1TUOcAk5SsM5mq"
accessToken="821557925034467328-DWEMbfZleVUJxwW8ZqngWJf2epK0txy"
accessTokenSecret="nPcH4Yv5361gtjjmlDPzcGesBgO9dDVsbkX1JpKJwfCA9"

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("please Enter hashtag or keyword to analyzie : ")
noOfSearchTerm=int(input("Enter how many tweets to analyize : "))

tweets=tweepy.Cursor(api.search,q=searchTerm ,lang="English").items(noOfSearchTerm)

positive=0
negative=0  
neutral=0
polarity=0


for tweet in tweets:   
   # print(tweet.text)
    analysis =  TextBlob(tweet.text)
    if (analysis.sentiment.polarity == 0):
         neutral +=1
    elif(analysis.sentiment.polarity < 0.00):
             negative +=1
    else: positive +=1

positive = percentage(positive, noOfSearchTerm)
negative= percentage(negative, noOfSearchTerm) 
neutral = percentage(neutral, noOfSearchTerm)    

positive = format(positive, '2f')
negative = format(negative, '2f')
neutral = format(neutral, '2f')

print("How people are reacting on " + searchTerm + "by analyzing " + str(noOfSearchTerm) + "tweets.")
if (polarity == 0):
    print("Neutral")
elif (polarity < 0):
    print("Negatve")
elif(polarity > 0):
    print("positive")

labels = ['positive['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]' , 'Negative['+str(negative) +'%]' ]
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title("sentiment analysis of twitter data")
plt.axis('equal')
plt.tight_layout()
plt.show()     