#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input('Qual número você quer o fatorial? '))

fatorialCont = numero
fatorial = 1

fim = False

while not fim:
    if fatorialCont > 0:
        fatorial *= fatorialCont
        fatorialCont -= 1
    else:
        print(f'O fatorial do número {numero} é {fatorial}')
        fim = True
