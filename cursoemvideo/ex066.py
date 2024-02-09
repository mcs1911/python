soma = cont = n = 0
print('----INICIO----')

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1 
    
print(f'Você digitou {cont} números e a soma deles vale {soma}.')

print('----FIM----')
