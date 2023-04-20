#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = valor / (anos * 12)

if prestacao < salario * 30:
    print(f'\033[1;4;32mAPROVADO!\033[m \nO emprestimo de \033[33mR$ {valor:.2f}\033[m para compra da casa foi aceito. '
          f'E sera pago em {anos} anos em prestações com o valor de \033[33mR$ {prestacao:.2f}\033[m')
else:
    print(f'\033[1;4;31mNEGADO!\033[m \nO emprestimo de \033[33mR$ {valor:.2f}\033[0m para compra da casa foi recusado, '
          f'pois passou o limite de 30% do salário. '
          f'O seu salário é de \033[34m{salario:.2f}R$\033[m e as prestações em {anos} ficariam \033[33mR${prestacao:.2f}\033[m')
