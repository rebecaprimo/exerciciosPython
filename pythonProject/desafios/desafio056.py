mediaIdade = 0
mulherMenor = 0
homemMaior = 0
homemNome = ''

for c in range(1, 5):
    print('='*10, f'Pessoa - {c}', '='*10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F]/[M]: '))

    mediaIdade += idade
    if c == 1 and sexo.upper() == 'M':
        homemMaior = idade
        homemNome = nome
    if sexo.upper() == 'M' and homemMaior < idade:
        homemMaior = idade
        homemNome = nome
    if sexo.upper() == 'F' and idade < 20:
        mulherMenor += 1

print(f'\nNesse grupo tem {mulherMenor} mulher(es) com menos de 20 anos.')
print(f'A média de idade das pessoas é {mediaIdade / 4:.1f} anos.')
print(f'O nome do homem mais velho é {homemNome} é a idade dele é {homemMaior} anos.')