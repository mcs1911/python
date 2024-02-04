# EXERCÍCIO 04 (49)

''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

print('----INÍCIO---')

num = int(input('Digite o número que você deseja calcular: '))

for i in range(1, 11):
    print(f' {num} * {i} = {num * i}')

print('---FIM---')