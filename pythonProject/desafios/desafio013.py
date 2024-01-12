print(f'='*10, 'CALCULADORA DE SÁLARIOS', '='*10)

salario = float(input('Digite aqui o seu salário: '))
bonus = salario * 0.15
final = salario + bonus

print(f'Parabéns! Seu novo salário é: R${final}!')
