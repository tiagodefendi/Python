from requests import get
from bs4 import BeautifulSoup as bs

unidade = str(input(
    'Escolha a moeda você quer a cotação:\nDolar\nEuro\nLibra Esterlina\nIene Japones\nPeso Argentino\nResposta:'
    )).lower().strip().replace(' ','-')

url = get(f'https://www.remessaonline.com.br/cotacao/cotacao-{unidade}')
soup = bs(url.text, 'html.parser')

moeda = soup.find('div', {'class':'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
moeda = moeda.replace(',', '.')
moeda = float(moeda)

while True:
    try:
        quantidade_de_moedas = int(input('Digite quantas moedas você possui: '))
    except:
        print('Erro no que foi digitado, tente novamente.')
    else:
        break

reais = moeda*quantidade_de_moedas
reais = str(reais)
reais = reais.replace('.',',')

print(f'Você possui R${reais}.')
