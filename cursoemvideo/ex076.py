listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)

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