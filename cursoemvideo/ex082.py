lista1 = []
lista_par = []
lista_impar = []
op = 'S'
while True:
    n = int(input('Digite um número: '))
    lista1.append(n)
    op = input('Deseja continuar? [S/N] ').upper()
    while op not in 'SN':
        op = input('Deseja continuar? [S/N] ').upper()
    if op == 'N':
        break
    
for n in lista1:
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 == 1:
        lista_impar.append(n)
        
print(f'A lista digitada foi: {lista1}')
print(f'Lista dos números pares: {lista_par}')
print(f'Lista dos números ímpares: {lista_impar}')