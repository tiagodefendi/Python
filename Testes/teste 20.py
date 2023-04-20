ana = 'anã'
print(ana[::-1])

l = ['a', 'b']
lista = ['asda','basda','bfks','kkjhku']
for i in range(len(lista)):
    for c in range(len(l)):
        if l[c] in lista[i]:
            print(lista[i])

for i in range(len(lista)):
    for c in range(len(l)):
        if l[c] not in lista[i]:
            print(lista[i])