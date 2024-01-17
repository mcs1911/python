'''n = int(input('Digite um número de 0 a 9999: '))
nu = str(n)
print(f'Analisando o número {nu}')
print(f'Unidade: {nu[3]}')
print(f'Dezena: {nu[2]}')
print(f'Centena: {nu[1]}')
print(f'Milhar: {nu[0]}')'''

# Porém essa fórmula só funciona para números de 4 digitos, assim para calcular qualquer número entre 0 e 9999 usaremos a fórmula matemática: 

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidades: {u} \nDezenas: {d} \nCentenas: {c} \nMilhar: {m}')

