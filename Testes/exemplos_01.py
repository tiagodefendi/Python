from math import pi, sin

def print_oi():
    print('Oi')

def print_msg(msg):
    print(msg)

def print_multi_msg(msg, n):
    print((msg+' ') * n)

def desenha_quadrado(n):
    print( '*' * n)
    print( '*', ' ' *(n-2), '*', sep='' )
    print( '*' , ' ' *(n-4), '*' )
    print( '*' * n)

# Funcao converte Celsius para  Fahrenheit
def converte(t):
    return (t*9/5)+32

def seno_grau(x):
    return sin(pi*x/180)


def multiple_print(string, n, palavras_erradas):
    if string in palavras_erradas:
        return
    print(string * n)

def print_msg_op(msg, n=1):
    print(msg*n)


def soma_digito(a):
    digitos=str(a)
    soma=0
    for dig in digitos:
        soma+=int(dig)
    return soma

def soma_numeros_print(a,b):
    print(a+b)

def soma_numeros_return(a,b):
    return a+b

def main():

    print_oi()
    print_msg('ola')
    print_multi_msg('ola',2) ## mostrar print_multi_msg(2,'ola')
    desenha_quadrado(10)
    desenha_quadrado(15)

    x=10
    y=20
    soma_numeros_print(x,y)

    soma_numeros_return(x,y)
    print(soma_numeros_return(x,y))

    temp=40
    print(f'{temp}  Celcius -> {converte(temp)} Fahrenheit ')

    print(sin(30))## em radianos
    print(seno_grau(30))## em radianos


    palavras=['tade','bo']
    multiple_print('Boa',2,palavras)
    multiple_print('bo',2,palavras)
    multiple_print('Bo',2,palavras)

    print_msg_op('Oi')
    print_msg_op('Oi',2)



    ### exercicio
   ## Escreva uma função chamada soma_dígitos que receba um número inteiro e retorne a soma dos
  #dígitos de num
    num=1234
    num=1000
    print(f'Soma dos digitos de {num} eh: {soma_digito(num)}')


if __name__ == "__main__":
    main()




