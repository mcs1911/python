'''
matriz1 = [
    [2, 6, 3],
    [9, 5, 4],
    [1, 0, 8]
]

for i in matriz1:
    print(matriz1.index(i))

for i in matriz1:
    print(i)

'''

r = int(input('Linhas: '))
c = int(input('Colunas: '))


for i in range(r):
    for j in range(c):
        print(f'({i},{j})', end=' ')
    print()

print('\n')

for i in range(r):
    for j in range(c):
        print(f'0', end=' ')
    print()
    
print('\n')

for i in range(r):
    for j in range(c):
        if i == j:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()

print('\n')

for i in range(r):
    for j in range(c):
        if i >= j:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()

print('\n')

for i in range(r):
    for j in range(c):
        if i <= j:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()

print('\n')

for i in range(r):
    for j in range(c):
        if i == 0:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()