def maior_numero(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

