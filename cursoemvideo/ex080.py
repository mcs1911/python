lista = []

for _ in range(5):
    valor = int(input('Digite um valor: '))
    
    if not lista:
        lista.append(valor)
    else:
        for i, num in enumerate(lista):
            if valor <= num:
                lista.insert(i, valor)
                break
        else:
            lista.append(valor)
        print(f'O valor {valor} foi adicionado na posição {i}')   
        
print(lista)

'''
SOLUÇÃO DO PROF:

for c in range(0, 5):
    n = int(input('Digite um velor:  '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
            
'''
'''
lista = list()

n3 = 0

maior = menor = 0 

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
lista.append(n1)
if n1 < n2:
    lista.append(n2)
    maior = n2
    menor = n1
else:
    lista.insert(0, n2)
    manor = n2
    maior = n1
for n in range(3):
    n3 = int(input('Digite um valor: '))
    if n3 > maior:
        lista.append(n3)
        maior = n3
    elif n3 < menor:
        lista.insert(0, n3) 
        menor = n3 
    elif menor < n3 < maior:
        lista.insert(1, n3) 
print(lista)

'''