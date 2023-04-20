#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Escolha um numero: '))
primo = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        primo += 1

if primo == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')
