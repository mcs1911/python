print('-' * 35)
print('DESEMPENHO DO JOGADOR')
print('-' * 35)

dic = {}
soma = 0
jogadores = []
lista = []

while True:
    dic.clear()
    dic['nome'] = input('Nome: ')

    qts = int(input('Quantas partidas? '))

    lista.clear()
    for i in range(0, qts):
        gol = int(input(f'Quantos gols na partida {i + 1}: '))
        soma += gol
        lista.append(gol)
    
    dic['gols'] = lista
    dic['total'] = soma

    jogadores.append(dic.copy())
    while True:
        op = input('Quer continuar? [S/N]').upper()[0]
        if op in 'NS':
            break
        print('ERRO! Responda apenas S ou N')
    if op == 'N':
        break
    

    print('-' * 35)
    
print(jogadores)

print('cod ', end='')
for i in dic.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
'''

print(f'O campo nome tem valor {dic["nome"]}')
print(f'O campo gols tem valor {dic["gols"]}')
print(f'O campo total tem valor {dic["total"]}')

print('-' * 35)

print(f'O jogador {dic["nome"]} jogou {qts} patidas:')
for k in range(0, len(dic["gols"])):
    print(f'Na partida {k + 1}, fez {dic["gols"][k]} gols.')
    
'''