# EXERCÍCIO 01 (46)

'''
print('----INÍCIO---')
print('---FIM---')

'''
# Faça um programa que mostre na tela
# Uma contagem regressiva para o estouro e fogos de artifício,
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print('----INÍCIO---')

from time import sleep

for num in range(10,-1, -1):
    print(num)
    sleep(0.5)
print('!!!')
    
print('---FIM---')