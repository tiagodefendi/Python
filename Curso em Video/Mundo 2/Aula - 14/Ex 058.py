#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

sorteado = randint(1, 10)

print('Sorteando números')
sleep(0.8)
print('Espere um pouco')
sleep(0.4)
print('...')
sleep(0.4)
print('Pronto')
sleep(0.25)

acerto = False
tentativas = 1
escolha = 0

temperatura = sorteado - escolha
if temperatura < 0:
    temperatura *= -1

dica = str(input('Você quer dicas? ')).lower().strip()[0]
if dica == 's':
    dica = int(input('Que nível de dica? (1-2) '))
else:
    dica = 0

while not acerto:
    escolha = int(input('Escolha um número de 1 a 10: '))

    if escolha == sorteado:
        acerto = True
    else:
        sleep(0.8)
        print('\033[31mERROU!\033[0mTente novamente')
        tentativas += 1

        if dica == 1:
            if escolha < sorteado:
                print('Tente um número maior!')
            else:
                print('Tente um número menor!')
        if dica == 2:
            if temperatura <= 3:
                print('Por pouco...')
            elif 3 < temperatura < 6:
                print('Quase...')
            else:
                print('Falta muito')

print(f'\033[32mPARABENS!\033[0m Você acertou com {tentativas} tentativas!')
