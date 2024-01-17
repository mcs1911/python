name = str(input('Qual é o seu nome completo? ')).strip()
print(f'{name.upper()}')
print(f'{name.lower()}')
print(f'Seu nome ao todo tem {len(name) - name.count(' ')} letras')
print(f'Seu primeiro nome tem {name.find(' ')} letras')

# Também poderia ser 
# primeiro = name.split()
# print(f'Seu primeiro nome é {primeiro[0]} e tem {len(separa[0])} letras')