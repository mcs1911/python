dic = {}

nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))

dic['nome'] = nome
dic['media'] = media
print(f'Nome é igual a {dic['nome']}')
print(f'Média é igual a {dic['media']}')

if media >= 7:
    situ = 'APROVADO'
else:
    situ = 'REPROVADO'

dic['situação'] = situ

print(f'Situação é igual a \033[1;32m{dic['situação']}\033[m')

print(dic)

for k, v in dic.items():
    print(f' - {k} é igual a {v}')