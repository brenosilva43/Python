# Exercícios feitos no Datalab

Os códigos desse repositório têm o intuito de mostrar algumas técnicas passadas dentro do datalab.
 
 -  CriptoMoeda: tem como objetivo a captura de dados do site m.investing das Criptomoedas e a cotação do dólar. Uma saída em csv é gerada para um futuro dataset feito no spark que calcula o valor das moedas em Real 
  - Cvm: download automático de arquivos do portal dados.gov(CVM) e extração dos arquivos zip de uma forma automática 
  - Excel: exercício feito para escrever os dados em planilhas do excel.
  - PySpark - Union: usar o PySpark do python para a união de datasets baixados do site dados.gov(CVM)
  - RequestInvest(Comentado): Uso do request para captura de dados das cotações do dólar e do euro, geração de um log de execução, uma saída em csv, gravação de dados no S3, mensagem para o Slack, Uso de maquina Ec2 AWS e crontab para execução do código via parâmetro   
  - Cálculo Regex: passagem de parâmetros e uso do regex.
  - Twitter: Captura os tweets por usuário e por hashtag. https://apps.twitter.com/ - pegar as credenciais
  - Twitter-Data: tem a finalidade de pegar os tweets por uma data especifica- Limite de 10 dias
  - twitter-Usuario: pega os tweets de um usuário - limite de 3200 tweets
  - JSON-CSV - permite a conversão dos arquivos json em csv
  - TwitterDiario - permite a Captura do Twitter a partir da data do ultimo tweet id e gravar no mesmo csv 
  - JsonTweet - Permite a captura de tweet e transforma-los em Json Limite de 3200 tweets por usuário.
  - Twitter Hora - caputura de twitter diario com atualização.
