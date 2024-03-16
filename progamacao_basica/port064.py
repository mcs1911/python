from random import randint

matriz = list()
for row in range(0, 4):
    linha = []
    for column in range(0, 4):
        num = randint(0, 10)
        linha.append(num)
    matriz.append(linha)
    
for elem in matriz:
    print(elem)
    
print('-' * 35)

for line in range(0, 4):
    print(f'Somando a linha {line}: ', end=' ')
    soma = 0
    for col in range(0, len(matriz)):
        print(f'{matriz[line][col]}', end=' ')
        soma += matriz[line][col]
    print(f'= {soma}')

