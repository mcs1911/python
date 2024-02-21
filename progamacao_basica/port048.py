print('DESCOBRINDO SE UM NÚMERO É PRIMO:')

div = 0
num = int(input('Digite um número: '))
for n in range(1, num + 1):
    if num % n == 0:
        print(f'[{n}]', end= ' ')
        div += 1
    else:
        print(f'{n}', end= ' ')
print(f'\nO número {num} foi divisível {div} vezes')
if div > 2:
    print('Logo, ele NÃO É PRIMO!')
else:
    print('Ele é PRIMO!!')
          