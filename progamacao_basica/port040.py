from time import sleep

op = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while op != 5:
    print('----------------------------------')
    print('''Qual operação você deseja realizar? 
          [ 1 ] - ADIÇÃO
          [ 2 ] - SUBTRAÇÃO
          [ 3 ] - MULTIPLICACÃO
          [ 4 ] - Inserir novos valores
          [ 5 ] - SAIR ''')
    print('----------------------------------')
    op = int(input())
    if op == 1:
        print('----------------------------------')
        print('Calculando:', end=' ')
        print(f'{n1} + {n2} = {n1 + n2}')
        print('----------------------------------')
    if op == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    if op == 3:
        print(f'{n1} x {n2} = {n1 * n2}')
    if op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    sleep(0.5)    
print('-----------------FIM-------------------')