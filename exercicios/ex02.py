# EXERCÍCIO 02 (47)

# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50

print('----INÍCIO---')

cont = 0
for num in range(2, 50, 2):
    print(num)
    cont += 1
print(f'Ao total essa lista tem \033[01;36m{cont}\033[m números pares')

print('---FIM---')