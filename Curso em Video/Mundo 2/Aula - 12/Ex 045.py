#Exercício Python 45: Crie um programa que faça o escolhacm[computador] jogar Jokenpô com você.

from random import randint

escolhacm = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
pessoa = input('Escolha pedra, papel ou tesoura: ').strip().lower()

if pessoa == escolhacm[computador]:
    print(f'Empate os dois escolheram {pessoa}')
elif pessoa == 'papel' and escolhacm[computador] == 'pedra':
    print(f'Você ganhou eu escolhi {escolhacm[computador]}')
elif pessoa == 'tesoura' and escolhacm[computador] == 'papel':
    print(f'Você ganhou eu escolhi {escolhacm[computador]}')
elif pessoa == 'pedra' and escolhacm[computador] == 'tesoura':
    print(f'Você ganhou eu escolhi {escolhacm[computador]}')
elif escolhacm[computador] == 'papel' and pessoa == 'pedra':
    print(f'Você perdeu eu escolhi {escolhacm[computador]}')
elif escolhacm[computador] == 'tesoura' and pessoa == 'papel':
    print(f'Você perdeu eu escolhi {escolhacm[computador]}')
elif escolhacm[computador] == 'pedra' and pessoa == 'tesoura':
    print(f'Você perdeu eu escolhi {escolhacm[computador]}')
else:
    print(f'Você escolhi {pessoa} e eu escolhi {escolhacm[computador]}')