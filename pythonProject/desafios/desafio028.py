import random

num = random.randint(0, 5)
print(f'='*10, 'ACERTANDO O NÚMERO', '='*10)

palpite = int(input('Qual número o computador está pensando? '))
print('PROCESSANDO....')
sleep(2) #cria uma pausa de 2 segundos
if num == palpite:
    print(f'Parabéns, você acertou!! O número era: {num}')
else:
    print(f'Você errou :(( O número era: {num}')
