#INSERIR NOME

nomeSplt = str(input('Me diga seu nome completo: ')).strip().split()
nomeComp = ' '.join(nomeSplt)

#INSERIR MASSA

massa = float(input(f'{nomeSplt[0]}, qual sua massa? '))

#INSERIR ALTURA

altura = float(input(f'Legal {nomeSplt[0]}, qual sua altura? '))

#INSERIR SEXO

sexo = str(input('Você é do sexo \033[1;34mmasculino\033[0m ou \033[1;35mfeminino\033[0m? ')).lower().strip()

#INSERIR IDADE

idade = float(input('Quantos anos você tem? '))

#CONFIRMAÇÂO DE DADOS
#FAZER

#CÁLCULOS
if sexo == 'masculino':
    k = 4
else:
    k = 2
peso_ideal = altura - 100 - (altura - 150)/k

imc = massa/(altura**2)

# CONTA PARA O SEXO MASCULINO
if sexo == 'masculino':
    print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} você é {imc_masculino}')

    if 5 <= idade <= 11:
        if imc <= 11.5:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mDESNUTRIDO!!!\033[m')
        elif 11.5 < imc <= 12.9:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mSUBDESNUTRIDO!!\033[m')
        elif 12.9 < imc <= 15:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;34mABAIXO DO PESO!\033[m')
        elif 15 < imc <= 20.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;32mPESO NORMAl\033[m')
        elif 20.3 < imc <= 23:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;33mLEVEMENTE ACIMA DO PESO!\033[m')
        elif 23 < imc <= 24.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;33mSOBREPESO!!\033[m')
        elif 24.3 < imc <= 26.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 1!!!\033[m')
        elif 26.8 < imc <= 28:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 2!!!\033[m')
        elif 28 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 3 / MÓRBIDA!!!\033[m')
        elif imc > 200:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                f'\033[1;4;31mOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE!!!!!\033[m')
            print('Claro se você conseguir...')
            print('Quer q eu chame uma carriola?..?')

    elif 11 < idade <= 14:
        if imc <= 13:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mDESNUTRIDO!!!\033[m')
        elif 13 < imc <= 14.2:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mSUBDESNUTRIDO!!\033[m')
        elif 14.2 < imc <= 16.5:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;34mABAIXO DO PESO!\033[m')
        elif 16.6 < imc <= 23:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;32mPESO NORMAl\033[m')
        elif 23 < imc <= 24.6:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;33mLEVEMENTE ACIMA DO PESO!\033[m')
        elif 24.6 < imc <= 28.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;33mSOBREPESO!!\033[m')
        elif 28.8 < imc <= 30:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 1!!!\033[m')
        elif 30 < imc <= 32.1:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 2!!!\033[m')
        elif 32.1 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 3 / MÓRBIDA!!!\033[m!!!')
        else:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                f'\033[1;4;31mOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE!!!!!\033[m')
            print('Claro se você conseguir...')
            print('Quer q eu chame um caminhão..?')

    elif 14 < idade <= 17:
        if imc <= 14:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mDESNUTRIDO!!!\033[m')
        elif 14 < imc <= 15.7:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mSUBDESNUTRIDO!!\033[m')
        elif 15.7 < imc <= 17.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;34mABAIXO DO PESO!\033[m')
        elif 17.3 < imc <= 24.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;32mPESO NORMAl\033[m')
        elif 24.8 < imc <= 27.9:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;33mLEVEMENTE ACIMA DO PESO!\033[m')
        elif 27.9 < imc <= 32.5:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;33mSOBREPESO!!\033[m')
        elif 32.5 < imc <= 36.4:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 1!!!\033[m')
        elif 36.4 < imc <= 38.7:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 2!!!\033[m')
        elif 38.7 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 3 / MÓRBIDA!!!\033[m!!!')
        else:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                f'\033[1;4;31mOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE!!!!!\033[m')
            print('Claro se você conseguir...')
            print('Quer q eu chame um guincho..?')

    else:
        if imc <= 16:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mDESNUTRIDO!!!\033[m')
        elif 16 < imc <= 17:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mSUBDESNUTRIDO!!\033[m')
        elif 17 < imc <= 20.7:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;34mABAIXO DO PESO!\033[m')
        elif 20.7 < imc <= 26.4:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;32mPESO NORMAl\033[m')
        elif 26.4 < imc <= 27.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;33mLEVEMENTE ACIMA DO PESO!\033[m')
        elif 27.8 < imc <= 31.1:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;33mSOBREPESO!!\033[m')
        elif 31.1 < imc <= 35.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 1!!!\033[m')
        elif 35.8 < imc <= 40:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 2!!!\033[m')
        elif 40 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                  f'\033[1;4;31mOBESIDADE GRAU 3 / MÓRBIDA!!!\033[m')
        else:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n'
                f'\033[1;4;31mOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE!!!!!\033[m')
            print('Claro se você conseguir...')
            print('Quer q eu chame um guindaste..?')

# CONTA PARA O SEXO FEMININO

if sexo == 'feminino':

    if idade < 5:
        print('Ainda não temos disponível')

    elif 5 <= idade <= 11:
        if imc <= 10:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nDESNUTRIDO!!!')
        elif 10 < imc <= 12.9:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSUBDESNUTRIDO!!')
        elif 12.9 < imc <= 14:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nABAIXO DO PESO!')
        elif 14 < imc <= 20.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nPESO NORMAl')
        elif 20.3 < imc <= 22:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n LEVEMENTE ACIMA DO PESO!')
        elif 22 < imc <= 24.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSOBREPESO!!')
        elif 24.3 < imc <= 25.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 1!!!')
        elif 25.8 < imc <= 27:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 2!!!')
        elif 27 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 3 / MÓRBIDA!!!')
        else:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE')
            print('Claro se você conseguir...')
            print('Quer q eu chame uma carriola?..?')

    elif 11 < idade <= 14:
        if imc <= 12:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nDESNUTRIDO!!!')
        elif 12 < imc <= 14.2:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSUBDESNUTRIDO!!')
        elif 14.2 < imc <= 15.5:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nABAIXO DO PESO!')
        elif 15.6 < imc <= 23.1:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nPESO NORMAl')
        elif 23.1 < imc <= 24.6:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n LEVEMENTE ACIMA DO PESO!')
        elif 24.6 < imc <= 27.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSOBREPESO!!')
        elif 27.8 < imc <= 29:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 1!!!')
        elif 29 < imc <= 31.1:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 2!!!')
        elif 31 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 3 / MÓRBIDA!!!')
        else:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE')
            print('Claro se você conseguir...')
            print('Quer q eu chame um caminhão..?')

    elif 14 < idade <= 17:
        if imc <= 13:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nDESNUTRIDO!!!')
        elif 13 < imc <= 14.7:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSUBDESNUTRIDO!!')
        elif 14.7 < imc <= 16.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nABAIXO DO PESO!')
        elif 16.3 < imc <= 24.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nPESO NORMAl')
        elif 24.8 < imc <= 25.9:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n LEVEMENTE ACIMA DO PESO!')
        elif 25.9 < imc <= 29.5:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSOBREPESO!!')
        elif 29.5 < imc <= 33.4:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 1!!!')
        elif 33.4 < imc <= 36.7:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 2!!!')
        elif 36.7 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 3 / MÓRBIDA!!!')
        else:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU LUCAS / CORRE PARA O HOSPITAL SE NÂO TU MORRE')
            print('Claro se você conseguir...')
            print('Quer q eu chame um guincho..?')

    else:
        if imc <= 16:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nDESNUTRIDO!!!')
        elif 16 < imc <= 17:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSUBDESNUTRIDO!!')
        elif 17 < imc <= 19.1:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nABAIXO PESO!')
        elif 19.1 < imc <= 25.8:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nPESO NORMAl')
        elif 25.8 < imc <= 27.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \n LEVEMENTE ACIMA DO PESO!')
        elif 27.3 < imc <= 32.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nSOBREPESO!!')
        elif 32.3 < imc <= 35.3:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 1!!!')
        elif 35.3 < imc <= 38.5:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 2!!!')
        elif 38.5 < imc <= 200:
            print(f'{nomeSplt[0]} seu imc é aproximadamente {imc:.1f} \nOBESIDADE GRAU 3 / MÓRBIDA!!!')
        elif imc > 200:
            print(
                f'{nomeSplt[0]} seu imc é aproximadamente {imc:.2} \nOBesIDADE GRAU X / CORRE PARA O HOSPITAL SE NÂO TU MORRE')
            print('Claro se você conseguir...')
            print('Quer q eu chame um guindaste..?')





