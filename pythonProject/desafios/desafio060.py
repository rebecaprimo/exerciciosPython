numero = int(input('Digite o número para calcular o fatorial: '))
contador = numero
fatorial = 1

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
