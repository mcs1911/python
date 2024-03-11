'''
pessoas = [['Joao', 34], ['Mayan', 35], ['Sergio', 36], ['Tom', 1]]

for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos de idade.')
    
'''

galera = list()
dado = list()

for j in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
print(galera)
print(dado)

for p in galera:
    if p[1] >= 21:
        print(f' {p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')
    
