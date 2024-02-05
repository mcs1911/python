lista = [4, 7, 22, 193, 53, 242, 1111, 4, 2232, 22, 332, 435]

contador = lista.count(4)
if contador > 1:
    lista.remove(4)

print(lista)

# Outra forma mais generica de fazer isso, se não sabemos exatamente quem queremos remover... e só não queremos repetidos

lista1 = [1, 1, 2, 3, 4, 2, 5, 7, 3]
semduplicado = []

for i in lista1:
    if i not in semduplicado:
        semduplicado.append(i)
        
print(semduplicado)