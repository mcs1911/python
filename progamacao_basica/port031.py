'''
num = int(input('Sua contagem regressiva vai começa em qual número? '))
fim = int(input('E vai até o número? '))
mul = int(input('Qual multiplo? '))

while num <= fim:
    if num % mul == 0:
        print(f'\033[01;35m[{num}]\033[m')
    else:
        print(num)
    num += 1
print('----FIM---')

'''

num = int(input('Sua contagem regressiva vai começa em qual número? '))
mul = int(input('Qual multiplo? '))

while num >= 0:
    if num % mul == 0:
        print(f'\033[01;35m[{num}]\033[m')
    else:
        print(num)
    num -= 1
print('----FIM---')