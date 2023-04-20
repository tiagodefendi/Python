#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtu = date.today().year
maior = 0
menor = 0

for c in range(0,6):
    anoNascimento = int(input('Em qual ano você nasceu? '))
    idade = anoAtu - anoNascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas ja são de maior idade e {menor} ainda são de menor')
