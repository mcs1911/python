def contagem(ini, fim, step):
    print(f' ----- CONTANDO DE {ini} ATÉ {fim} -----')
    for i in range(ini, fim + 1, step):
        print(f'{i} ->', end=' ')
    print('FIM!')
    print()

def Inicio():
    
    contagem(0, 10, 2)
    contagem(10, 50, 5)
    

Inicio()