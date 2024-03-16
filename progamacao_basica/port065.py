from random import randint

matriz = []
for r in range(4):
    lista = list()
    for c in range(4):
        num = randint(0, 10)
        lista.append(num)
    matriz.append(lista)
    
for line in matriz:
    print(line)

for col in range(0, len(matriz)):
    print(f'Somando a coluna {col}: ', end=' ')
    soma = 0
    for linha in range(0, len(matriz)):
        print(f'{matriz[linha][col]}', end=' ')
        soma += matriz[linha][col]
    print(f'= {soma}')
        