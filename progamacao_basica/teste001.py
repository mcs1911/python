
num = int(input('Sua contagem começa em qual número? '))
fim = int(input('E vai até o número? '))
op = input('''Você deseja incrementar ou decrementar?
        1 - Incrementar
        2 - Decrementar
        ''')

while op not in '12':
    op = input('''Você deseja incrementar ou decrementar?
        1 - Incrementar
        2 - Decrementar
        ''')
x = int(input('Qual valor? '))

if op == '1':
    for i in range(num, fim, x):
        print(i )
        
elif op == '2':
    for i in range(num, fim, -x):
        print(i)
print('----FIM---')

