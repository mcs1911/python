lista = []
op = 'S'
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado. Não vou adicionar...')
    else: 
        lista.append(num)
        print('Valor adicionado com sucesso...')
    op = input('Quer continuar? [s/n] ').upper()
    while op not in 'SN':
        op = input('Quer continuar? [s/n] ').upper()

    if op == 'N':
        break

ordem = sorted(lista)
print(f'Você digitou os valores {ordem}')