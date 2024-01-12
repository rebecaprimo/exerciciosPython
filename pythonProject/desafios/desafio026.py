frase = str(input('Digite uma frase aqui: '))
frase = frase.lower().strip()

print(f'Na frase existem {frase.count('a')} A(s).')
print(f'O primeiro A aparece na posição {frase.find('a') + 1}') # +1 pq a primeira posição é zero
print(f'O último A aparece na posição {frase.rfind('a') + 1}') #