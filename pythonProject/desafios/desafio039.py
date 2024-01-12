from datetime import date #importando o módulo de datas

nasc = int(input('Digite o ano que você nasceu: '))
anoAtual = date.today().year #armazena o ano vigente
idade = anoAtual - nasc
if idade < 18:
    print(f'Em {anoAtual} você tem {idade} anos.')
    print(f'Você ainda não tem idade suficiente para se alistar!')
elif (anoAtual - nasc) > 18:
    print(f'Em {anoAtual} você tem {idade} anos.')
    print(f'Você já passou da idade para se alistar, caso não tenha se aplicado, regularize sua situação!')
else:
    print(f'Em {anoAtual} você tem {idade} anos.')
    print(f'Você tem 18 anos e precisa se alistar antes do final do ano! :)')
