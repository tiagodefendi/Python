#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Me diga em que ano nós estamos: '))
bissextidade = ano % 4

if ano == 0:
    ano = date.today().year

if bissextidade == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Nossa que legal {ano} é um ano bissexto')
if bissextidade == 1:
    print(f'Falta pouco para um ano bissexto')
if bissextidade == 2:
    print(f'Ainda fata metade')
if bissextidade == 3:
    print(f'Estamos muito longe')
