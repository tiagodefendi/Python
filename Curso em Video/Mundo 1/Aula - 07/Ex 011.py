print('Você vai pintar as paredes da sua casa, a cada dois m² você ira ultilizar 2 L de tinta.')
h=float(input('Qual a altura da sua casa? '))
l=float(input('Qual a largura da sua casa? '))
a=h*l
lt=a/2
print(f'As paredes de sua casa medem {l}m x {h}m, então a área das paredes medem {a}m² e será gasto {lt:.2f}L de tinta para pintar a parede.')
