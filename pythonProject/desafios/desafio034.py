salario = float(input('Digite seu salário: '))

if salario >= 1250.00:
    novoSalario = salario * 0.1
    print(f'O aumento do seu salário vai ser de 10%: R${novoSalario:.2f}!\nNovo salário: R${salario + novoSalario:.2f}')
else:
    novoSalario = salario * 0.15
    print(f'O aumento do seu salário vai ser de 15%: R${novoSalario:.2f}!\nNovo salário: R${salario + novoSalario:.2f}')