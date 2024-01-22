from random import randint
from time import sleep

print('Vamos jogar JoKenPo??')

op = ["Pedra", "Papel", "Tesoura"]
comp = randint(0,2)
computer = op[comp]

print('''Escolha uma opção: 
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')

jogador = int(input('Qual a sua escolha? '))

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
print('-=' * 20)

if jogador not in range(3): 
    print('Opção inválida! Digite um número válido \033[1;35mSergito!!\033[m')
else:
    print(f'Você escolheu \033[7m{op[jogador]}\033[m')    
    print(f'O computador jogou \033[7m{computer}\033[m')
    print('-=' * 20)
    if jogador == comp:
        print('\033[1;33mEMPATE.\033[m Tente Novamente!')
    elif jogador == 0 and comp == 1:
        print('\033[1;31mVOCÊ PERDEU!!!\033[m Tente Novamente!')
    elif jogador == 0 and comp == 2:
        print('\033[1;32mVOCÊ GANHOU!!!!\033[m')
    elif jogador == 1 and comp == 0:
        print('\033[1;31mVOCÊ PERDEU!!!\033[m Tente Novamente!')
    elif jogador == 1 and comp == 2:
        print('\033[1;32mVOCÊ GANHOU!!!!\033[m')
    elif jogador == 2 and comp == 0:
        print('\033[1;31mVOCÊ PERDEU!!!\033[m Tente Novamente!')
    elif jogador == 2 and comp == 1:
        print('\033[1;32mVOCÊ GANHOU!!!!\033[m')
    

print('---FIM DO JOGO---')
    
