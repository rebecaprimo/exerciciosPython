from datetime import date

ano = int(input('Digite aqui um ano que você quer analisar, coloque 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto, tem 366 dias!')
else:
    print(f'O ano {ano} NÃO é bissexto, tem apenas 365 dias!')
    