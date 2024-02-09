print('-' * 30)
print('LOJA DA MAYNHA')
print('-' * 30)

continuar = 'S'
preco = total = caro = cont = 0
nome_barato = nome = 'c'
barato = 1000
while True:
    cont += 1
    if continuar in 'Nn':
        print('Finalizando sua compra')
        break
    if continuar in 'Ss':
        nome = input('Produto: ')
        preco = int(input('Preço R$: '))
        total += preco
        if preco > 1000:
            caro += 1
        if barato > preco:
            nome_barato = nome
            barato = preco
    continuar = input('Deseja continuar a compra [S/N]: ')
    print('-' * 30)

print('-' * 30)                
print(f'Total R$: {total:.2f}')
print(f'Quantidade de produtos com valor superior a R$1000,00 foram \033[01;35m{caro}\033[m')
print(f'O produto mais barato é \033[01;32m{nome_barato} e custa R${barato}\033[m')
        
    
    
    
        