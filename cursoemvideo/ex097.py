def linha(n):
    n = len(n) 
    print('~' * n)
    
    
def escreva(texto):
    linha(texto)
    print(texto)
    linha(texto)



msg = input('Digite uma frase: ')

escreva(msg)

'''
poderia ser tudo numa unica def

def escreva(texto):
    tam = len(texto)
    print('~' * tam)
    print(texto)
    print('~' * tam)

'''