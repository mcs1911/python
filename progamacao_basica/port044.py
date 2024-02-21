from random import randint

cont = soma = maior = menor = cinco = 0

while True:
    sort = randint(0, 10)
    print(f'O {cont + 1}º valor sorteado é {sort}')
    op = input('Quer sortear mais um? [S/N]').upper()
    while op not in 'NS':
        op = input('Quer sortear mais um? [S/N]').upper()
    cont += 1
    soma += sort
    if cont == 1:
        maior = sort
        menor = sort
    else:
        if sort > maior:
            maior = sort
        if sort < menor:
            menor = sort
    if sort == 5:
        cinco += 1
        
    if op == 'N' :
        break
    
    
print(f'Você me fez sortear {cont} valores')
print(f'A soma entre eles é {soma}')
print(f'O maior valor sorteado foi {maior} e o menor foi {menor}')
print(f'O valor 5 foi sorteado {cinco} vezes')