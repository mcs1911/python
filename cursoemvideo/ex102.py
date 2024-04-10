def fatorial(n, show=True):
    """
    -> Calcula o Fatorial de um Número
    
    :parametro n: O número a ser fatorado
    :parametro show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial
       
    """
    if show == True:
        for i in range(n, 0, -1):
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
        
    f = 1
    while n > 0:
        f *= n
        n -= 1 
    return (f'{f}')
    
    
print(fatorial(5, show=True))

'''
RESOLUÇÃO DO PROF

f = 1
for c in range(n, 0, -1):
    if show:
        print(c, end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
    f *= c
return f

'''