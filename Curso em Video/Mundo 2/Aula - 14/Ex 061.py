#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

inicio = int(input('Escolha um  numero para iniciar a PA: '))
razao = int(input('Qual a razão da PA? '))
pa = inicio
contador = 1
fim = False

print(f'A progressão aritimetica é:\n{inicio}', end=', ')

while not fim:
    if contador < 10:
        pa += razao
        contador += 1
        print(pa, end=', ')
    else:
        fim = True
