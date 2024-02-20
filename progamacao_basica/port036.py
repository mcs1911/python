from random import randint

maiores = div = 0
cont = 1
num = int(input('Quantos valores você deseja sortear? '))
print(f'Sorteando {num} números:', end= ' ')
while cont <= num:
    x = randint(0, 10)
    print(f'{x}...', end=' ')
    cont += 1 
    if x > 5:
        maiores += 1
    elif x % 3 == 0:
        div += 1
print('\n--------------------------')
print(f'Dos {num} números sorteados:')
print(f'{maiores} são maiores que 5')
print(f'{div} são divisíveis por 3')