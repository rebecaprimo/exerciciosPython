cidade = str(input('Digite aqui o nome da cidade: '))

santo = cidade.upper()
santo = santo.split()

if santo[0] == 'SANTO':
    print(f'A cidade que você digitou começa com Santo: {cidade}')
else:
    print(f'A cidade que você digitou NÃO começa com Santo: {cidade}')