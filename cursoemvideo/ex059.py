print('-=-' * 20)
print('MENU DE OPÇÕES')
print('-=-' * 20)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
print('''Selecione a opção desejada: 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
op = int(input('Opção desejada: '))
if op == 1:
    print(f'A soma de {n1} + {n2} = {n1 + n2}')
if op == 2:
    print(f'A multiplicação entre {n1} e {n2} é = {n1 * n2}')
if op == 3:
    if n1 > n2:
        print(f'O maior número digitado foi {n1}')
    else:
        print(f'O maior número digitado foi {n2}')  
while op == 4:
    print('Selecione novos números:')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    op = int(input('Opção desejada: '))
if op == 5:
    print('Você selecionou \033[7msair do programa\033[m')
    print('--FIM--')
if 1 > op or op > 5:
    print('O valor digitado é inválido. Tente novamente')
