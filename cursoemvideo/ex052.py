# Primo / 1 e por ele mesmo / n 
n = int(input('Digite um número: '))
print(f'{n} é um número primo?')
print('-=-' * 20)
tot = 0
for c in range(1, n + 1):
    if  n % c == 0:
        print(f'\033[1;33m', end='')
        tot += 1
    else:
        print(f'\033[1;31m', end='')
    print(f'{c}')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO.')
