#Exercício Python 48: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0

for numero in range(3,501, 3):
    if numero % 2 == 1:
        soma += numero
        contador += 1
print(f'A soma dos {contador} números é de {soma}')
