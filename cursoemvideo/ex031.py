km = int(input('Qual a distância em km? '))
print(f'A distância a ser percorrida é de {km}km')
if km <= 200:
    print(f'Sua viagem vai custar R${km * 0.50 :.2f}')
else:
    print(f'Sua viagem vai custar R${km * 0.45 :.2f}')
    