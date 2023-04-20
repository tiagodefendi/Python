massa = float(input('Informe sua massa: '))
altura = float(input('Informe sua altura: '))
imc = massa/(altura**2)

if imc <= 16:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;31mDESNUTRIDO!!!\033[m')
elif 16 < imc <= 17:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;31mSUBDESNUTRIDO!!\033[m')
elif 17 < imc <= 20.7:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;34mABAIXO DO PESO!\033[m')
elif 20.7 < imc <= 26.4:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;32mPESO NORMAl\033[m')
elif 26.4 < imc <= 27.8:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;33mLEVEMENTE ACIMA DO PESO!\033[m')
elif 27.8 < imc <= 31.1:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;33mSOBREPESO!!\033[m')
elif 31.1 < imc <= 35.8:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;31mOBESIDADE GRAU 1!!!\033[m')
elif 35.8 < imc <= 40:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;31mOBESIDADE GRAU 2!!!\033[m')
elif 40 < imc <= 200:
    print(f'Seu imc é aproximadamente {imc:.1f} \n'
          f'\033[1;4;31mOBESIDADE GRAU 3 / MÓRBIDA!!!\033[m')
else:
    print(
        f'Seu imc é aproximadamente {imc:.1f} \n'
        f'\033[1;4;31mOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE!!!!!\033[m')
    print('Claro se você conseguir...')
    print('Quer q eu chame um guindaste..?')