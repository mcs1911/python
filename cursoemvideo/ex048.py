soma = 0
cont = 0
for c in range(1, 501, 2): # para economizar processamento - assim conseguimos os números ímpares
    if c % 3 == 0:
        soma += c
        cont = cont + 1 # cont += 1
print(f'A soma de todos os {cont} valores é igual a: {soma}')