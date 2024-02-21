cont = par = menor =  0

while True:
    n = int(input(f'Digite o {cont + 1}º valor: '))
    cont += 1
    op = input('Quer continuar? [S/N]').upper()
    while op not in 'NS':
        op = input('Quer continuar? [S/N]').upper()
    
    if n % 2 != 0:
        if cont == 1:
            menor = n
        else:
            if n < menor:
                menor = n
    else:
        par += 1
                
    if op == 'N' :
        break


print(f'Ao todo foram digitados {cont} valores')
print(f'Você digitou {par} valores PARES')
print(f'O menor valor Ímpar digitado foi {menor}')
print('************** FIM **************')