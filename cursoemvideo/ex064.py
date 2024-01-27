print('-=-' * 20)

n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro qualquer: '))
    soma = soma + n
    if n == 999:
        soma = soma - 999
print(f'A soma de todos os números digitados foi {soma}')