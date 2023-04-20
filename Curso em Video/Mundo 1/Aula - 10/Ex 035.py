#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao
#usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Diga o comprimeto de um segmento de reta: '))
reta2 = float(input('Diga o comprimeto de um outra segmento de reta: '))
reta3 = float(input('Diga o comprimeto de mais um segmento de reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print(f'Os segmentos de reta {reta1, reta2, reta3} podem formar um triângulo')
else:
    print(f'Os segmentos de reta {reta1, reta2, reta3} não podem formar um triângulo')
