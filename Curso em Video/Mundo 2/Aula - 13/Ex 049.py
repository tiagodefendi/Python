#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
#que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Escolha o numero q você deseja a tabuada:'))
numeroMult = 0

for tabuada in range(1,11):
    numeroMult = tabuada * numero
    print(f'{numero} x {tabuada} = {numeroMult}')
