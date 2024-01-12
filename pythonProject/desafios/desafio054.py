from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input(f'{c}. Qual seu ano de nascimento? '))
    if anoAtual - ano < 21:
        menor += 1
    else:
        maior += 1

print(f'Das pessoas entrevistadas, {menor} são menores de idade e {maior} são maiores!')