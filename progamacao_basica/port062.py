lista = list()
dados = []

for i in range(6):
    nome = input('Nome: ')
    sexo = input('Sexo: [M/F]').upper()
    sal = float(input('Salário: R$ '))
    dados.append(nome)
    dados.append(sexo)
    dados.append(sal)
    lista.append(dados[:])
    dados.clear()
    
print('-' * 35)
print('\t\tLISTAGEM COMPLETA')
print('-' * 35)

print('NOME \tSEXO \tSALÁRIO')

for j in range(0, len(lista)):
    print(f'{lista[j][0]} \t{lista[j][1]} \tR${lista[j][2]:.2f}')
    
print('-' * 35)