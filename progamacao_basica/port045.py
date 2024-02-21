from random import randint

numero = randint(1, 10)
cont = tentativas = 0
print('Vou pensar em um número de 1 a 10... Você tem 3 chances para adivinhar')
while True:
    tent =int(input(f'Chance número {cont + 1}: '))
    tentativas += 1
    if tent == numero:
        print('Uau você ACERTOU!')
        break
    elif tent > numero:
        print('Não foi dessa vez, pense em um número MENOR')
    elif tent < numero:
        print('Não foi dessa vez, pense em um número MAIOR')
    
    cont += 1
    
    if cont == 3:
        print('Você errou! Mais sorte na próxima vez')
        break
if tent == numero:
    print(f'Você precisou de {tentativas} tentativas')
print('FIM DO JOGO!')