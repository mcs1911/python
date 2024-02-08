# EXERCÍCIO 62
'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

print('----INÍCIO---')

pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
cont = 1
num = pri
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{num} -> ', end=' ')
        cont +=1
        num += raz
    mais = int(input('\nQuantos números mais você gostaria de ver? '))
        
print('\n---FIM---')
