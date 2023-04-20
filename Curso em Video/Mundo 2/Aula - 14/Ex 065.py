# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = maior = menor = soma = contador = 0
continuar = 's'

numero = int(input('Diga-me um número inteiro: '))
soma += numero
contador += 1
maior = menor = numero

continuar = str(input('Voce deseja continuar? ')).lower().strip()[0]
if continuar == 's':
    while continuar in 's':
        numero = int(input('Diga-me um número inteiro: '))
        soma += numero
        contador += 1
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

        continuar = str(input('Voce deseja continuar? ')).lower().strip()[0]

media = soma / contador
print(f'A média dos números foi {media}, o maior número foi {maior} e o menor foi {menor}')
