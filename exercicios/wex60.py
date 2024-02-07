# EXERCÍCIO 60

''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

print('----INÍCIO---')

n = int(input('Digite um número inteiro qualquer: '))
i = 10
i = n
fat = 1
print(f'{n}! = {n} ', end='')
while i > 1:
    fat *= i
    i -= 1 
    print(f' * {i}', end=' ')
print(f' = {fat}', end='')

print('\n---FIM---')