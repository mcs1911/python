cont = velho = jovem = soma = maior = menor = 0
primeira = True
nome = 'maria'


while True:
    print('------------------------------')
    print('Cadastro de amigos')
    print('------------------------------')
    nome = str(input('Nome: '))
    if nome.upper() == 'FIM':
        break
    idade = int(input('Idade: '))
    print('FIM para terminar')
    
    if primeira:
        velho = nome
        jovem = nome
        menor = idade
        maior = idade
        primeira = False
    else:
        if idade > maior:
            maior = idade
            velho = nome
        if idade < menor:
            menor = idade
            jovem = nome
    soma += idade
    cont += 1 
    
    
print(f'Total de amigos cadastrados: {cont}')
print(f'Seu amigo mais velho é {velho} com {maior} anos.')
print(f'Seu amigo mais jovem é {jovem} com {menor} anos.')
if cont > 0:
    print(f'A média de idade do grupo é de {soma / cont :.2f}')
else:
    print('Nenhum amigo cadastrado')