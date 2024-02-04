# EXERCÍCIO 10 (55)

''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

print('----INÍCIO---')

maior = 0
menor = 100

for pessoa in range(1,6):
    peso = int(input(f'Digite o peso da pessoa {pessoa}: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso 

print(f'O maior pesso encontrado foi de {maior}kg e o menor de {menor}kg')
    
print('---FIM---')