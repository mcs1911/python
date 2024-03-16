def contagem(i, f, p):
    print(f'------ CONTANDO DE {i} a {f} ------')
    if i > f  and p > 0:
        for j in range(i, f - 1, - p):
            print(f'{j} -> ', end=' ')
    else:
        for k in range(i, f - 1, p):
            print(f'{k} -> ', end=' ')  
    print('FIM!')
    print()
    
def Inicio():
    
    contagem(0, 10, 2)
    contagem(10, 50, 5)
    contagem(10, 2, 1)
    contagem(50, 0, -10)


Inicio()