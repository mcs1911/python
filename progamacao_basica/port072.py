def Tabuada(n):
    print(f' ------- TABUADA DE {n} -------')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 30)
    
    
def Inicio():
    num = int(input('Quer ver a tabuada de qual número? '))
    Tabuada(num)


Inicio()