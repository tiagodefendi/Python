#Importes
from requests import get
from bs4 import BeautifulSoup as bs
from decouple import config
from discord.ext import commands

#Botão para comandos
bot = commands.Bot('$')

@bot.command(name='valor')
async def monetary(ctx, coin):
    unidade = coin.lower()

    url = get(f'https://www.remessaonline.com.br/cotacao/cotacao-{unidade}')
    soup = bs(url.text, 'html.parser')

    valor = soup.find('div', {'class':'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
        
    await ctx.send(f'A moeda {coin} vale R${valor}.')

#Roda o Bot
TOKEN = config('TOKEN')
bot.run(TOKEN)
