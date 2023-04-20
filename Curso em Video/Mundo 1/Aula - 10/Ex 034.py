#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o
#valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salário do funcionario? '))
aumentGrande = salario * 1.15
aumentPequeno = salario * 1.1

if salario <= 1250:
    print(f'O valor do salario com aumento sera de {aumentGrande:.2f}R$')
else:
    print(f'O valor do salario com aumento sera de {aumentPequeno:.2f}R$')
