nome = str(input('Digite seu nome completo: '))

maius = nome.upper()
#print(maius.find('SILVA'))

if 'SILVA' in maius:
    print(f'Seu nome tem Silva: {nome}')
else:
    print(f'Seu nome NÃO tem Silva: {nome}')

