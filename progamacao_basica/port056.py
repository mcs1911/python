val = int(input('Digite um valor: '))
pos = 0

lista = [val]

print('Vetor de Contagem de 5 em 5')

for _ in range(9):
    segundo_valor = lista[- 1] + 5
    lista.append(segundo_valor)
    
    
for valor in lista:
    print(f'{pos}:[{valor}] ->', end=' ')
    pos += 1
print('FIM')