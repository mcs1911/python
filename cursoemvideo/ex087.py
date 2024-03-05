#  EXERCÍCIO 87
'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''

matriz = []
soma = 0

for r in range(3):
    linha = list()
    for c in range(3):
        n = int(input(f'Digite o número [{r}, {c}]:  '))
        linha.append(n)
        if n % 2 == 0:
            soma += n
    matriz.append(linha)

for linha in matriz:
    print(linha)
print()

print(f'A soma de todos os valores pares digitados é: {soma}')