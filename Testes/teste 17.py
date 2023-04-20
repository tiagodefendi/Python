dic = {}
palavra = input('bahhh: ').lower().replace(' ', '')
for i in range(0, len(palavra)):
    if palavra[i] not in dic.values():
        dic[i] = palavra[i]
print(f'existem {len(dic)} diferentes nessa string')
