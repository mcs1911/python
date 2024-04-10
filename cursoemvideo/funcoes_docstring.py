# Criando uma documentação para uma função

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
        :parametro i: inicio da contagem
        :parametro f: fim da contagem
        :parametro p: passo da contagem
        :return: sem retorno
    """
    
    c = i
    
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


help(contador)