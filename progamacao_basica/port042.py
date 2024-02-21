homem = mulher = cont = som_salh = totm = maior = 0
while True:
    nome = input('Nome: ')
    sx = input('Sexo: ')
    sal = float(input('Salário R$ '))
    op = input('Quer continuar? [S/N] ').upper()
    
    while op not in 'SN':
        op = input('Quer continuar? [S/N] ').upper()
    
    if sx in 'Mm':
        homem += 1 
        som_salh += sal
        if cont == 1:
            maior = sal
        else:
            if sal > maior:
                maior = sal
    if sx in 'Ff':
        mulher += 1
        if sal > 1000:
            totm += 1
    cont += 1
    if op == 'N':
        break
    
print(f'Total de pessoas cadastradas: {cont}')
print(f'Total de HOMENS cadastradas: {homem}')
print(f'Total de MULHERES cadastradas: {mulher}')
if homem > 0:
    print(f'Média salarial dos homens: {som_salh / homem :.2f}')
else: 
    print('Homens não foram cadastrados')
print(f'Total de mulheres que ganham acima de R$ 1000: {totm}')
print(f'Maior salário entre os homens R${maior}')