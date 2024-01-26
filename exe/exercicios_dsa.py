
#Fundamentos de Linguagem Python Para Análise de Dados e Data Science

#Capítulo 4 - Exercícios

print('Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.')

lista = []

for c in range(1,11):
    lista.append(c)

print(f'{lista}')

print('Exercício 2 - Crie uma lista de 5 objetos e imprima na tela')

lista = ['café', 'chocolate', 'pão', 'bolacha', 'leite']
print(lista)

print('Exercício 3 - Crie duas strings e concatene as duas em uma terceira string')

palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite outra palavra: ')
print(f'{palavra1} {palavra2}')

# OU print(palavra1 + palavra2)
# OU print(palavra1 + " " + palavra2)
# frase = palavra1 + palavra2 // print(frase)


print("""Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla""")

tup = (1, 2, 2, 3, 4, 4, 4, 5)
print(tup)
contador = tup.count(4)
print(f'O número 4 aparece {contador} vezes na tupla fornecida.') 

# OU print(tup.count(4))

print('Exercício 5 - Crie um dicionário vazio e imprima na tela')

dict = {}
print(dict)

print('Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela')

dici = {"Mayan":35, "Sergito":36, "Maria":68}
print(dici)
print(dici.keys())
print(dici.values())

print('Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela')

dici["Carmen"] = 66
print(dici)

print("""Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
Um dos valores deve ser uma lista de 2 elementos numéricos. 
Imprima o dicionário na tela.""")

dicionario = {"dia":19, 'ano': 1988, "data":[19, 11]}
print(dicionario)

print("""Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
o quarto elemento um valor do tipo float.
Imprima a lista.""")

lista_ex9 = ["gatinho", (2, 44), {"Cor": "Azul", "Numero": 3}, 3.14]
print(lista_ex9)
print(type(lista_ex9[0]))
print(type(lista_ex9[1]))
print(type(lista_ex9[2]))
print(type(lista_ex9[3]))


print("""Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'""")

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:19])
print(frase[1:18])