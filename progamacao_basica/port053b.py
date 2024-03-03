soma = cont = 0
op = 'S'

while True:
    try:
        num = int(input('Digite um número entre 0 e 10: '))
        if num >= 0 and num <= 10:
            soma += num
            cont += 1
            op = input('Quer continuar?' ).upper()
            while op not in 'NS':
                op = input('Quer continuar? ').upper()
    except:
        print('Valor inválido, tente novemente!')
    
    if op in 'N':
        break
        
print(f'Você digitou {cont} números')
print(f'A soma entre eles é {soma}')

    