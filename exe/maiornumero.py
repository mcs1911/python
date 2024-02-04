lista = [4, 7, 22, 193, 53, 242, 1111, 4, 2232, 22, 332, 435]
maior = 0 
# Aqui o maior poderia ser o primeiro número da lista maior = lista[0]
for i in lista:
    if i > maior:
        maior = i
print(maior)

# Outra forma de conseguir o maior número de uma lista

lista.sort()
lista.reverse()
print(lista[0])