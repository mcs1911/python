'''
print('-=-' * 20)
print('VAMOS JOGAR JOKEMPO??')
print('-=-' * 20)

from random import choice
from time import sleep

jog = str(input('Pedra, papel ou tesoura? ')).lower()
if jog in ('pedra', 'papel', 'tesoura'):
    comp = choice(['pedra', 'papel', 'tesoura'])
    print('Pedra, papel ou tesssssooooura...')
    print('-=-'* 20)
    sleep(1)
    if comp == 'pedra' and jog == 'tesoura':
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;31mVocê PERDEU!')
    elif comp == 'tesoura' and jog == 'papel':
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;31mVocê PERDEU!')
    elif comp == 'papel' and jog == 'pedra':
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;31mVocê PERDEU!')
    elif comp == jog:
        print('Temos um empate, jogue outra vez!')
        jog = str(input('Pedra, papel ou tesoura? ')).lower()
        if jog in ('pedra', 'papel', 'tesoura'):
            comp = choice(['pedra', 'papel', 'tesoura'])
            print('Pedra, papel ou tesssssooooura...')
            print('-=-'* 20)
            sleep(3)
            if comp == 'pedra' and jog == 'tesoura':
                print(f'Computador: {comp} \nJogador: {jog}')
                print('\033[1;31mVocê PERDEU!')
            elif comp == 'tesoura' and jog == 'papel':
                print(f'Computador: {comp} \nJogador: {jog}')
                print('\033[1;31mVocê PERDEU!')
            elif comp == 'papel' and jog == 'pedra':
                print(f'Computador: {comp} \nJogador: {jog}')
                print('\033[1;31mVocê PERDEU!')
            else:
                print(f'Computador: {comp} \nJogador: {jog}')
                print('\033[1;32mVocê GANHOU!')
    else:
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;32mVocê GANHOU!')
else:
    print('Jogada inválida!')

print('---FIM DO JOGO---') '''

print('-=-' * 20)
print('VAMOS JOGAR JOKEMPO??')
print('-=-' * 20)

from random import choice
from time import sleep

jog = str(input('Pedra, papel ou tesoura? ')).lower()
while True:
    comp = choice(['pedra', 'papel', 'tesoura'])
    print('Pedra, papel ou tesssssooooura...')
    print('-=-'* 20)
    sleep(1)
    if comp == 'pedra' and jog == 'tesoura':
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;31mVocê PERDEU!')
        break
    elif comp == 'tesoura' and jog == 'papel':
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;31mVocê PERDEU!')
        break
    elif comp == 'papel' and jog == 'pedra':
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;31mVocê PERDEU!')
        break
    elif comp == jog:
        print('Temos um empate, jogue outra vez!')
        jog = str(input('Pedra, papel ou tesoura? ')).lower()
    else:
        print(f'Computador: {comp} \nJogador: {jog}')
        print('\033[1;32mVocê GANHOU!')
        break

print('---FIM DO JOGO---')
