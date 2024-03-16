from random import randint

matriz = []
soma = acima = abaixo = 0

for r in range(5):
    lista = list()
    for c in range(5):
        num = randint(0, 10)
        soma += num
        lista.append(num)
    matriz.append(lista)

for linha in matriz:
    print(linha)

media = soma / len(matriz) ** 2

print('-' * 35)
print(f'A média dos valores gerados é {media :.2f}')
print('-' * 35)

print('Na segunda linha, os valores acima da média são:')
for col in range(0, len(matriz)):
    if matriz[1][col] >= media:
        print(f'[{1}][{col}] = {matriz[1][col]}')