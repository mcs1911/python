'''
def contar_letras():
    s = input('Digite uma palavra: ')
    l = input('Qual letra você deseja contar? ')

    cont = 0
    for letra in s:
        if letra == l:
            cont += 1
    print(cont)
    
contar_letras()

'''
# Para que aceite como argumento:

def contar_letras(s, l):

    cont = 0
    for letra in s:
        if letra == l:
            cont += 1
    return cont
    
ex1 = contar_letras('caramelo', 'a')
print(ex1)