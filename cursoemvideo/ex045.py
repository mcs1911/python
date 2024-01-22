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

print('---FIM DO JOGO---') 

def validar_jogada(jogada):
    jogadas_validas = ['pedra', 'papel', 'tesoura']
    return jogada in jogadas_validas


print('-=-' * 20)
print('VAMOS JOGAR JOKEMPO??')
print('-=-' * 20)

while True:
    jog = str(input('Pedra, papel ou tesoura? ')).lower()
    jog_valida = validar_jogada(jog)
    if jog_valida:
        break
    print('Jogada inválida!')

comp = choice(['pedra', 'papel', 'tesoura'])
print('Pedra, papel ou tesssssooooura...')
print('-=-' * 20)
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
elif comp == jog:
    print('Temos um empate, jogue outra vez!')
    jog = str(input('Pedra, papel ou tesoura? ')).lower()
    jog_valida = validar_jogada(jog)
    if jog_valida:
        break
    else:
        print('Jogada inválida!')
else:
    print(f'Computador: {comp} \nJogador: {jog}')
    print('\033[1;32mVocê GANHOU!')

print('---FIM DO JOGO---')
'''

