
dic = {}

while True:
    nome = input('Nome: ')
    sexo = input('Sexo: [M/F] ').upper()
    idade = int(input('Idade: '))
    pessoa = [nome, sexo, idade]
    dic['cadastro'] = pessoa
    op = input('deseja continuar? [S/N]').upper()
    if op in 'Nn':
        break
    
print(dic)