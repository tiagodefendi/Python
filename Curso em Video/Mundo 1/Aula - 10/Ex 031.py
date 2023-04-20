#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia =float(input('Qual a distancia da viagem que você ira percorrer? '))
taxaCurta = distancia * 0.5
taxaLonga = distancia * 0.45

if ( distancia <= 200 ):
    print(f'A taxa que você ira pagar é de {taxaCurta:.2f} R$')
else:
    print(f'A taxa que você ira paragar é de {taxaLonga:.2f} R$')

'''taxa = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(f'A taxa que você ira paragar é de {taxa:.2f} R$')'''
