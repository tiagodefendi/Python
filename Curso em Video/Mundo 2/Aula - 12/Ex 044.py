#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

compra = float(input('Qual valor do compra? R$ '))

dinheiro = compra * 0.9
cartao = compra * 0.95
juros = compra * 1.2

pagamento = input('Você deseja pagar em dinheiro ou no cartão? ').strip().lower()

if pagamento == 'dinheiro':
    print(f'Pagando em dinheiro o valor de R$ {compra} tera um disconto de 10% passando a ser de R$ {dinheiro:.f2}')
else:
    parcela = input(f'Você deseja parcelar a compra de R$ {compra}? ').strip().lower()
    if parcela == 'sim':
        vezes = int(input('Em quantas vezes vc deseja parcelar? '))
        if vezes >= 3:
            print(f'Pagando em {vezes}x no cartão tera um juros simples de 20%, assim você devera pagar {vezes} parcelas de '
                  f'R$ {juros/vezes:.2f}')
        else:
            print(f'Parcelando em duas vezes não tera nenhum disconto, assim você devera pagar 2 parcelas de {compra/2:.2f}')
    else:
        print(f'Pagando no cartão o valor de R$ {compra} tera um disconto de 5% passando a ser de R$ {cartao:.2f}')
