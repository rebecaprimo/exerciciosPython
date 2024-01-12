print(f'='*10, 'PROMOÇÕES', '='*10)

preco = float(input('Digite o preço do produto: '))
desc = preco * 0.05
final = preco - desc

print(f'O valor do item com desconto é R${final:.2f}!')