import tweepy
import csv
from dateutil.parser import parse
import pytz
import datetime
import os

tz = pytz.timezone('America/Sao_Paulo')
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

max_id_anterior = []

nomes = ["@infoMoney","@folha_mercado","@EstadaoEconomia",\
        "@uoleconomia","@valoreconomico","@OGlobo_Economia",\
        "@AgoraNaEconomia","@EconomiaGV","@B3_Oficial",\
        "@Dinheirama","@iGEconomia","@br_economico","@BloombergBrasil"]

today = str(datetime.date.today().strftime("%Y-%m-%d"))
print(today)
max_id_anterior = []

file_exists = os.path.isfile("Twitter-"+today+".csv")
if not file_exists:
    for i in range(0,len(nomes)):
      for tweet in tweepy.Cursor(api.search,q="from:"+nomes[i]+" since:"+today+"", tweet_mode='extended').items():
          user = tweet.user.screen_name
          print(user)
          twee = str(tweet.full_text)
          twee = twee.replace('"', "'")
          print(twee)
          like = tweet.favorite_count
          retweet = tweet.retweet_count
          seguidores = tweet.user.followers_count
          x = tweet.created_at
          data = parse(str(x) + ' +0000')
          data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
          dataFinal = data
          print(dataFinal)
          id = tweet.id
          i += 1

          file_exists = os.path.isfile("Twitter-"+today+".csv")
          with open("Twitter-"+today+".csv", 'a', newline='') as saida:
              headers = ['User', 'Data', 'Seguidores', 'Retweet', 'Likes', 'Id', 'Tweet']
              writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
              if not file_exists:
                  writer.writeheader()
              writer.writerow({'User': user, 'Data': dataFinal, 'Seguidores': seguidores, 'Retweet': retweet, 'Id': id, 'Likes': like, 'Tweet': twee})

    #PEGA TODOS OS ULTIMOS IDS SE O ARQUIVO NÂO EXISTIR
    for z in nomes:
        for tweet in api.user_timeline(id=z, count=1):
            user = tweet.user.screen_name
            x = tweet.created_at
            data = parse(str(x) + ' +0000')
            data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
            dataFinal = data
            id = tweet.id
            with open("max_id.csv", 'a', newline='') as saida:
                escrever = csv.writer(saida, delimiter=";", quoting=csv.QUOTE_MINIMAL)
                escrever.writerow([user, id, dataFinal])


else:
    with open('max_id.csv', 'r') as csvfile:
        csv_m = csv.reader(csvfile, delimiter=';')

        for row in csv_m:
            x = row[1]
            max_id_anterior.append(x)
    i = 0

    for i in range(0,len(max_id_anterior)):
        for tweet in tweepy.Cursor(api.search,q="from:"+nomes[i], tweet_mode='extended', since_id=max_id_anterior[i]).items():
            user =  tweet.user.screen_name
            print(user)
            twee = str(tweet.full_text)
            twee = twee.replace('"',"'")
            print(twee)
            like = tweet.favorite_count
            retweet = tweet.retweet_count
            seguidores = tweet.user.followers_count
            x = tweet.created_at
            data = parse(str(x) + ' +0000')
            data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
            dataFinal = data
            print(dataFinal)
            id = tweet.id
            i+=1

            file_exists = os.path.isfile("Twitter-"+today+".csv")
            with open("Twitter-"+today+".csv", 'a', newline='') as saida:
                headers = ['User', 'Data', 'Seguidores', 'Retweet', 'Likes', 'Id', 'Tweet']
                writer = csv.DictWriter(saida, delimiter=';', lineterminator='\n', fieldnames=headers)
                if not file_exists:
                    writer.writeheader()
                writer.writerow({'User': user, 'Data': dataFinal, 'Seguidores': seguidores, 'Retweet': retweet, 'Id': id, 'Likes': like, 'Tweet': twee})

    os.remove("max_id.csv")
    for z in nomes:
        for tweet in api.user_timeline(id=z, count=1):
            user = tweet.user.screen_name
            x = tweet.created_at
            data = parse(str(x) + ' +0000')
            data = data.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
            dataFinal = data
            id = tweet.id
            with open("max_id.csv", 'a', newline='') as saida:
                escrever = csv.writer(saida, delimiter=";", quoting=csv.QUOTE_MINIMAL)
                escrever.writerow([user, id, dataFinal])

