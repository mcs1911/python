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
O PROFESSOR RESOLVE POR MAIOR E MENOR PESO
AI NO CASO SERIA ANTES DE FAZER O APPEND PARA A LISTA PRINCIPAL (PESSOAS), FAZ-SE UMA VERIFICAÇÃO DE IF 

if len(pessoas) == 0:
    mai = menor = dados[1]
else:
    if dados[1] > mai:
        mai = dados[1]
    if dados[1] < men:
        men = dados[1]

Para printar o nome da pessoa ele fez um for e colocou um 
for p in pessoas:
    if p[1] == mai
        print(f'{p[1]}')
    
e um para o menor peso tb
'''
    

'''
print(type(pessoas[1]))
'''