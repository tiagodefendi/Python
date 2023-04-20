numero = int(input('Escolha um número: '))
primo = 1
contPrimo = 0

while primo != numero + 1:
    if numero % primo == 0:
        contPrimo += 1
        print(f'\033[32m{primo}\033[0m')
    else:
        print(f'\033[31m{primo}\033[0m')
    primo += 1
if contPrimo == 2:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')
