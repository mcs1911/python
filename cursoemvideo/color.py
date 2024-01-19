'''
Style : 0, 1, 4, 7 (None, bold, sub, negative/inversão)
Color : 30 - branco
        31 - vermelho
        32 - verde
        33 - amarelo
        34 - azul
        35 - lilas
        36 - turquesa
        37 - cinza
Backgound : Mesmo esquema começando por 40

\033[Style;color;backgroundm
para tirar a formatação, se necessário, colocar o \033[m ao final
'''

print('\033[33mHello, World!') #Verde
print('\033[31mHello, World!') #Vermelho
print('\033[1;34;43mHello, World!')
print('\033[7;34;43mHello, World!\033[m')

a = 3
b = 5 

print(f'Os valores são \033[31m{a}\033[m e \033[34m{b}')