print('-=-' * 20)
print('Bem-vindo à Calculadora Simples!')
print('-=-' * 20)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('''Digite a operação que você deseja realizar: 
[ 0 ] - para ADIÇÃO
[ 1 ] - para SUBTRAÇÃO
[ 2 ] - para MULTIPLICAÇÃO
[ 3 ] - para DIVISÃO ''')
op = int(input('Opcão escolhida: '))
if 0 <= op <= 3:
    if op == 0:
        print(f'{n1} mais {n2} = {n1 + n2}')
    elif op == 1:
        print(f'{n1} menos {n2} = {n1 - n2}')
    elif op == 2:
        print(f'{n1} vezes {n2} = {n1 * n2}')
    elif op == 3:
        print(f'{n1} dividido por {n2} = {n1 / n2}')
else:
    print('Operação inválida. Tente Novamente')
print('--FIM--')