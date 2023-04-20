#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
from time import sleep

sorteio = 1,2,3,4,5
sorteado = choice(sorteio)

print('Sorteando números')

print('Espere um pouco')
sleep(2)
print('Mais um pouco')
sleep(2)
print('Pronto')

escolha = int(input('Escolha um número de 1 a 5: '))
if escolha == sorteado:
    print('PARABENS! Você acertou!')
else:
    print(f'ERROU! \nEu pensei no número {sorteado}')
