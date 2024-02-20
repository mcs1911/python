n = 3
matriz = []

for row in range(n):
    linha = [ ]
    for col in range(n):
        linha.append([int(input(f'Número ({row}, {col}): '))])
    matriz.append(linha)
    print()

print(*matriz, sep="\n")
