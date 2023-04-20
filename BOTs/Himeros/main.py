#Importes
from decouple import config
from time import sleep

#Import do Discord
import discord
from discord import channel
from discord.ext import commands,tasks
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

himeros = commands.Bot('\\')

#Avisa quando o Himeros está aberto
@himeros.event
async def on_ready():
    print('Cheguei 😈')


#Eventos
@himeros.event
async def on_message(message):
    
    if message.author == himeros.user:
        return
    
    elif 'plvr' in message.content:
        await message.delete()
        await message.channel.send(
            f'Olha a boca, {message.author.mention}!'
        )
        sleep(3)
    await himeros.process_commands(message)

@himeros.event
async def on_command_error(ctx,error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send('Por favor envie todos argumentos! Digete "\\help" para saber mais')
    elif isinstance(error,CommandNotFound):
        await ctx.send('O comando não existe! Digete "\\help" para saber os comandos existentes')
    else:
        raise error


#Comandos
@himeros.command(name='oi', help='| Envia um "oi"')
async def send_hello(ctx):
    name = ctx.author.name
    if name == 'Infinity':
        response = f'Seja bem vindo, óh grande mestre gostoso {name}'            
    else:
        response = f'Olá, {name}'    
    await ctx.send(response)

@himeros.command(name='calcular', help='| Calcula uma expressão(Requer uma expressão)')
async def calculation_expression(ctx, *expression):
    expression = ''.join(expression)
    response = eval(expression)
    await ctx.send(f'A resposta é {response}')

@himeros.command(name='shiii', help='| Envia uma mensagem no privado')
async def secret(ctx):
    try:
        await ctx.send('Cheque seu privado. 🔒')
        await ctx.author.send('Comi o kur de quem leu...')
    except discord.errors.Forbidden:
        await ctx.send(
            'Não posso te contar a fofoca, tente habilitar "Receber mensagens de qualquer pessoa do Servidore(Opições->Privacidade)"'
            )

@himeros.command(name='foto', help='| Envia uma foto aleatória da internet')
async def get_random_image(ctx):
    url_image = 'https://picsum.photos/512/512'
    embed_image = discord.Embed(
        title = 'Resultado da busca de imagem',
        description ='A busca é totalmente aleatória',
        color = 0x7E95A4
    )
    embed_image.set_author(name=himeros.user.name, icon_url=himeros.user.avatar_url)
    embed_image.set_footer(text=f'Feito por {himeros.user.name}', icon_url=himeros.user.avatar_url)
    embed_image.add_field(name='API', value='Usamos a API do https://picsum.photos')
    embed_image.add_field(name='Parametros', value='(largura)/(altura)')
    embed_image.add_field(name='Exemplo:', value='https://picsum.photos/1000/1000', inline=False)
    embed_image.set_image(url=url_image)
    await ctx.send(embed=embed_image)


#Roda o Bot
TOKEN = config('TOKEN')
himeros.run(TOKEN)
