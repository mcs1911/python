
print('Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.')

lista = [2, 3, 4]

for i in lista:
    print((i ** 3))
    
'''
list1 = [3,4,5]
quadrado = [item**3 for item in list1] 
print(quadrado)
'''

print('Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!')

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()

resultado = list(map(lambda w : [w.upper(), w.lower(), len(w)], palavras))
for i in resultado:
    print(i)
    
#Esse for final é para criar listas separadas para cada elemento criado na função split
  
# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.

matrix = [[1, 2],[3,4],[5,6],[7,8]]

transposta = list(zip(*matrix))
print(transposta)

'''
SOLUÇÃO DO PROFESSOR:

matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
'''
 
print('Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. Aplique as duas funções aos elementos da lista abaixo. Obs: as duas funções devem ser aplicadas simultaneamente')

lista = [0, 1, 2, 3, 4]

def quadrado(x):
    return (x ** 2)

def cubo(x):
    return (x ** 3)

func = [quadrado, cubo] 

resultado = [list(map(lambda f: f(i), func)) for i in lista]
print(resultado)

'''

OUTRA FORMA SERIA DECLARANDO LAMBDA COMO AS FUNÇÕES QUADRADO E CUBO:

# Função para calcular o quadrado de um número
quadrado = lambda x: x**2

# Função para calcular o dobro de um número
dobro = lambda x: x*2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicando as funções usando map
resultados_quadrado = list(map(quadrado, numeros))
resultados_dobro = list(map(dobro, numeros))

# Imprimindo os resultados
print("Números:", numeros)
print("Quadrados:", resultados_quadrado)
print("Dobros:", resultados_dobro)

'''

print('Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado ao elemento correspondente na listaB.')
listaA = [2, 3, 4]
listaB = [10, 11, 12]

#[x * y for x, y in zip(lista1, lista2)]

resultado = [x ** y for x, y in zip(listaA, listaB)]
print(list(resultado))

'''
RESOLUÇÃO DO PROFESSOR

listaA = [2, 3, 4]
listaB = [10, 11, 12]
print(list(map(pow, listaA, listaB)))
'''
    
print('Exercício 6 Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos. range(-5, 5)')

def verificar_negativo(n):
    if n < 0:
        return True
    else:
        return False    

lista = []
for i in range(-5, 5):
    lista.append(i)
print(f'Lista de números propostos: \033[01;33m{lista}\033[m') 

#list(filter(lambda n: n < 0, lista))

resultado = list(filter(verificar_negativo, lista))
print(f'O resultado da lista com apenas os números negativos: \033[01;35m{resultado}\033[m')

range(-5, 5)
list(filter((lambda x: x < 0), range(-5,5)))

print('Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.') 
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

# Definindo uma função

def igualdade(elemento):
    return elemento in a and elemento in b

valores_comuns = list(filter(igualdade, b))

print(valores_comuns)

# RESOLUÇÃO DO PROFESSOR print(list(filter(lambda x: x in a, b)))

# Usando Lambda

comuns = list(filter(lambda elemento: elemento in a and elemento in b, b))
print(comuns)

#resultado = list(filter(igualdade(a,b), a b))
#print(resultado)

# Exercício 8 - Considere os dois dicionários abaixo. 
 # Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

intercalando = zip(dict1.keys(), dict2.values())
print(list(intercalando))

'''
SOLUÇÃO DO PROFESSOR:

def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

dict3 = trocaValores(dict1, dict2)
print(dict3)

'''
print('Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5')

#lista = ["banana", "maçã", "laranja", "uva"]
#for indice, valor in enumerate(lista):
#print(f"Índice: {indice}, Valor: {valor}")

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for indice, valor in enumerate(lista):
    if indice > 5:
        print(f'Índice: {indice}, Valor: {valor}') 
   
# Com a função Lambda:
     
print(list(filter(lambda indice_valor: indice_valor[0] > 5, enumerate(lista))))

'''
SOLUÇÃO DO PROFESSOR:

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for indice, valor in enumerate(lista):
    if indice <= 5:
        continue
    else:
        print (valor)
'''

print('Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras Data e Science" na frase: A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.')
    
import re

frase = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

# Padrão regex para extrair a palavra após 'Data Science'

padrao = re.compile(r'\bData Science\b\s+(\w+)')

correspondencia = padrao.search(frase)

if correspondencia:
    palavra_apos_data_science = correspondencia.group(1)
    print(f"A palavra após 'Data Science' é: {palavra_apos_data_science}")
else:
    print("Não foi possível extrair a palavra.")
        

  