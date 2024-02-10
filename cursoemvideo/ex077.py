palavras = ('manga', 'maça', 'laranja', 'uva', 'pera', 'morango')
#frutas = list(palavras)

'''
for fruta in frutas:
    vogal = set()
    for letra in fruta:
        if letra in 'aeiou':
            vogal.add(letra)
            print(f'A palavra {fruta} possui as vogais {", ".join(vogal)}')


for fruta in palavras:
    vogal = ''
    for letra in fruta:
        if letra in 'aeiou' and letra != vogal:
            vogal += letra
    print(f'A palavra {fruta.upper()} possui as vogais {", ".join(vogal).upper()}')
'''

for fruta in palavras:
    vogal = set()
    for letra in fruta:
        if letra in 'aeiou':
            vogal.add(letra)
    ordem = ", ".join(sorted(vogal))
    print(f'A palavra {fruta.upper()} possui as vogais {ordem.upper()}')