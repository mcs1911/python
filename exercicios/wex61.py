# EXERCÍCIO 61
'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''

print('----INÍCIO---')

pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
cont = 1
num = pri
while cont < 10:
    print(f'{num} -> ', end=' ')
    cont +=1
    num += raz
        
print('\n---FIM---')