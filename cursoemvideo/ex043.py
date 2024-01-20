print('-=-' * 20)
print('CALCULANDO O IMC')
print('-=-' * 20)

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é igual a: {imc :.1f}')
if imc < 18.5:
    print('Seu IMC está abaixo de 18.5 logo você está \033[1;31mABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Seu IMC está entre 18.5 e 25 logo você está com \033[1;32mPESO IDEAL')
elif 25 <= imc < 30:
    print('Seu IMC está entre 25 e 30 logo você está com \033[1;35mSOBREPESO')
elif 30 <= imc <= 40:
    print('Seu IMC está entre 30 e 40 logo você está com \033[1;33mOBESIDADE')
elif imc > 40:
    print('Seu IMC está acima de 40 logo você está com \033[1;31mOBESIDADE MÓRBIDA')
