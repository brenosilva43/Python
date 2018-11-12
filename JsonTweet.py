import tweepy
import json
import os
import csv
from dateutil.parser import parse

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


nomes = ["@infoMoney","@folha_mercado","@EstadaoEconomia",\
        "@uoleconomia","@valoreconomico","@OGlobo_Economia",\
        "@AgoraNaEconomia","@EconomiaGV","@B3_Oficial",\
        "@Dinheirama","@iGEconomia","@br_economico","@BloombergBrasil"]


for tweet in tweepy.Cursor(api.user_timeline,id="@B3_Oficial", tweet_mode='extended').items():
    json1 = tweet._json
    print(json1)
    json3 = json.dumps(json1, ensure_ascii=False)
    json3 = json3.replace("\\\"","'")
    f = open("Twitter-Json.json", 'a')
    f.write(json3+"\n")



