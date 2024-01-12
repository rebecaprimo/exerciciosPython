tabuada = int(input('Insira um número: '))

print(f'A tabuada do número {tabuada} é: ')
for numero in range(0, 11):
    print(f'{tabuada} X {numero} = {tabuada * numero}')

print('Gostou? Tente novamente!')