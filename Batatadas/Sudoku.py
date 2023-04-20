from random import randint

class Sudoku:
    def __init__(self):
        self.campos = [[0] * 9] * 9

        self.lista_0 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_7 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_8 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lista_geral = [
            self.lista_0, self.lista_1, self.lista_2,
            self.lista_3, self.lista_4, self.lista_5,
            self.lista_6, self.lista_7, self.lista_8,
        ]
        sorteio = 0
        for i in range(0, 9):
            número_de_sorteios = randint(3, 5)
            while sorteio <= número_de_sorteios:
                if sorteio < número_de_sorteios:
                    if randint(1, 2) == 1:
                        aleatório = randint(1, 9)
                        posição = randint(0, 8)
                        if aleatório not in self.lista_geral[i]:
                            if self.lista_geral[i][posição] == ' ':
                                self.lista_geral[i][posição] = aleatório
                                sorteio += 1
                else:
                    sorteio = 0
                    break

    def preenche_Campo(self):
        for i in range(0, 9):
            for k in range(0, 9):
                for j in range(0, 9):
                    if self.lista_geral[i][k] != ' ':
                        if i != j:
                            if self.lista_geral[i][k] == self.lista_geral[j][k]:
                                self.lista_geral[j][k] = ' '
        for i in range(0, 3):
            for k in range(0, 3):
                for j in range(0, 3):
                    for m in range(0, 3):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(3, 6):
            for k in range(0, 3):
                for j in range(3, 6):
                    for m in range(0, 3):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(6, 9):
            for k in range(0, 3):
                for j in range(6, 9):
                    for m in range(0, 3):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(0, 3):
            for k in range(3, 6):
                for j in range(0, 3):
                    for m in range(3, 6):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(3, 6):
            for k in range(3, 6):
                for j in range(3, 6):
                    for m in range(3, 6):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(6, 9):
            for k in range(3, 6):
                for j in range(6, 9):
                    for m in range(3, 6):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(0, 3):
            for k in range(6, 9):
                for j in range(0, 3):
                    for m in range(6, 9):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(3, 6):
            for k in range(6, 9):
                for j in range(3, 6):
                    for m in range(6, 9):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '
        for i in range(6, 9):
            for k in range(6, 9):
                for j in range(6, 9):
                    for m in range(6, 9):
                        if self.lista_geral[i][k] != ' ':
                            if i != j:
                                if self.lista_geral[i][k] == self.lista_geral[j][m]:
                                    self.lista_geral[j][m] = ' '

    def imprime_Campos(self):
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
                                print(f'{branco} {self.lista_geral[((i + 1) // 2) - 1][((j + 1) // 2) - 1]} {reseta}',
                                      end='')
                            else:
                                print(f'{azul} {self.lista_geral[((i + 1) // 2) - 1][((j + 1) // 2) - 1]} {reseta}',
                                      end='')
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
                                print(f'{branco} {self.lista_geral[((i + 1) // 2) - 1][((j + 1) // 2) - 1]} {reseta}',
                                      end='')
                            else:
                                print(f'{azul} {self.lista_geral[((i + 1) // 2) - 1][((j + 1) // 2) - 1]} {reseta}',
                                      end='')
                    print('')

    def movimento_valido(self, l, c, valor):
        if valor != 0:
            for i in range(9):
                for j in range(9):
                    if self.lista_geral[l][j] == valor:
                        print("Teste1")
                        return False
                    if self.lista_geral[i][c] == valor:
                        print(i, c, self.lista_geral[i][c])
                        print("Teste2")
                        return False
            if l in range(0, 3):
                if c in range(0, 3):
                    for j in range(0, 3):
                        for m in range(0, 3):
                            if valor == self.lista_geral[j][m]:
                                return False
                elif c in range(3, 6):
                    for j in range(3, 6):
                        for m in range(0, 3):
                            if valor == self.lista_geral[j][m]:
                                return False
                elif c in range(6, 9):
                    for j in range(6, 9):
                        for m in range(0, 3):
                            if valor == self.lista_geral[j][m]:
                                return False
            elif l in range(3, 6):
                if c in range(0, 3):
                    for j in range(0, 3):
                        for m in range(3, 6):
                            if valor == self.lista_geral[j][m]:
                                return False
                if c in range(3, 6):
                    for j in range(3, 6):
                        for m in range(3, 6):
                            if valor == self.lista_geral[j][m]:
                                return False
                if c in range(6, 9):
                    for j in range(6, 9):
                        for m in range(3, 6):
                            if valor == self.lista_geral[j][m]:
                                return False
            elif l in range(6, 9):
                if c in range(0, 3):
                    for j in range(0, 3):
                        for m in range(6, 9):
                            if valor == self.lista_geral[j][m]:
                                return False
                if c in range(3, 6):
                    for j in range(3, 6):
                        for m in range(6, 9):
                            if valor == self.lista_geral[j][m]:
                                return False
                if c in range(6, 9):
                    for j in range(6, 9):
                        for m in range(6, 9):
                            if valor == self.lista_geral[j][m]:
                                return False
            return True
        return False

    def fim(self):
        for i in range(9):
            for j in range(9):
                if self.campos[i][j] != 0:
                    continue
                else:
                    return False
        return True


def main(): 
    jogo = Sudoku()
    jogo.preenche_Campo()
    while jogo.fim() == False:
        jogo.imprime_Campos()
        l = int(input('Escolha uma linha: ')) - 1  # O -1 pois as coordenadas das lista começam em 0
        c = int(input('Escolha uma coluna: ')) - 1
        valor = int(input('Digite um valor: '))
        if jogo.movimento_valido(l, c, valor) == True:
            jogo.lista_geral[l][c] = valor
        else:
            print('Posição Inválida')
            continue
main()