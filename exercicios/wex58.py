# EXERCÍCIO 58

''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''

print('----INÍCIO---')

import random

tentativas = 0
computador = random.randint(0,10)
jogador = 11

while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1

print(f'\033[01;32mPARABÉNS!!! Você acertou...\033[m')
print(f'Mas precisou de \033[01;31m{tentativas} tentativas\033[m')

print('---FIM---')
