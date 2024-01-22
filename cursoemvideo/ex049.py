n = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'A Tabuada de {n} é: {n} x {c :2} = \033[36m{n * c}\033[m')
