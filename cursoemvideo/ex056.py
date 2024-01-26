somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulhermenor = 0
for p in range(1,5):
    print(f'-----{p}ª PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm'and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulhermenor += 1
mediaidade = somaidade / p
print('--------Resultados:--------')
print(f'A média de idade desse grupo de pessoas é de {mediaidade :.0f} anos')
print(f'O homem mais velho do grupo de pessoas fornecidas tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'No grupo de pessoas fornecidas há {totmulhermenor} mulheres menores de 20 anos')

