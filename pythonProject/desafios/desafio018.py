import math
angulo = float(input('Digite aqui seu ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Os seno, cosseno e tangente de {angulo}, são, respectivamente: \nSeno -> {seno:.2f}\nCosseno -> {cosseno:.2f}\nTangente -> {tangente:.2f}')