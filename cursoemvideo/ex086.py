# MATRIZ 3x3

matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        num = int(input(f'Digite o número ({l}, {c}): '))
        linha.append(num)
    matriz.append(linha)
        
print('Matriz 3x3')
for linha in matriz:
    print(linha)
