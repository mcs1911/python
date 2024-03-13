from random import randint

print('-----------------')
print('SORTEIO INVERTIDO')
print('-----------------')

print('Sorteando 10 valores...')
pos = 9
lista = list()
for i in range(10):
    num = randint(1,10)
    lista.append(num)

for a, b in enumerate(lista):
    print(f'[{a}]:{b}', end=' ')
    
print('\nMostrando a sequência invertida')
# print(lista[::-1])
 
for a, b in enumerate(lista[::-1]):
    print(f'[{pos}]:{b}', end=' ')
    pos -= 1
    
#for j in range(9, 0, -1):
#    print(f'[{j}]: ',) 
   