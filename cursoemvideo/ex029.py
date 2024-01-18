vel = int(input('Qual é a velocidade do carro? '))
print(f'A velocidade do carro é de {vel}km/h')
'''
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print(f'O valor da multa a pagar é de R${multa :.2f}')
'''
if vel > 80:
    print(f'Você foi multado em R${(vel - 80) * 7 :.2f}')


