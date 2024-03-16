from random import randint

dic = dict()

for i in range(0, 4):
    dado = randint(1, 6)
    dic[i] = dado
    
print(dic)

rank = sorted(dic.items(), key=lambda x: x[1], reverse=True)

print(rank)

for k, (jogador, resultado) in enumerate(rank, start=1):
    print(f'{k}º lugar: Jogador {jogador} tirou {resultado}')

'''

for j in range(0, len(dic)):
    print(f'O jogador {j} tirou {dic[j]}')

rank = sorted(dic.values(), reverse= True)

print(rank)    

for k in range(0, len(rank)):
    print(f' {k + 1}º Lugar: {rank[k]}')
    

aux = 0
for k in range(0, len(dic) - 1):
    for m in range(1, len(dic)):
        if dic[k] < dic[m]:
            aux = dic[k]
            dic[k] = dic[m]
            dic[m] = aux

'''
         