from random import randint

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
    número_de_sorteios = randint(3, 5)
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
for i in range(0, 9):
    for k in range(0, 9):
        for j in range(0, 9):
            if lista_geral[i][k] != ' ':
                if i != j:
                    if lista_geral[i][k] == lista_geral[j][k]:
                        lista_geral[j][k] = ' '



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



for i in range(0, 9):
    print(lista_geral[i])
    print()
