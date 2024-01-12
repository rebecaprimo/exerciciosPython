from random import randint

num = randint(0, 10)
tentativa = 0
print(f'='*10, 'ACERTANDO O NÚMERO #2', '='*10)
palpite = int(input('Qual número estou pensando? '))

while not num == palpite:
    print('Errou! :(')
    palpite = int(input('Qual número estou pensando? '))
    tentativa += 1

print(f'Acertou depois de {tentativa} vezes :D Parabéns!')