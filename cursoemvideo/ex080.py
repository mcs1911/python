lista = list()
num = n = cont = 0

for i in range(5):
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont += 1
    if len(lista) > 1:
        n = int(input('Digite um valor: '))
        if num > n:
            lista.insert(cont,num)
print(lista)