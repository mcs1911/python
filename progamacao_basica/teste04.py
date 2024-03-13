lista = [3, 5, 2, 7, 8, 7]
val = int(input('Qual é a chave? '))
for i in range(0, len(lista)):
    if lista[i] == val:
        print(f'O valor {val} foi encontrado na posição {i}')       

if val not in lista:   
    print(f'O valor {val} não foi encontrado na lista')
       