n = 3
matriz = []

for row in range(n):
    linha = [ ]
    for col in range(n):
        linha.append(int(input(f'Número ({row}, {col}): ')))
    matriz.append(linha)
    print()

for lista in matriz:
    print(lista)
    
print('\n')

n = 3
matriz = []

for row in range(n):
    linha = [ ]
    for col in range(n):
        linha.append([int(input(f'Número ({row}, {col}): '))])
    matriz.append(linha)
    print()

for lista in matriz:
    print(lista)