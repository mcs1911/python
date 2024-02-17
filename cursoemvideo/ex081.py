lista = list()
op = 'S'
soma = 0
cinco = ' '

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    op = input('Deseja continuar? [S/N] ').upper()
    while op not in 'SN':
        op = input('Deseja continuar? [S/N] ').upper()
    soma += 1
    if op == 'N':
        break
    if 5 in lista:
        cinco = 'A lista possui o valor 5'
    else:
        cinco = '5 Não está na lista'

lista.sort(reverse=True)

print(f'A lista é composta de {soma} números')
print(lista)
print(f'{cinco}')

'''
para saber quantos elementos era só ter usado o {len(lista)}
'''