
'''
# EXERCÍCIO 63

Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

n0 = 0
n1 = 1

n = int(input('Quantos números vc quer ver? '))
print(f'{n0} -> {n1} -> ', end=' ')

for i in range(n):
    n2 = n0 + n1
    n0 = n1
    n1 = n2
    print(f'{n2} -> ', end=' ')
    
print('FIM')  

# Exercício: Calcular a média de notas de alunos
soma = cont = 0
notas = ['João', 8, 'Maria', 7, 'Carlos', 6, 'Ana', 9]

for i in range(0, len(notas), 2):
    nota = notas[i + 1]
    soma += nota
    cont += 1
    
# Outra opção de for seria começando com 1 range(1, len(notas), 2) e depois notas seria nota = notas[i]

print(soma)
media = soma / cont
print(media)

EXERCICIO 76

produtos = ('Caderno', 'R$ 20,99', 'Mochila', 'R$ 120,00', 'Lápis', 'R$ 2,50', 'Caneta', 'R$ 3,50')
print('-------------------------')
print('Listagem de Preços')
print('-------------------------')
for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]

    print(f'{produto.ljust(10)}\t{preco}')

for item in range(0, len(produtos), 2):
    print(produtos[item])
for item in range(1, len(produtos), 2):
    print(produtos[item])        


EXERCICIO 77

minha_tupla = ('Maça', 'Laranja', 'Pera', 'Uva', 'Melao')

for elemento in minha_tupla:
    elemento = elemento.lower() 
    print(f'A palavra \033[01;32m{elemento}\033[m possui as vogais: ', end=' ')
    for letra in elemento:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
    
EXERCICIO 78

lista = list()
maior = menor = pos_menor = pos_maior = 0 

for i in range(5):
    lista.append(int(input('Digite um número: ')))
    
for num in range(len(lista)):
    if num == lista[0]:
        maior = num
        menor = num
    else:
        if lista[num] > maior:
            maior = lista[num]
            pos_maior = num
        if lista[num] < menor:
            menor = lista[num]
            pos_menor = num
            
print(lista)
print(f'O maior número da lista é {maior} e está na posição {pos_maior}')
print(f'O menor número da lista é {menor} e está na posição {pos_menor}')
'''
#  EXERCÍCIO 83
'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.

lista = []
exp = input('Digite uma expressão matemática: ')

for i in exp:
    if i in '(':
        lista.append(i)
    if i in ')':
        try:
            lista.remove('(')
        except:
            print('Sua expressão tem parêntesis a mais. Tente novamente!')
            quit()
print(lista)
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão tem parêntesis a mais. Tente novamente!')
'''    
#  EXERCÍCIO 86
'''
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta


for r in range(3):
    for c in range(3):
        n = int(input(f'Digite o número da posição [{r},{c}]: '))
        print(f'{n}', end=' ')
    print()

'''

matriz = []

for r in range(3):
    linha = []
    for c in range(3):
        n = int(input(f'Digite o número [{r}, {c}]: '))
        linha.append(n)
    matriz.append(linha)
    
for linha in matriz:
    print(linha)
print()
    