# EXERCÍCIO 07 (52)

''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''

# SÓ PODE SER DIVISÍVEL 2 VEZES, POR 1 E POR ELE MESMO

print('----INÍCIO---')

num = int(input('Digite um número: '))

total = 0

for n in range(1, num + 1):
    
    if num % n == 0:
        total += 1

print(f'O número {num} foi divisível \033[01;35m{total}\033[m vezes')   
if total == 2:
    print(f'O número \033[01;32m{num} É PRIMO\033[m')
else:
    print(f'O número \033[01;31m{num} NÃO É PRIMO!\033[m') 
    
print('---FIM---')
