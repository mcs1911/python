print('-' * 35)
print('DESEMPENHO DO JOGADOR')
print('-' * 35)

dic = {}
soma = 0
nome = input('Nome: ')
dic['nome'] = nome

qts = int(input('Quantas partidas? '))

lista = []
for i in range(0, qts):
    gol = int(input(f'Quantos gols na partida {i + 1}: '))
    soma += gol
    lista.append(gol)
  
dic['gols'] = lista
dic['total'] = soma

print(dic)

print('-' * 35)

print(f'O campo nome tem valor {dic["nome"]}')
print(f'O campo gols tem valor {dic["gols"]}')
print(f'O campo total tem valor {dic["total"]}')

print('-' * 35)

print(f'O jogador {dic["nome"]} jogou {qts} patidas:')
for k in range(0, len(dic["gols"])):
    print(f'Na partida {k + 1}, fez {dic["gols"][k]} gols.')
    