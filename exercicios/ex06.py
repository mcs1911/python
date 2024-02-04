# EXERCÍCIO 06 (51)

''' 
Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('----INÍCIO---')

primeiro = int(input('Primeiro termo: '))
raz = int(input('Digite a razão dessa PA: '))
final = primeiro + raz * 10 

print(f'A PA de {primeiro} com razão de {raz} é:')
    
for num in range(primeiro, final, raz):
    print(num, end=' ')


print('---FIM---')
