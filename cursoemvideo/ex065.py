print('-=-' * 20)
print('Desafio desafiador do while!')

media = 0
maior = 0
menor = 10
op = 'S'
cont = 0 

while op == 'S':
    n = int(input('Digite um valor: '))
    op = str(input('Você deseja continuar inserindo números?: ')).upper()
    media = media + n
    cont += 1
    if op == 'N':
        mediaf = media / cont
        print(f'A média dos {n} os números digitados foi: {mediaf :.1f}')
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
