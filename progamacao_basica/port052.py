
num = int(input('Quantos andares? '))

for i in range(num):
    for j in range(i):
        print(' ', end= ' ')
    for f in range(i, num):
        print('*', end=' ')
    for t in range(i, num - 1):
        print('*', end=' ')
    print()