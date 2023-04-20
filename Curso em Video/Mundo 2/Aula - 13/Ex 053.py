#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços. Exemplos de palíndromos:

palindromo = input('Qual é a frase? ').strip().lower().split()
grudar = '' .join(palindromo)
inverso = ''
'''inverso = grudar[::-1]'''
for pali in range(len(grudar)+1, -1, -1):
    inverso += grudar[pali]
if inverso == grudar:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')