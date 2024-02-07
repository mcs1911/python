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
n = 10

while cont < n:
    print(f'{num} -> ', end=' ')
    cont +=1
    num += raz
    
n = int(input('\nQuantos números mais você gostaria de ver? '))
        
print('\n---FIM---')
