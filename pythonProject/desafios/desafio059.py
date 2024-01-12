num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
opcao = 0
soma = num1 + num2
multiplicacao = num1 * num2

while opcao != 5:
    opcao = int(
        input('Digite uma opção: \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n-> '))
    if opcao == 1:
        print(f'A soma dos números é igual a {soma}')
    elif opcao == 2:
        print(f'A multiplição dos números é igual a {multiplicacao}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que {num2}')
        else:
            print(f'O número {num2} é maior que {num1}')
    elif opcao == 4:
        num1 = int(input('Insira um número: '))
        num2 = int(input('Insira outro número: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente :(')
    print('=-=' * 10)