print('-=-' * 20)
print('Desafio desafiador do while!')

soma = cont = media = maior = menor = 0
op = 'S' 
while op in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Você deseja continuar inserindo números?[S/N]: ')).upper().strip()[0]
        
media = soma / cont

print(f'A média dos {n} os números digitados foi: {media :.2f}')     
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')

