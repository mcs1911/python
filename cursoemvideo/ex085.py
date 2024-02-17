lista = [[],[]]

for num in range(7):
    num = int(input(f'Número {num}: '))
    if num % 2 == 0:
        lista[0].append(num)
        
    else:
        lista[1].append(num)

ordem = [sorted(lista[0])] + [sorted(lista[1])]

print(ordem)
print(f'Lista dos pares: {ordem[0]}')
print(f'Lista dos ímpares: {ordem[1]}')