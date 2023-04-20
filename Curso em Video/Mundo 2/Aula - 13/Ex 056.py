#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
#quantas mulheres têm menos de 20 anos.

idadeGrup = 0
homemMV = 0
nomeHomMV = ''
mulherM20 = 0

for c in range(0,4):

    nome = input('Qual seu nome? ')
    idade = int('Qual sua idade? ')
    sexo = input('Qual seu gênero? ').strip().lower()

    idadeGrup += idade
    if sexo == 'masculino':
        if idade > homemMV:
            homemMV = idade
            nomeHomMV = nome
    else:
        if idade < 20:
            mulherM20 += 1

idadeMed = idadeGrup / 5

print(f'A idade média do grupo é de {idadeMed}, o homem mais velho se chama {nomeHomMV}, e {mulherM20} mulheres tem menos de vinte anos.')
