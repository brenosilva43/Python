import requests
import datetime
import sys
import csv
import time
import boto3
import json
#imports das bibliotecas


# Definição das variaveis de tempo, URL e o Header para simular o navegador
x=0
tempo_inicial = time.time() 
urldolar = 'https://m.investing.com/currencies/usd-brl'
date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
urleuro = 'https://m.investing.com/currencies/eur-brl'
headers = {'user-agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'}
webhook = 'https://hooks.slack.com/services/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'
slackmsg = {'text':'Acabei!!!'}

#metodo que envia mensagem pro slack
def msgSlack():
    webhook = ''
    slackmsg = {'text': 'Projeto Compilado'}
    requests.post(webhook, data=json.dumps(slackmsg))

#Metodo que manda os arquivo gravado para o S3    
def s3():
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
    )
    s3 = session.resource('s3')
    data = open('testeRequest.csv', 'rb')
    s3.Bucket('s3.datalab-fiap-2018').put_object(Key='Desafio/Breno/testeRequest.csv', Body=data)
    dat = open('log.txt', 'rb')
    s3.Bucket('s3.datalab-fiap-2018').put_object(Key='Desafio/Breno/log.txt', Body=dat)

#Medodo que faz o request da cotacao do Euro da pagina m.investing
def cotacaoEuro():
    resp = requests.get(urleuro, headers=headers)
    string = resp.text
    r1 = string.find('lastInst')
    r2 = string.find('quotesChange')
    x = string[r1:r2]
    r3 = x.find('>')
    r4 = x.find('</')
    x1 = x[r3:r4]
    x2 = x1.replace(">"," ")
    Euro = x2.strip()
    return Euro

#metodo de gravar cotação do Euro  
def gravarEuro():
    with open("testeRequest.csv", 'a', newline='') as saida:
        escrever = csv.writer(saida, delimiter =",",quoting=csv.QUOTE_MINIMAL)
        escrever.writerow(["EUR/BRL",cotacaoEuro(),date])

#Medodo que faz o request da cotacao do Dolar da pagina m.investing
def contacaoDolar():
    resp = requests.get(urldolar, headers=headers)
    string = resp.text
    r1 = string.find('lastInst')
    r2 = string.find('quotesChange')
    x = string[r1:r2]
    r3 = x.find('>')
    r4 = x.find('</')
    x1 = x[r3:r4]
    x2 = x1.replace(">", " ")
    Dolar = x2.strip()
    return Dolar

#Metodo de gravar a cotação em csv
def gravarDolar ():
    with open("testeRequest.csv", 'a', newline='') as saida:
        escrever = csv.writer(saida, delimiter =",",quoting=csv.QUOTE_MINIMAL)
        escrever.writerow(["USD/BRL",contacaoDolar(),date])

#metodo que faz o log dos arquivos        
def log():
    datefinal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file = open('log.txt', 'a', newline='')
    file.write("HORARIO DE EXECUCAO: "+date+"\n")
    if x == 1:
        file.write('ACAO: Gravando dolar'+"\n")
    elif x == 2:
        file.write('ACAO: Gravar Euro'+"\n")
    elif x == 3:
        file.write('ACAO: GRAVANDO NO S3 E MANDANDO MSG NO SLACK'+"\n")
    else:
        file.write('ACAO: Programa executado sem parametro'+"\n")
    file.write("TEMPO FINAL: " + datefinal+"\n")
    file.write("TEMPO DE EXECUCAO : %s segundos " % format(time.time() - tempo_inicial, '.4f')+"\n"+"\n")
    file.close()

#Metodo main que chama os metodos definidos por parametros usando o sysargv
if __name__ == '__main__':

    argumento = sys.argv[1:]
    if argumento == ['1']:
        x=1
        gravarDolar()
        log()
    elif argumento == ['2']:
        x=2
        gravarEuro()
        log()
    elif argumento == ['hora']:
        x=3
        msgSlack()
        s3()
    else:
        print('Por Favor digite o parametro 1 para dolar ou 2 para Euro')


