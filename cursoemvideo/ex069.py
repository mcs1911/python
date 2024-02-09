homens = menor = 0
mulheres_menores = 0
continuar = 'S'

while True:
    if continuar in 'Nn':
        break
    print('-' * 30)
    print('----CADASTRO----')
    print('-' * 30)
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if sexo in 'MmFf':
        idade = int(input('Idade: '))
        if idade < 18:
            menor += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            mulheres_menores += 1
        continuar = input('Deseja continuar cadastrando? [S/N]: ').strip().upper()[0]


print('-' * 30)
print('----ANALISANDO----')
print('-' * 30)
print(f'Foram cadastradas \033[01;33m{menor} pessoa(s) menor(es) de 18 anos.\033[m ')
print(f'Foram cadastrados \033[01;36m{homens} homens.\033[m')
print(f'Foram cadastradas \033[01;35m{mulheres_menores} mulher(es) menores de 20 anos.\033[m ')
print('\n----FIM----')
