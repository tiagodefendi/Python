dic = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
    }
frase = input('bahhhh... ')
for i in range(0, len(frase)):
    if frase[i] in dic:
        dic[(frase[i])] += 1
print(dic)
