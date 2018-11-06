import tweepy
import datetime
import pytz
from dateutil.parser import parse
import csv
import os


tz = pytz.timezone('America/Sao_Paulo')

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

y=0
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

fuso = 3

username = ""
startDate = datetime.datetime(2018,10,1,0+3)
endDate = datetime.datetime(2018,11,1,0+3)

tweets = []
tmpTweets = tweepy.Cursor(api.user_timeline, id='').items()
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)


for i in tweets:
    y+=1
    tweet = i.text
    data = parse(str(i.created_at)+' +0000')
    data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
    dataFinal = data
    print(dataFinal)

    # file_exists = os.path.isfile("Twitter.csv")
    # with open("Twitter.csv", 'a', newline='') as saida:
    #     headers = ['Data', 'User', 'Tweet']
    #     writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
    #     if not file_exists:
    #         writer.writeheader()
    #     writer.writerow({'Data': dataFinal, 'User': username, 'Tweet': tweet})








print(y)
