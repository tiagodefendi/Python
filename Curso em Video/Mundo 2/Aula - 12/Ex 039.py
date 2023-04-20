# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade,se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Qual sua idade? '))

tempoFalt = 18 - idade
tempoPass = idade - 18

if idade == 1:
    print('Só falta um anos para você se alistar!')
elif idade < 18:
    print(f'Ainda faltam {tempoFalt} anos para você se alistar!')
elif idade == 18:
    print(f'Está na hora de se alistar!')
elif idade == 19:
    print('JA faz um ano que você deveria se alistar!')
else:
    print(f'Ja passaram {tempoPass} ano que você deveria se alisatar!')
