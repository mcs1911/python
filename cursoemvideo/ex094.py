pessoas = dict()
lista = []
soma = 0
while True:
    pessoas.clear()
    pessoas['nome'] = input('Nome: ')

    while True:
        pessoas['sexo'] = input('Sexo: [M/F]').upper()[0]
        
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M para masculino ou F para feminino')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        op = input('Quer continuar a cadastrar? [S/N] ').upper()[0]
        if op in 'NS':
            break
        print('ERRO! Responda S para sim e N para não')
    if op == 'N':
        break

print(lista)

print(f'Foram cadastradas {len(lista)} pessoas.')

media = soma / len(lista)
print(f'A média das idades do grupo cadastrado é { media:.2f}')

print(f'Mulheres cadastradas: ')
for p in lista:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=' ')
    

for p in lista:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k}: {v}; ', end=' ')
        print()
    

'''   

dic = {}
lista = list()
while True:
    nome = input('Nome: ')
    sexo = input('Sexo: [M/F] ').upper()
    idade = int(input('Idade: '))
    pessoa = [nome, sexo, idade]

    op = input('deseja continuar? [S/N]').upper()
    if op in 'Nn':
        break
    
    lista.append(pessoa)

dic['cadastro'] = lista
    
print(dic)

'''