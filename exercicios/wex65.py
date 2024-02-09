# EXERCÍCIO 65

''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''

maior = 0 
menor = 100
cont = 0 
soma = 0
continuar = 0
n = 1
op = 'S'
while op in 'Ss':
    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'S':
        cont = 0
    while cont < 5:
        n = int(input('Digite um número: '))
        cont += 1
        soma += n
        media = soma / cont
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        
#op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    
print(f'A média dos valores imputados é de {media :.2f}')
print(f'O maior valor imputado foi {maior} e o menor {menor}.')

print('\n---FIM---')