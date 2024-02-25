print('Andares do Triângulo')

andar = int(input('Quantos andares? '))

'''
for i in range (1):
    for e in range(andar + 1):
    print('*' * e)
'''

for i in range(andar):
    for f in range(i + 1):
        print('*', end=' ')
    print()