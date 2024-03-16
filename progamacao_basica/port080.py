def Mudapreco(ori, n, op):
    
    if op == "A":
        novo = ori + (ori * n / 100)
    else:
        novo = ori - (ori * n / 100)
    
    return novo

def Inicio():
    
    print('Preço original: R$:1000')
    print(f'Aumento de 20%: R$ {Mudapreco(1000, 20, "A"):.2f}')
    print(f'Desconto de 15%: R$ {Mudapreco(1000, 15, "D"):.2f}')

Inicio()