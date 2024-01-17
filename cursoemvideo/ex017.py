# Fórmula com importação da raiz quadrada

'''from math import sqrt

cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjascente: '))

print(f'Com o cateto oposto igual a {cato} e o cateto adjascente igual a {cata} a hipotenusa desse trinângulo retângulo é igual a {sqrt(cato * cato + cata * cata) :.2f}')'''

# Fórmula Matemática

'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = (co ** 2 + ca **2) ** (1/2)

print(f'A hipotenusa desse triângulo vale {hi :.2f}')
'''

# Fórmula com importação da Hipotenusa

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)

print(f'A hipotenusa deste trinÂngulo vale {hi :.2f} ')


