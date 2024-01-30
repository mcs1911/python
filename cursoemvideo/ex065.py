print('-=-' * 20)
print('Desafio desafiador do while!')

n = int(input('Digite um valor: '))
media = 0
maior = n
menor = n
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
        elif n < menor:
            n = menor
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
