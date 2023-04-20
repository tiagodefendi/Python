p=float(input('Valor do Produto: R$ '))
d=float(input('Valor do desconto: % '))
dd=(100-d)/100
print(f'Valor do produto com desconto: R$ {p*dd:.2f}')
