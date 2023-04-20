#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
par = 0
impar = 0

for c in range(0, 6):
    numero = int(input('Escolha um número: '))
    if numero % 2 == 0:
        soma += numero
        par += 1
    else:
        impar += 1

print(f'Você escolheu {par} números pares e {impar} números ímpares\n a soma dos números pares é de {soma}')