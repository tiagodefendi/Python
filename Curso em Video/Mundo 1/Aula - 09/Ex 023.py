x = int(input('Escolha um número interio: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')
