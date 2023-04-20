#Exercício Python 51: Desenvolva um programa que leia o primeiro termo
#a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input('Escolha um  numero para iniciar a PA: '))
razao = int(input('Qual a razão da PA? '))
fimPa = inicio + 9 * razao + razao

for c in range(inicio, fimPa, razao):
    print(c)
