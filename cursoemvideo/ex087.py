#  EXERCÍCIO 87
'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''

matriz = []
soma = terceira = maior = 0

for r in range(3):
    linha = list()
    for c in range(3):
        n = int(input(f'Digite o número [{r}, {c}]:  '))
        linha.append(n)
        if n % 2 == 0:
            soma += n
        '''
        if n in linha[r][3]:
            terceira += n
        '''   
    matriz.append(linha)

for i in matriz[1]:
    if i == 0:
        maior = i
    else:
        if i > maior:
            maior = i

            
for linha in matriz:
    print(linha)
print()

print(f'A soma de todos os valores pares digitados é: {soma}')
print(f'A soma dos valores da terceira coluna é: {terceira}')
print(f'O maior valor da segunda linha é: {maior}')

#print(matriz[0][2])

'''
if n[r][3]:
    terceira += n
if n[2][c]:
    maior = n[2][0]
    if n > maior:
        maior = n
maior = max(linha[1])
'''