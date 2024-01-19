from random import randrange

n = randrange(0, 5)
num = int(input('Digite um número de 0 a 5: '))
print(f'Seu número escolhido foi: {num}')
if n == num:
    print('Você ACERTOU!!!')
else:
    print('Você ERROU!!! ')
print('--FIM DO JOGO---')

'''
from random import randint
from time import sleep
computador = radint(0, 5)
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! Eu pensei no número {computador} e você digitou {jogador}')
'''