print('-=' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 30)

'''
Essa sequência consiste em que cada termo é a soma entre ele e seu antecessor
'''
t1 = 0
t2 = 1
cont = 3 
termos = int(input('Quantos termos você gostaria de ver? '))
print(f'{t1} -> {t2}', end='')
while cont <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(f' -> {t3}', end='')
print('\n---FIM---')