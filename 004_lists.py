### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 50, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.78, "Mayan", "Cavalcanti"] #Não precisa conter o mesmo tipo de dados

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])

#print(my_other_list[4]) IndexError pq essa posição não foi atribuída
#print(my_other_list[-5]) IndexError

print(my_list.count(30))

print(my_list + my_other_list) #na ordem indicada
#print(my_list - my_other_list) Error

my_other_list.append("Escorpião") #Ao final da lista
print(my_other_list)

my_other_list.insert(1, "Frambuesa") #Na posição indicada
print(my_other_list)

my_other_list[1] = "Morango"
print(my_other_list)

my_other_list.remove("Morango")
print(my_other_list)

my_list.remove(30) #Só exclui um dos dois 30 que tinha
print(my_list) 

del my_list[2] #Remove elimina algo que conhecemos/ sabemos que esta na lista, del simplesmente remove por indíce
print(my_list)

print(my_list.pop()) #Exclui o ultimo valor, ou o valor indicado 
print(my_list)

print(my_list.pop(2))
print(my_list)

#Se quisessemos guardar o elemento eliminado teriamos que criar uma variável
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list) # Essa não foi limpa, pois foi copiada sua imagem antes do clear

my_new_list.reverse()
print(my_new_list)

my_new_list.append(2)
print(my_new_list)

my_new_list.sort() #Faz por ordem de grandeza, do menor para o maior
print(my_new_list)

print(my_new_list[1:3]) #Aqui imprime o que está entre os indices 1 e 3