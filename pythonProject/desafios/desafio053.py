frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
fraseInv = frase[::-1]

if frase.upper() == fraseInv:
    print(f'As frases {frase} e {fraseInv} SÃO palíndromas!')
else:
    print(f'As frases {frase} e {fraseInv} NÃO SÃO palíndromas!')