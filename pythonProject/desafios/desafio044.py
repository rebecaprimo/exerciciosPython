preco = float(input('Insira o valor do produto que deseja comprar: R$'))

pagamento = int(input('Qual a forma de pagamento utilizada?\n1 - À vista (dinheiro)\n2 - À vista (crédito)\n3 - Até 2x no cartão\n4 - Até 3x ou mais no cartão\n-> '))

if pagamento == 1:
    desconto = preco * 0.10
    preco = preco - desconto
    print(f'O valor do seu produto com o desconto será R${preco:.2f}!')
elif pagamento == 2:
    desconto = preco * 0.05
    preco = preco - desconto
    print(f'O valor do seu produto com o desconto será R${preco:.2f}!')
elif pagamento == 3:
    print(f'Seu produto não terá desconto nessa modalidade!')
elif pagamento == 4:
    juros = preco * 0.20
    preco = juros + preco
    print(f'Seu produto terá juros de 20%. Preço final: R${preco:.2f}!')
else:
    print(f'Opção inválida!')