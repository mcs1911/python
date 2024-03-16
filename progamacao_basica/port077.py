def Primo(n):
    div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            div += 1
    if div > 2:
        primo = False
    else:
        primo = True
    
    return primo


def Inicio():
    num = int(input('Digite um número para saber se ele é primo: '))
    if (Primo(num)):
        print(f'O número {num} \033[1;32mÉ PRIMO!\033[m')
    else:
        print(f'O número {num} \033[1;31mNÃO É PRIMO!')

Inicio()

'''
O professor fez a logica do laço verificando entre 2 e um número antes do número... assim se ele for divisível dentro desse intervalo ele não é primo

e comeeçou o programa com primo = True e se ele fosse divisível por algum numero  primo = False e um break para parar o programa.
'''