dia = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos km rodados? '))
print(f'O valor total a pagar é de R${(dia * 60) + (km * 0.15) :.2f}')
