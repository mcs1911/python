from random import randint
n = int(input('Quantos números você quer que eu sorteie? '))
i = 1
soma = 0
while i <= n:
    x = randint(0, 10)
    print(f'O {i}º valor sorteado foi: {x}')
    soma += x
    i += 1
print(f'A soma dos números sorteados foi de \033[01;36m{soma}!')