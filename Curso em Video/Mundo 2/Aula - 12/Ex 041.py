#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o
#ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date

anoNascimento=int(input('Insira o ano do nascimento do atleta: '))
anoUser= date.today().year
idade= anoUser - anoNascimento

if idade <= 9:
    print(f'O atleta com {idade} anos esta na classificação Mirim')
elif 9 < idade <= 14:
    print(f'O atleta com {idade} anos esta na classificação Infantil')
elif 14 < idade <= 19:
    print(f'O atleta com {idade} anos esta na classificação Júnior')
elif 19 < idade <= 25:
    print(f'O atleta com {idade} anos esta na classificação Sênior')
else:
    print(f'O atleta com {idade} anos esta na classificação Master')
