num = str(input('Digite um número inteiro de 0 a 9999: '))

if len(num) == 1:
    print(f'O número é constituído por: \nUnidade {num[0]}')
elif len(num) == 2:
    print(f'O número é constituído por: \nDezena: {num[0]}\nUnidade: {num[1]}')
elif len(num) == 3:
    print(f'O número é constituído por: \nCentena: {num[0]}\nDezena: {num[1]}\nUnidade: {num[2]}')
else:
    print(f'O número é constituído por: \nMilhar: {num[0]}\nCentena: {num[1]}\nDezena: {num[2]}\nUnidade: {num[3]}')
