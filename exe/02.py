'''2. Searching and Replacing:
* Find the first occurrence of a specific letter in a string and return its index.
* Replace all instances of a word in a sentence with another word.
* Check if a string contains a specific substring.
* Split a string into a list of words based on a delimiter (e.g., commas, spaces).'''


txt = str(input('Digite uma frase: ')).strip().lower()
if 'a' in txt: 
    print(f'A primeira vez que a letra a aparece na frase é na posição {txt.find('a')}')
else: print('A frase não possui letra a')


frase = str('O sapo não lava o pé')
print(frase)
nova = frase.replace('sapo', 'Sergito')
print(nova)


frase = str('O sapo não lava o pé')
if 'sapo'in frase:
    print(True)
else: print(False)


txt1 = str(input('Digite uma frase: ')).strip()
div = txt1.split(' ')
print(div)
