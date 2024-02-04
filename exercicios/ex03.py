# EXERCÍCIO 03 (48)

# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.

print('----INÍCIO---')


soma = 0
cont = 0
for num in range(1, 500, 2):
    if num % 3 == 0:
        soma += num
        cont += 1
        print(num)
    
print(f'Neste intervalo foram encontrados \033[01;36m{cont}\033[m números ímpares multiplos de 3.')
print(f'A soma de todos estes números é: \033[01;35m{soma}\033[m')

print('---FIM---')
