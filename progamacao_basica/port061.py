print('-=' * 20)
print('Analisador de Nomes')
print('-=' * 20)

lista = []
tot_menor = tot_vogal = tot_s = 0
for i in range(6):
    nome = input(f'Nome para a posição [{i}]: ')
    lista.append(nome)

print('............Analisando............')

print('Nomes com menos de 6 letras:')

for j in range(0, len(lista)):
    if len(lista[j]) < 6:
        print(f'[{j}] = {lista[j]}', end=' ')
        tot_menor += 1

print(f'TOTAL = {tot_menor}')

print('-' * 40)
print('\nNomes que começam com vogal:')

for k in range(0, len(lista)):
    if lista[k][0] in 'AEIOUaeiou':
        print(f'[{k}] = {lista[k]}', end=' ')
        tot_vogal += 1

print(f'TOTAL = {tot_vogal}')

print('-' * 40)

print('\nNomes que possuem a letra "s":')

s = list()
for l in range(0, len(lista)):
    for letra in lista[l]:
        if letra in 'Ss' and lista[l] not in s:
            s.append(lista[l])
            tot_s += 1

for m in range(0, len(s)):
    print(f'[{m}] = {s[m]}', end=' ')
    
print(f'TOTAL = {tot_s}')

print('-' * 40)


