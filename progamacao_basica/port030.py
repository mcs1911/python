num = int(input('Sua contagem começa em qual número? '))
fim = int(input('E vai até o número? '))
inc = int(input('Qual o incremento? '))

while num <= fim:
    if num % 4 == 0:
        print('PIN!\n')
    else:
        print(num, end=' ')
    num += inc
print('----FIM---')