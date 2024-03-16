def Fibonacci(n):
    n1 = 0
    n2 = 1
    lista = [0, 1, ]
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        lista.append(n3)
    
    return lista    
    


def Inicio():
    
    qtd = int(input('Quantos termos vc quer ver? '))
    print(f'Sequência de Fibonacci: {Fibonacci(qtd)} ')
    
Inicio()