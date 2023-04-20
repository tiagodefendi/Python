#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

numero1 = int(input('Insira um valor: '))
numero2 = int(input('Insira outro valor: '))

fim = False
soma = numero1 + numero2
produto = numero1 * numero2

while not quebra:

    funcao = int(input('Selecione o que você quer fazer:\n[1]Somar\n[2]Multiplicar'
                       '\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\nR: '))

    if funcao == 1:
        print(f'A soma de {numero1} e {numero2} é de {soma}')
    elif funcao == 2:
        print(f'O produto entre {numero1} e {numero2} é de {produto}')
    elif funcao == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que o número {numero2}')
        else:
            print(f'O número {numero2} é maior que o número {numero1}')
    elif funcao == 4:
        numero1 = int(input('Insira um valor: '))
        numero2 = int(input('Insira outro valor: '))
    elif funcao == 5:
        quebra = True
    else:
        print('Opição iválidia ! Tente novamente')
