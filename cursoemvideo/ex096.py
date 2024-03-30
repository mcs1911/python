def area(larg, compr):
    a = larg * compr
    print(f'A área do terreno de {larg}x{compr} é {a}m²')
    
    
print('-' * 35)
print('CONTROLE DE TERRENOS')
print('-' * 35)
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))

area(l, c)