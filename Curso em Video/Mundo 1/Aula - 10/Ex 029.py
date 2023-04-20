#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00
#por cada Km acima do limite.

velocidade =float(input('ALERTA DE RADAR \nQual é a velocidade do seu carro carro:'))
multa = (velocidade - 80) * 7

if (velocidade <= 80):
    print('Muito bem, continui dirigindo com cuidado')
else:
    print(f'MULTADO! Você exedeu o limite de 80Km/h \nVocê deve pagar um taxa de {multa} para poder passar. ')