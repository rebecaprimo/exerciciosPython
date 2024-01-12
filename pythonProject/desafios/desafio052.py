numero = int(input('Digite um número: '))
divisiveis = 0

for i in range(1, numero+1):
    if numero % i == 0:
        print('\033[33m', end=' ')
        divisiveis += 1
    else:
        print('\033[31m', end=' ')
if divisiveis == 2:
    print(f'O número {numero} É PRIMO!!')
else:
    print(f'O número {numero} NÃO É PRIMO!!')
print(f'Foi divisível {divisiveis} vezes.', end=' ')