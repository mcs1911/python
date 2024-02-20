peso = acima = chom = cmul = 0
sx = ' '
lim = int(input('Qual é o peso limite: '))
pessoas = int(input('Quantas pessoas você quer cadastrar? '))
cont = 1


while cont <= pessoas:
    (print(f'-----Pessoa {cont} de {pessoas}-----'))
    peso = int(input('Peso: '))
    sx = input('Sexo: [M/F] ').upper()
    while sx not in 'MF':
        sx = input('Sexo: [M/F] ').upper()
    if peso > lim:
        acima += 1 
        if sx in 'M':
            chom += 1
        if sx in 'F':
            cmul += 1 
    cont +=1

print('=========================')
print('\tRESULTADO\t')
print('=========================')

print(f'Ao todo temos {acima} acima do peso limite de {lim}kg.')
print(f'Dessas pessoas, {chom} são Homens e {cmul} são Mulheres.')

    