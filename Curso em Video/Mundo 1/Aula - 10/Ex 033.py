#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = float(input('Escolha um numero: '))
numero2 = float(input('Escolha mais um numero: '))
numero3 = float(input('Escolha outro numero: '))

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

print(f'O maior número que você escolheu é o número {maior} e o menor foi o {menor}')
