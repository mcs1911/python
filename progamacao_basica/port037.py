nome_velho = nome_novo = maior = menor = 0
cont = 1

while cont <= 5:
    print('---------------------------')
    nome = input(f'Nome da {cont}ª pessoa: ')
    idade = int(input('Idade: '))
    if cont == 1:
        maior = idade
        menor = idade
        nome_novo = nome
        nome_velho = nome
    else:
        if idade > maior:
            maior = idade
            nome_velho = nome
        if idade < menor:
            menor = idade 
            nome_novo = nome
            
    cont +=1
    print('---------------------------')

print(f'A pessoa com maior idade é {nome_velho} com {maior} anos')
print(f'A pessoa com maior idade é {nome_novo} com {menor} anos')