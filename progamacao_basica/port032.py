cont = 1
impar = par = 0
while cont <= 5:
    val = int(input(f' Digite o {cont}º valor: '))
    if val % 2 == 0:
        par += val
    else:
        impar += val
    cont += 1
print(f'Somando todos os valores pares, temos {par}.')
print(f'Somando todos os valores ímpares, temos {impar}.')
