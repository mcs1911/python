name = str(input('Digite seu nome completo: ')).strip()
list = name.split()
print(f'Seu primeiro nome é {list[0]}')
print(f'Seu último nome é {list[-1]}')
