frutas = list()
dados = []
totmui = totpou = 0

for fruta in range (3):
    dados.append(input('Digite uma fruta: '))
    dados.append(int(input('Quantas frutas? ')))
    frutas.append(dados[:])
    dados.clear()
print(frutas)
print(dados)

for fruta in frutas:
    if fruta[1] < 5:
        print(f'Temos pouca {fruta[0]}')
        totpou += 1
    else:
        print(f'Temos bastante {fruta[0]}')
        totmui += 1
print(f'Temos {totmui} frutas em bastante quantidade e {totpou} fruta que tem pouco')