r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da terceira reta: '))

if (r1 + r2) < r3 or (r2 + r3) < r1 or (r3 + r1) < r2:
    print(f'\nEssas retas NÃO podem formar um triângulo! :(')
else:
    print(f'\nEssas retas formam um triângulo! :D')
    if r1 == r2 == r3:
        print(f'Esse triângulo será Equilátero (possui todos os lados iguais)!')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print(f'Esse triângulo será Isósceles (possui dois lados iguais)!')
    else:
        print(f'Esse triângulo será Escaleno (possui todos os lados diferentes)!')