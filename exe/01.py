'''1. Basic Manipulation:
* Get user input and print it in all uppercase letters.
* Ask for a sentence and count the number of words in it.
* Reverse a string using slicing and the reversed() function.
* Combine two strings, inserting a space between them.
* Check if a string starts with a vowel and ends with a consonant.'''

name = str(input('Digite seu nome completo? ')).strip()
print(f'{name.upper()}')

frase = str(input('Digite uma frase: ')).strip()
palavras = frase.split()
print(f'Sua frase tem {len(palavras)} palavras') 

fruit = str(input('Qual sua fruta favorita? '))
fruta_reversa = fruit[::-1] #Slicing to reverse
print(f'Sua fruta favorita ao contrário fica: {fruta_reversa}')

#Alternativa:

'''fruta_reversa = ''.join(reversed(fruit)) 
print(f'Sua fruta favorita ao contrário fica: {fruta_reversa}') '''

n1 = str(input('Digite uma palavra: ')).strip()
n2 = str(input('Digite outra: ')).strip()
palavras_unidas = " ".join([n1, n2])
print(f'A junção das suas palavras fica {palavras_unidas}')

vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
cor = str(input('Qual é sua cor favorita? ')).strip()

'''print(f'Sua cor favorita começa com vogal? {cor.startswith(vogais)}')
print(f'Sua cor favorita termina com consoante? {cor.endswith(consoantes)}')'''


print(f'Sua cor favorita começa com vogal? {cor[0] in vogais}')
print(f'Sua cor favorita termina com consoante? {cor[-1] in consoantes}')





