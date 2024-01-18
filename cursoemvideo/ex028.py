from random import randrange

n = randrange(0, 5)
num = int(input('Digite um número de 0 a 5: '))
print(f'Seu número escolhido foi: {num}')
if n == num:
    print('Você ACERTOU!!!')
else:
    print('Você ERROU!!!')
print('--FIM DO JOGO---')
