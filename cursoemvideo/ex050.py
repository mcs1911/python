s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o valor {c}: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A soma dos {cont} valores pares digitados é: \033[35m{s}\033[m')