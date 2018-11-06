import tweepy
import os
import csv
from dateutil.parser import parse
import pytz
import datetime

tz = pytz.timezone('America/Sao_Paulo')
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


nomes = "@infoMoney","@folha_mercado","@EstadaoEconomia",\
        "@uoleconomia","@valoreconomico","@OGlobo_Economia",\
        "@AgoraNaEconomia","@EconomiaGV","@B3_Oficial",\
        "@Dinheirama","@iGEconomia","@br_economico"

id = "folha-mercado"

#----------------------------------------------------------------------------

for tweet in tweepy.Cursor(api.user_timeline, id='@br_economico', tweet_mode='extended').items():
   user =  tweet.user.screen_name
   twee = tweet.full_text
   like = tweet.favorite_count
   retweet = tweet.retweet_count
   seguidores = tweet.user.followers_count
   x = tweet.created_at
   data = parse(str(x) + ' +0000')
   data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
   dataFinal = data
   print(dataFinal)


   file_exists = os.path.isfile("Twitter.csv")
   with open("Twitter.csv", 'a', newline='') as saida:
       headers = ['User', 'Data','Seguidores','Retweet','Likes', 'Tweet']
       writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
       if not file_exists:
           writer.writeheader()
       writer.writerow({'User': user,'Data': dataFinal,'Seguidores':seguidores,'Retweet': retweet, 'Likes':like, 'Tweet': twee})
