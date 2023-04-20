#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
#Mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

numero1 = int(input('Escolha um número inteiro: '))
numero2 = int(input('Escolha outro número inteiro: '))

if numero1 > numero2:
    print(f'O primeiro número ({numero1}) é maior')
elif numero2 > numero1:
    print(f'O segundo número ({numero2}) é maior')
else:
    print(f'Os valores {numero1} e {numero2} são iguais')
