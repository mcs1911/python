'''
def comprar():
    print('Comprar Bala')
    print('Comprar Suco')
    print('Comprar Picolé')
    
def inicio():
    print('Despertar')
    comprar()
    print('Dançar')
    print('Brincar')
    print('Dormir')

inicio()

def comprar(din):
    if din <= 1:
        print('Comprar Bala')
    elif din <= 2:
        print('Comprar Suco')
    else:
        print('Comprar Picolé')
    
def inicio():
    print('Despertar')
    comprar(1)
    print('Dançar')
    comprar(2)
    print('Brincar')
    comprar(5)
    print('Dormir')

inicio()

'''
def soma(n1, n2):
    n1 += 2
    n2 -= 1
    s = (n1 + n2)
    print(s)
    
def inicio():
    a = 5
    b = 3
    soma(a, b)
    print(f'{a} e {b}')

inicio()