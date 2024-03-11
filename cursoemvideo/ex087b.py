'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''
som_par = soma = maior = 0
dados = list()
matriz = []

for r in range(3):
    for c in range(3):
        num = int(input(f'Digite o valor [{r},{c}]: '))
        dados.append(num)
        if num % 2 == 0:
            som_par += num 
    matriz.append(dados[:])
    if dados[r:3]:
        soma += num
    dados.clear()
    print()

for i in matriz[1]:
    if i == 0:
        maior = i
    else:
        if i > maior:
            maior = i
            
for linha in matriz:
    print(linha)
print(f'A soma de todos os valores pares digitados é {som_par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')

