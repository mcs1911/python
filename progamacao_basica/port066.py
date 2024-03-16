matriz = []
maior = 0
for r in range(3):
    lista = list()
    for c in range(3):
        num = int(input(f'Digite um valor para a posição [{r}][{c}]: '))
        lista.append(num)
    matriz.append(lista)

for linha in matriz:
    print(linha)
    
print('Procurando pelo maior valor')

for l in range(0, len(matriz)):
    for n in range(0, len(matriz)):
        if n == 0:
            maior = matriz[l][n]
        else:
            if matriz[l][n] > maior:
                maior = matriz[l][n]

print(f'Maior valor encontrado na matriz: {maior}')

print(f' Valor {maior} encontrado nas posições: ')
for k in range(0, len(matriz)):
    for m in range(0, len(matriz)):
        if matriz[k][m] == maior:
            print(f'[{[k]}][{[m]}] ->', end=' ')

print('FIM')