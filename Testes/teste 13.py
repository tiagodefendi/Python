lista1 = [1,2,0]
lista2 = [3,4,5]
lista_geral = [
    lista1,
    lista2
]
print(
    f'printa as listas dentro das listas {lista_geral}\n',
    f'printa a 1ª lista {lista_geral[0]}\n',
    f'printa o 2º item da 1ª lista{lista_geral[0][1]}'
    )
print(len(lista_geral))