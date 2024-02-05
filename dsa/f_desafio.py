lista = [5, 2, 5, 2, 2]
lista_2 = ['x']

'''
for i in lista:
    for f in lista_2:
        print(f'{f * i}')

for i in lista:
    print('x' * i)
'''
for i in lista:
    output = ''
    for count in range(i):
        output += 'x'
    print(output)