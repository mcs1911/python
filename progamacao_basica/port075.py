def analisar(lista):
    print(f'O vetor possui {len(lista)} elementos...')
    
    print('Os elementos da lista são: ')
    for n, p in enumerate(lista):
        print(f'[{n}] -> {p}', end=' ')
    
    print('\nValores PARES nas posições: ', end=' ')
   
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            print(i, end=' ')
    
    print()
    
    print('\nValores ÍMPARES nas posições: ', end=' ')
    
    for i in range(0, len(lista)):
        if lista[i] % 2 == 1:
            print(i, end=' ')

def Inicio():
    
    vet = [2, 8, 7, 4, 3, 1]
    analisar(vet)
    
Inicio()