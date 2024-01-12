r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da terceira reta: '))

if (r1 + r2) < r3 or (r2 + r3) < r1 or (r3 + r1) < r2:
    print(f'Essas retas NÃO podem formar um triângulo! :(')
else:
    print(f'Essas retas formam um triângulo! :D')
