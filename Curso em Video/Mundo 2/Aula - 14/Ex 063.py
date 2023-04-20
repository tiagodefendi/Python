# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

numero = int(input('Quantos numeros da sequencia de Fibonacci você quer ver? '))
fibonacci1 = 0
fibonacci2 = 1
fibonacci3 = fibonacci1 + fibonacci2
contador = 2

print(f'{0}, {1}', end=', ')

while contador < numero:
        print(f'{fibonacci3}', end=', ')
        contador += 1
        fibonacci1 = fibonacci2
        fibonacci2 = fibonacci3
        fibonacci3 = fibonacci1 + fibonacci2
