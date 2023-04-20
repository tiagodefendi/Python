#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Escolha um número inteiro para ser convertido: '))
baseConversao = int(input('''Escolha qual será a base de conversão:'
[1] para binário
[2] para octal
[3] para hexadecimal
Eu escolha a '''))

if baseConversao == 1:
    print(f'o número {numero} em binario é {bin(numero)[2:]}')
elif baseConversao == 2:
    print(f'o número {numero} em octal é {oct(numero)[2:]}')
elif baseConversao == 3:
    print(f'o número {numero} em hexadecimal é {hex(numero)[2:]}')
else:
    print(f'ERROR as opções eram 1 - 2 - 3 e vc escolheu {numero}')
