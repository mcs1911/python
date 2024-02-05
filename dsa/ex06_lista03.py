'''
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
#range(-5, 5)
'''

def verificar_negativo(n):
    if n < 0:
        return True
    else:
        return False    

lista = []
for i in range(-5, 5):
    lista.append(i)
print(f'Lista de números propostos: \033[01;33m{lista}\033[m') 

#list(filter(lambda n: n < 0, lista))

resultado = list(filter(verificar_negativo, lista))
print(f'O resultado da lista com apenas os números negativos: \033[01;35m{resultado}\033[m')
    
