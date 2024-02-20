hmaior = hmenor = mmaior = mmenor = totm = toth = 0
cont = 1 
homem_velho = ' '
mulher_velha = ' '
homem_novo = ' '
mulher_nova = ' '

while cont <= 5:
    print('---------------------------')
    sx = input('Sexo: [M/F] ').upper()
    nome = input(f'Nome da {cont}ª pessoa: ')
    idade = int(input('Idade: '))
    
    if sx in 'M':
        toth += 1
        if toth == 1:
            hmaior = idade
            hmenor = idade
            homem_velho = nome
            homem_novo = nome
        else:
            if hmaior < idade:
                hmaior = idade
                homem_velho = nome
            if idade < hmenor:
                hmenor = idade 
                homem_novo = nome
    if sx in 'F':
        totm += 1
        if totm == 1:
            mmaior = idade
            mmenor = idade
            mulher_velha = nome
            mulher_nova = nome
        else:
            if mmaior < idade:
                mmaior = idade
                mulher_velha = nome
            if idade < mmenor:
                mmenor = idade 
                mulher_nova = nome
           
    cont += 1
    print('---------------------------')

print(f'Foram digitados {toth} Homens e {totm} Mulheres.')
print(f'O homem mais velho é {homem_velho} com {hmaior} anos')
print(f'A mulher mais velha é {mulher_velha} com {mmaior} anos')
print(f'O homem mais novo é {homem_novo} com {hmenor} anos')
print(f'A mulher mais nova é {mulher_nova} com {mmenor} anos')

'''

hmaior = hmenor = mmaior = mmenor = totm = toth = 0
cont = 1 
homem_velho = ' '
mulher_velha = ' '
homem_novo = ' '
mulher_nova = ' '

while cont <= 5:
    print('---------------------------')
    sx = input('Sexo: [M/F] ').upper()
    nome = input(f'Nome da {cont}ª pessoa: ')
    idade = int(input('Idade: '))
    
    if cont == 1:
        hmaior = idade
        hmenor = idade
        homem_velho = nome
        homem_novo = nome
        mmaior = idade
        mmenor = idade
        mulher_velha = nome
        mulher_nova = nome
        if sx in 'M':
            toth += 1
        else:
            totm += 1
    else:
        if sx in 'M':
            toth += 1
            if hmaior < idade:
                hmaior = idade
                homem_velho = nome
            if idade < hmenor:
                hmenor = idade 
                homem_novo = nome
        if sx in 'F':
            totm += 1
            if mmaior < idade:
                mmaior = idade
                mulher_velha = nome
            if idade < mmenor:
                mmenor = idade 
                mulher_nova = nome
           
    cont +=1
    print('---------------------------')

print(f'Foram digitados {toth} Homens e {totm} Mulheres.')
print(f'O homem mais velho é {homem_velho} com {hmaior} anos')
print(f'A mulher mais velha é {mulher_velha} com {mmaior} anos')
print(f'O homem mais novo é {homem_novo} com {hmenor} anos')
print(f'A mulher mais nova é {mulher_nova} com {mmenor} anos')

'''