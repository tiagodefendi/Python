#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Escolha um número inteiro para eu dizer se ele é par ou impár: '))
resultado = numero % 2

if (resultado == 0):
    print(f'{numero} é um número par')
else:
    print(f'{numero} é um número impár')
