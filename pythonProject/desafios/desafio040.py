nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Média: {media:.2f}\nInfelizmente, você está abaixo da média e reprovado! :(')
elif media >= 5.0 and media <= 6.9:
    print(f'Média: {media:.2f}\nVocê está em recuperação! :/')
else:
    print(f'Média: {media:.2f}\nParabéns!! Você foi aprovado :D')
