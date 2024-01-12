sexo = str(input('Digite seu sexo [F]/[M]: ')).strip().upper()[0] #pega apenas a primeira letra do input

while sexo not in 'MF':
    print('Opção inválida!')
    sexo = str(input('Digite seu sexo [F]/[M]: ')).strip().upper()[0]

print('Obrigada por responder!')