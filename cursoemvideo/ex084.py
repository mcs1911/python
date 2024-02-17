pessoas = []
dados = list()
pesadas = []
leves = list()
op = 'S'
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    op = input('Que continuar cadastrando? [S/N] ').upper()
    while op not in 'SN':
        op = input('Que continuar cadastrando? [S/N] ').upper()
    if op == 'N':
        break
    print('-' * 20)

for pessoa in pessoas:
    
    if pessoa[1] > 100:
        pesadas.append(pessoa[0])
    if pessoa[1] < 70:
        leves.append(pessoa[0])

print(pessoas)
print(f'Total de Cadastros: {len(pessoas)}')
print(f'As pesoas que pesam mais de 100kg: {pesadas}')
print(f'As pesoas que pesam menos de 70kg: {leves}')
    

'''
print(type(pessoas[1]))
'''