from random import randint

numeros = []


def somaPar(lista):
    soma = 0
    for j in range(0, len(lista)):
        if lista[j] % 2 == 0:
            soma += lista[j] 
    print(f'A soma entre todos os valores pares é igual a \033[1;32m{soma}')


def sorteia():
    for i in range(5):
        n = randint(0, 10)
        numeros.append(n)
    print(f'Sorteando os valores da lista: {numeros}')


sorteia()
somaPar(numeros)

'''

for valor in numeros:
    if valor % 2 == 0:
        soma += valor

'''