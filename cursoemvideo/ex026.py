frase = str(input('Digite uma frase: ')).lower().strip()
print(f' A letra a aparece {frase.count('a')} vezes na sua frase')
print(f'A primeira letra a aparece na posição {frase.find('a')+1}')
print(f'A última letra a aparece na posição {frase.rfind('a')+1}')

# Se adiciona o + 1 para melhorar a visualização e contagem...