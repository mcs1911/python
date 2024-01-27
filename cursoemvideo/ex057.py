print('-=-' * 20)
print('Inicio')

s = 'P'
while s != 'M' and s != 'F':
    s = str(input('Sexo [M/F]: ')).upper()[0]
    print('Por favor digite um sexo válido!')
    if s == 'M':
        print(f'Você digitou Masculino')
    if s == 'F':
        print(f'Você digitou Feminino')
print(f'Você digitou {s}')


# outra forma de fazer seria:
# while sexo not in 'MmFf':