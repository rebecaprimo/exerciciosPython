soma = 0

for digite in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero

print(f'A soma de todos os números pares digitados foi: {soma}!')
