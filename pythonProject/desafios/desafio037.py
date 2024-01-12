numero = int(input('Digite um número inteiro: '))
base = int(input(f'Insira qual para qual base você deseja converter o número {numero}:\n1 - Base binária\n2 - Base octal\n3 - Base hexadecimal\n -> '))

if base == 1:
    print(f'A representação binária do número {numero} é: {bin(numero)[2:]}')
elif base == 2:
    print(f'A representação octal do número {numero} é: {oct(numero)[2:]}') #[2:] mostra os caracteres a partir do caractere 2
elif base == 3:
    print(f'A representação hexadecimal do número {numero} é: {hex(numero)[2:]}')
else:
    print('Essa opção não está disponível!')
