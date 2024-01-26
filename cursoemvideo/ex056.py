somaidade = 0
mediaidade = 0

for p in range(1,5):
    print(f'-----{p}ª PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
mediaidade = somaidade / 4
print(f'A média de idade desse grupo de pessoas é de {mediaidade}')
