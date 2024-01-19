'''
4 . Parsing and Extracting:
* Split a sentence into a list of words and their lengths.
* Extract the last three characters of a string.
* Get the first word from a string.
* Retrieve a substring between two specified indices.

'''

txt = str(input('Digite uma frase: ')).strip()
separado = txt.split()
print(f'Separando a frase fica: {separado} {len(separado)}')

name = str(input('Digite o seu nome: ')).strip()
print(f'As últimas 3 letras do seu nome são: {name[-3], name[-2], name [-1]}')


frase = str(input('Digite uma frase: ')).strip()
sepa = frase.split()
print(f'A primeira palavra da sua frase é \033[32m{sepa[0].upper()}')


a = 'Hello, World!'
print(f'\033[31m{a[2:6]}')
