valor = float(input('Insira o valor da casa que deseja financiar: R$'))
salario = float(input('Digite seu salário mensal: R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

totalPrestacao = anos * 12
valorPrestacao = valor / totalPrestacao
porcentagem = salario * 30 / 100

if porcentagem >= valorPrestacao:
    print(f'Infelizmente, o financiamento foi REPROVADO! :(\nValor da parcela: R${valorPrestacao:.2f}\n30% do salário: R${porcentagem:.2f}')
else:
    print(f'Parabéns, seu financiamento foi APROVADO! :D\nValor da parcela: R${valorPrestacao:.2f}\n30% do salário: R${porcentagem:.2f}')
