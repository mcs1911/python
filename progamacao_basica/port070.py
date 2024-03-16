def quadrado(tam):
    for i in range(0, tam):
        for j in range(0, tam):
            print('▄', end=' ')
        print()
    print(f'{tam}x{tam}')
    print()

def Inicio():
    
    quadrado(4)
    quadrado(2)
    quadrado(5)

Inicio()