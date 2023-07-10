import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://www63.bb.com.br/portalbb/djo/id/comprovante/consultaDepositoJudicial,802,4647,4650,0,1,1.bbx')

soup = BeautifulSoup(resposta.content, "html.parser")
print(resposta.content)
# print(soup.find(class_='g-recaptcha').findAllNext)


