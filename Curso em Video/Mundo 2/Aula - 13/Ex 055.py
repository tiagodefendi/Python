#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

peso = 0
pesoMaior = 0
pesoMenor = 0

for c in range(0, 5):
    peso = float(input('Qual seu peso? '))
    if pesoMenor == 0:
        pesoMenor = peso
    elif peso > pesoMaior:
        pesoMaior = peso
    elif peso < pesoMenor:
        pesoMenor = peso

print(f'O maior peso é de {pesoMaior}Kg e o menor peso é de {pesoMenor}')
