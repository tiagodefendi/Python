#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

genero = str(input('Qual o seu genero? ')).lower().strip()[0]

while genero not in 'mf':
    print('Valor invalido')
    genero = str(input('Qual o seu genero? ')).lower().strip()[0]

if genero == 'f':
    genero = 'feminino'
else:
    genero = 'masculino'

print(f'Você é do gênero {genero}')