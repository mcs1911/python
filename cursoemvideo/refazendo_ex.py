produtos = ('Caderno', 'R$ 20,99', 'Mochila', 'R$ 120,00', 'Lápis', 'R$ 2,50', 'Caneta', 'R$ 3,50')
print('-------------------------')
print('Listagem de Preços')
print('-------------------------')
for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]

    print(f'{produto.ljust(10)}\t{preco}')

'''

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