from random import randint

print('-=-' * 20)
print('JOGO DE ADIVINHAÇÃO')
print('-=-' * 20)
print('''Regra do jogo: O computador vai pensar em um número de 0 a 10 e você precisa adivinhar em qual número ele pensou...''')
print('-=-' * 20)

comp = randint(0, 10)
tentativas = 1
jogador = int(input('Em qual número o computador pensou? '))
while comp != jogador:
    print('Você \033[31mErrou!!\033[mTente novamente!')
    jogador = int(input('Tente outro número: '))
    tentativas += 1
print(f'\033[34mVocê ACERTOU!\033[m O número escolhido pelo computador foi {comp}')
print(f'Você precisou de \033[33m{tentativas}\033[m tentativas!')
