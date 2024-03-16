def Maior(n):
   
    for i in range(0, len(n)):
        if i == 0:
            maior = n[i]
        else:
            if n[i] > maior:
                maior = n[i]
    
    return maior

def Inicio():
    
    num = [3, 7, 1, 4, 9, 6, 2]
    print(f'O maior valor encontrado foi: \033[1;35m{Maior(num)}')
    
Inicio()