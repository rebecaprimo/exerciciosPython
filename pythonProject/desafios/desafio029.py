velocidade = float(input('Digite a velocidade do seu carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Atenção!!! Você foi multado em R${multa} :(')
else:
    print('Ufa! Sem multas para você :D')
