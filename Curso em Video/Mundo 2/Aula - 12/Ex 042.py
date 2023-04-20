#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

reta1 = float(input('Diga o comprimeto de um segmento de reta: '))
reta2 = float(input('Diga o comprimeto de um outra segmento de reta: '))
reta3 = float(input('Diga o comprimeto de mais um segmento de reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print(f'Os segmentos de reta {reta1, reta2, reta3} podem formar um triângulo')
    if reta1 == reta2 == reta3:
        print('Esse triangulo sera equilatero, com todos lados iguais')
    elif reta1 != reta2 != reta3 != reta1:
        print('Esse triangulo sera escaleno, com todos lados diferentes.')
    else:
        print('Esse triangulo sera Isósceles, com dois lados iguais e um diferente')
else:
    print(f'Os segmentos de reta {reta1, reta2, reta3} não podem formar um triângulo')
