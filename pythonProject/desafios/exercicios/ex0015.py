diasAlugado = int(input('Insira a quantidade de dias que você ficará com o carro: '))
kmRodado = float(input('Quantos KM você rodou? '))

precoFinal = (diasAlugado*60) + (kmRodado*0.15)

print(f'O valor total do aluguel ficou {precoFinal} reais!')