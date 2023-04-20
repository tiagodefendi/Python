km=float(input('Quantos quilimonetros durou o trajeito? '))
d=float(input('Quantos dias durou o trajeto? '))
pk=km*0.15
pd=d*60
print(f'O preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado é de R${pk+pd:.2f}.')
