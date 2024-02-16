lista = list()


for e in range(5):
    valor = int(input(f'Qual valor você deseja colocar na posição {e}: '))
    lista.append(valor)

maior = menor = valor
pos_maior = pos_menor = 0

for pos, valor in enumerate(lista):
    if valor > maior:
        maior = valor
        pos_maior = pos
    elif valor < menor:
        menor = valor
        pos_menor = pos

print(f'O maior valor digitado é {maior} e aparece nas posições {pos_maior}')

print(f'O maior valor digitado é {menor} e aparece nas posições {pos_menor}')

    