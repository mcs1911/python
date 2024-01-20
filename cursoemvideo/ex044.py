print('-=-' * 20)
print('CONDIÇÕES DE PAGAMENTO')
print('-=-' * 20)

valor = float(input('Digite o valor do produto: R$ '))
pag = str(input('Digite a forma de pagamento desejada: ')).lower()
if pag == 'dinheiro' or pag == 'cheque':
    print(f'\033[7mTotal a pagar:\033[m R${valor - valor * 0.1 :.2f}')
elif pag == 'cartao' or pag == 'cartão':
    par = int(input('Quantidade de parcelas: '))
    if par == 1:
        print(f'\033[7mTotal a pagar:\033[m  R${valor - valor * 0.05 :.2f}')
    elif par == 2:
        print(f'\033[7mTotal a pagar:\033[m  R${valor :.2f}')
    elif par >= 3:
        print(f'\033[7mTotal a pagar:\033[m  R${valor + valor * 0.2 :.2f}')
        print(f'Total de parcelas: {par} \nValor de cada parcela: R${(valor + valor * 0.2) / par}')
print('Obrigada pela sua compra!')
         
