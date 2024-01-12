km = float(input('Digite aqui a distância em KM da sua viagem: '))

if km <= 200:
    preco = (km * 0.5)
    print(f'O preço da passagem vai ser R${preco:.2f}!')
else:
    preco = (km * 0.45)
    print(f'O preço da sua passagem vai ser R${preco:.2f}!')