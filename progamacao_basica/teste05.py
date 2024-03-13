from random import randint

lista = []
maior = menor = 0

for i in range(10):
    num = randint(0, 10)
    lista.append(num)

for j in range(0, len(lista)):
    if j == 0:
        maior = lista[j]
        menor = lista[j]
    else:
        if lista[j] > maior:
            maior = lista[j]
        if lista[j] < menor:
            menor = lista[j]

print(lista)
print(f'O menor valor encontrado na lista foi {menor}')
print(f'O maior valor encontrado na lista foi {maior}')