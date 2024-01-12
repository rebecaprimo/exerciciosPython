primeiroTermo = int(input('Digite o primeiro termo da sua P.A.: '))
razao = int(input('Qual a razão da sua P.A.? '))
decimo = primeiroTermo + (10 - 1) * razao #10 - 1 pq eu quero os dez primeiros termos da P.A

for numero in range(primeiroTermo, decimo + razao, razao):
    print(f'{numero}', end=' ➤ ')
print('P.A finalizada!')