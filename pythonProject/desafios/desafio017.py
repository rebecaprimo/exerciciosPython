from math import hypot
catetoA = float(input('Insira o valor do cateto adjacente: '))
catetoO = float(input('Insira o valor do cateto oposto: '))
#hipotenusa = (catetoA ** 2 + catetoO ** 2) ** (1/2)
hipotenusa = hypot(catetoA, catetoO)

print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
