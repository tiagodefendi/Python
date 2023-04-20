#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1=float(input('Qual foi sua primeira nota? '))
nota2=float(input('Qual foi sua segunda nota? '))
media = (nota1 + nota2)/2

if media < 5:
    print(f'\033[31mREPROVADO\033[0m, sua édia foi {media}')
elif 5 <= media < 7:
    print(f'\033[33mRECUPERAÇÃO\033[0m, sua média foi {media}')
else:
    print(f'\033[32mAPROVADO\033[0m, sua média foi {media}')
