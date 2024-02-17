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

'''
SOLUÇÃO DO PROF:

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista [c] < menor:
            menor = lista[c]

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
        
MESMA COISA PARA O MENOR... ELE FEZ UM FOR ENTRE OS PRINTS
    
'''