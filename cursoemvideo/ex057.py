print('-=-' * 20)
print('Inicio')

M = 'Masculino'
F = 'Feminino'
while s != 'M' and s != 'F':
    s = str(input('Sexo [M/F]: ')).upper()
    print('Por favor digite um sexo válido!')
print(f'Você digitou {s}')


