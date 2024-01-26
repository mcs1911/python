'''
for c in range(1, 10):
    print(c)
print('Fim')

# se o ponto final já estiver definido vc pode usar FOR ou WHILE, mas se vc não conhecer quantas voltas terão que ser dadas até chegar ao objetivo final o FOR não serve para esse tipo de estrutura.
# FOR precisa de um determinado range
# WHILE segue até a condição de controle ser atingida 

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')


n = 1
while n != 0:
    n = int(input('Digite um valor inteiro: '))
print('FIM')



r = 'S'
while r == 'S':
    n = int(input('Digite um valor inteiro: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')