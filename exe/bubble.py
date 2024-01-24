'''
Inicio

Peça para o usuário uma lista de números

Validar quem é o menor número e assim sucessivamente

Criar uma nova lista com os valores em ordem

mostrar nova lista 

FIM

'''

lista = [32,15,6,89,65,24,2]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n): # Para cada elemento i do array
        for j in range(0, n-i-1): # Para cada elemetno j do array
            if arr[j] > arr[j+1]: # Se elemento i for maior que elemento j
                arr[j], arr[j+1] = arr[j+1], arr[j] #troque os elementos i e j de posição
    return arr
print(bubble_sort(lista))

print('--FIM--')