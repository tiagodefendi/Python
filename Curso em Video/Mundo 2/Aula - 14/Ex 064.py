# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

valor = numeros =soma = 0
valor = int(input('Diga-me um número inteiro '))

while valor != 999:
        numeros += 1
        soma += valor
        valor = int(input('Diga-me um número inteiro '))

print(f'Você me disse {numeros} números e a soma deles é {soma}')
