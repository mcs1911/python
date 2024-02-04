# EXERCÍCIO 05 (50)

'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.

'''

print('----INÍCIO---')

cont = 0
soma = 0
for i in range(1, 7):
   num = int(input(f'Número inteiro {i}: ')) 
   if num % 2 == 0:
       soma += num
       cont += 1
print(f'A soma dos {cont} números pares fornecidos é: {soma}')

print('---FIM---')