#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

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

parar = False
limite = 1

while not parar:
    contador = 1
    fim = False
    limite = int(input('\nVocê deseja ver mais quantos termos da PA? '))
    if limite != 0:
        pa += razao
        print(pa, end=', ')
        while not fim:
            if contador < limite:
                pa += razao
                contador += 1
                print(pa, end=', ')
            else:
                fim = True
    else:
        parar = True
