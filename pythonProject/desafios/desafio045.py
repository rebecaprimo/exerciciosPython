from random import randint

print('Vamos jogar pedra, papel, tesoura?? ')
itens = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input('Digite qual sua opção: \n[0] - Pedra\n[1] - Papel\n[2] - Tesoura\n-> '))

computador = randint(0, 2)

if computador == escolha:
    print(f'Empatamos!\nMinha escolha: {itens[computador]}\nSua escolha: {itens[jogador]}')

