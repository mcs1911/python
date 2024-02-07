# EXERCÍCIO 59

''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso 
'''

print('----INÍCIO---')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    print('''Digite a operação que deseja realizar:
          [1] - Somar
          [2] - Multiplicar
          [3] - Maior
          [4] - Novos números
          [5] - Sair do programa
          ''')
    op = int(input('Opção: '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif op == 2:
        multi = n1 * n2
        print(f'A multiplicação de {n1} * {n2} = {multi}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é o maior número')
        else:
            print(f'{n2} é o maior número')
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        break
    else: #if 0 > op < 6: 
        print('Opção inválida. Tente novamente.')
        

        
    
print('---FIM---')
