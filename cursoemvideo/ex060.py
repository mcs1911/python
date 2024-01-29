print('FATORIAL!!')

# WHILE
num = int(input('Digite um número: '))
c = num 
f = 1
print(f'Calculando {num}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1

print(f'{f}')

# Importando biblioteca

from math import factorial
n = int(input('Digite um número inteiro: '))
f = factorial(n)
print(f'O fatorial de {n} é igual a {f}')


# FOR

n = int(input('Digite um número: '))
f = 1
print(f'Calculando {n}! ', end='')
for n in range(n,0, -1):
    print(f'{n}', end='')
    print(f' x' if n > 1 else ' = ', end=' ')
    f *= n
print(f'{f}')