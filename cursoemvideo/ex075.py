lista = []

for i in range(4):
    n = int(input('Digite um valor de 0 a 10: '))
    lista.append(n)

tupla = tuple(lista)
print(tupla)
nove = tupla.count(9)
print(f'O valor 9 apareceu {nove} vezes')
if 3 in tupla:
    tres = tupla.index(3)
    print(f'A primeira aparição de 3 é na posição {tres}')
else:
    print('A tupla não tem o número 3')

lista2 = []
for numero in tupla:
    if numero % 2 == 0:
        lista2.append(numero)
tupla_par = tuple(lista2)
print (f'Os números pares dessa tupla são {tupla_par}')

'''
MACETE PRA CRIAR A TUPLA - SEM FAZER POR LISTA:

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}')

O EXERCÍCIO PODE SER REDUZIDO COLOCANDO AS FUNÇÕES DIRETAMENTE NO PRINT E AO FINAL NÃO É NECESSÁRIO FAZER UMA SEGUNDA LISTA, POIS NÃO ESTAMOS MODIFICANDO A TUPLA, APENAS ITERANDO-A
'''