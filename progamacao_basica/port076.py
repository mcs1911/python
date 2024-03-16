def Somador(a, b):
    return a + b
    

def Inicio():
    
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    s = Somador(n1, n2)
    print(f'A soma entre os dois valores é {s}')


Inicio()


'''
return a + b 

ou 

soma = a + b
return soma

'''