#### Library ####

# Importando toda a biblioteca

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')

# Importando uma função específica

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {raiz :.3f}')