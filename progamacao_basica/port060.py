from random import randint

print('Sorteando 10 valores: ')

lista = []
soma = cont = maior = cont_maior = 0
for i in range(10):
    num = randint(0, 5)
    lista.append(num)

print(lista)

print('--------------------------------')
print('Analisando os valores sorteados:')

print('\tValores pares nas posições: ', end=' ')
for j in range(0, len(lista)):
    if lista[j] % 2 == 0:
        soma += lista[j]
        print(j, end=' ')
        
print(f'\n\tSoma dos valores pares: {soma}')

print('--------------------------------')

print('\tValores ímpares nas posições: ', end=' ')
for h in range(0, len(lista)):
    if lista[h] % 2 != 0:
        cont += 1
        print(h, end=' ')
        
print(f'\n\tQuantidade de valores ímpares: {cont}')

print('--------------------------------')

print('\tMaior valor sorteado: ', end=' ')
for k in range(0, len(lista)):
    if k == 0:
        maior = lista[k]
    else:
        if lista[k] > maior:
            maior = lista[k]
print(maior, end='')

print(f'\n\tO maior valor foi encontrados nas posições: ', end=' ')
for l in range(0, len(lista)):
    if lista[l] == maior:
        cont_maior += 1
        print(l, end=' ')

print(f'\n\tTotal de ocorrências: {cont_maior}')