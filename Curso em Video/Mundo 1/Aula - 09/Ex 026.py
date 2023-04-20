x = str(input('Digite uma frase: ')).lower().strip()
print('Na sua frase apareceu a letra a {} vezes'.format(x.count('a')))
print('Na sua frase o primeiro "a" aparece no {}º caractere.'.format((x.find('a')+1)))
print('Na sua frase o último "a" aparece no {}º caractere.'.format((x.rfind('a')+1)))
