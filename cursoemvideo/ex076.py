'''
preço = produto = ' '

for n in listagem:
    if listagem.index(n) % 2 == 0:
        produto = n
    else:
        preço = n
    print(f'{produto}......R$ {preço}')
    

produtos = []
preços = []

for n in listagem:
    if listagem.index(n) % 2 == 0:
        produtos.append(n)
    else:
        preços.append(n)

n = 0
while n < 5:
    print(f'{produtos.index[n]}......R$ {preços.index[n]}')
    n += 1

'''

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)

print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for i in range(0, len(listagem), 2):
    produto = listagem[i]
    preço = listagem[i + 1]
    print(f'{produto}......R$ {preço}')

#PROFESSOR 
print('-' * 340)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)