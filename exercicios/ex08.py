# EXERCÍCIO 08 (53)

''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona


print('----INÍCIO---')

frase = input('Digite uma frase: ').upper().strip()

palavras = frase.split(' ')
letras = ''.join(palavras)

if letras == letras[::-1]:
    print(f'A frase {letras} é igual ao seu inverso {letras[::-1]}')
    print(f'A frase {letras} é um PALÍNDROMO')
else:
    print(f'A frase NÃO É UM PALÍNDROMO')
    print(f'A frase {letras} não é igual ao seu inverso {letras[::-1]}')
    
print('---FIM---')