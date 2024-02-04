# EXERCÍCIO 09 (54)

''' 
Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores
'''

print('----INÍCIO---')

from datetime import date

maiores = menores = 0

for i in range(1, 8):
    ano = int(input(f'Ano de nascimento de {i}: '))
    idade = date.today(). year - ano
    if idade < 21:
        menores += 1
    else:
        maiores += 1 

print(f'Da lista fornecida \033[01;32m{menores}\033[m pessoas são menor de idade e \033[01;36m{maiores}\033[m são maior de idade')

print('---FIM---')