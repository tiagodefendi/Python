from random import randint
from random import shuffle

#GERA AS LISTAS
lista_0 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_8 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista_geral = [
    lista_0, lista_1, lista_2,
    lista_3, lista_4, lista_5,
    lista_6, lista_7, lista_8, 
    ]
sorteio = 0
for i in range(0, 9):
    número_de_sorteios = randint(4, 6)
    while sorteio <= número_de_sorteios:
        if sorteio < número_de_sorteios:
            if randint(1, 2) == 1:
                aleatório = randint(1, 9)
                posição = randint(0, 8)
                if aleatório not in lista_geral[i]:
                    if lista_geral[i][posição] == ' ':
                        lista_geral[i][posição] = aleatório
                        sorteio += 1
        else:
            sorteio = 0
            break
    '''for j in range(0, número_de_sorteios):
        aleatório = randint(1, 9)
        if aleatório not in lista_geral[i]:
            lista_geral[i] = lista_geral[i].append(aleatório)
    shuffle(lista_geral[i])'''

#VERIFICA NA VERTICAL
for i in range(0, 9):
    for k in range(0, 9):
        for j in range(0, 9):
            if lista_geral[i][k] != ' ':
                if i != j:
                    if lista_geral[i][k] == lista_geral[j][k]:
                        lista_geral[j][k] = ' '
#VERIFICA NO QUADRANTE
for i in range(0, 3):
    for k in range(0, 3):
        for j in range(0, 3):
            for m in range(0, 3):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(3, 6):
    for k in range(0, 3):
        for j in range(3, 6):
            for m in range(0, 3):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(6, 9):
    for k in range(0, 3):
        for j in range(6, 9):
            for m in range(0, 3):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(0, 3):
    for k in range(3, 6):
        for j in range(0, 3):
            for m in range(3, 6):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(3, 6):
    for k in range(3, 6):
        for j in range(3, 6):
            for m in range(3, 6):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(6, 9):
    for k in range(3, 6):
        for j in range(6, 9):
            for m in range(3, 6):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(0, 3):
    for k in range(6, 9):
        for j in range(0, 3):
            for m in range(6, 9):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(3, 6):
    for k in range(6, 9):
        for j in range(3, 6):
            for m in range(6, 9):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '
for i in range(6, 9):
    for k in range(6, 9):
        for j in range(6, 9):
            for m in range(6, 9):
                if lista_geral[i][k] != ' ':
                    if i != j:
                        if lista_geral[i][k] == lista_geral[j][m]:
                            lista_geral[j][m] = ' '

#IMPRAME A TABELA
reseta = '\033[m'
preto = '\033[30;40m'
branco = '\033[7m'
azul = '\033[30;44m'
for i in range(19):
    if i not in [7, 9, 11]:
        if i % 2 == 0:
            for j in range(19):
                print(f'{preto}---{reseta}', end='')
            print('')
        else:
            for j in range(19):
                if j % 2 == 0:
                    print(f'{preto}---{reseta}', end='')
                else:
                    if j not in [7, 9, 11]:
                        print(f'{branco} {lista_geral[((i+1)//2)-1][((j+1)//2)-1]} {reseta}', end='')
                    else:
                        print(f'{azul} {lista_geral[((i+1)//2)-1][((j+1)//2)-1]} {reseta}', end='')
            print('')
    else:
        if i % 2 == 0:
            for j in range(19):
                print(f'{preto}---{reseta}', end='')
            print('')
        else:
            for j in range(19):
                if j % 2 == 0:
                    print(f'{preto}---{reseta}', end='')
                else:
                    if j in [7, 9, 11]:
                        print(f'{branco} {lista_geral[((i+1)//2)-1][((j+1)//2)-1]} {reseta}', end='')
                    else:
                        print(f'{azul} {lista_geral[((i+1)//2)-1][((j+1)//2)-1]} {reseta}', end='')
            print('')
