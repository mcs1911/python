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

'''
SOLUÇÃO DO PROFE:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:ˆ5}]', end='')
    print()
'''