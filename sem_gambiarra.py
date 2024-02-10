menor = None
print('Inicio')
for valor in [3, 9, 66, 1, 89, 54]:
    if menor is None:
        menor = valor
    elif valor < menor:
        menor = valor
    print(menor, valor)
print('Fim', menor)