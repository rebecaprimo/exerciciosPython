from datetime import date
anoAtual = date.today().year
ano = int(input('Qual seu ano de nascimento? '))

idade = anoAtual - ano
inicio = 'Segundo a Confederação Nacional de Natação, sua categoria é:'

if idade <= 9:
    print(f'{inicio} Mirim')
elif idade <= 14:
    print(f'{inicio} Infantil')
elif idade <= 19:
    print(f'{inicio} Junior')
elif idade <= 25:
    print(f'{inicio} Sênior')
else:
    print(f'{inicio} Master')