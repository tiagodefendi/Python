n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))
n4 = int(input('Pela ultima vez digite número um inteiro: '))

if (n1 % 2) == 0:
        n1 = 0
if (n2 % 2) == 0:
        n2 = 0
if (n3 % 2) == 0:
        n3 = 0
if (n4 % 2) == 0:
        n4 = 0

soma = n1 + n2 +n3 + n4

print(f'A soma dos numeros impares é igual a {soma}')
