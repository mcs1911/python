lista = []
dados = list()
soma = acima = maior = 0
veio = []
for i in range(5):
    nome = input(f'{i + 1}º Nome: ')
    idade = int(input(f'Idade de {nome}: '))
    dados.append(nome)
    dados.append(idade)
    lista.append(dados[:])
    dados.clear()

for j in range(0, len(lista)):
    soma += lista[j][1]
    
media = soma / len(lista)

print(f'A média das idades das pessoas cadastradas é: {media} anos')

for k in range(0, len(lista)):
    if lista[k][1] >= media:
        acima += 1
        print(f'{lista[k][0]} tem idade acima da média ({lista[k][1]})')
  

for l in range(0, len(lista)):
    if l == 0:
        maior = lista[l][1]
    else:
        if lista[l][1] > maior:
            maior = lista[l][1]

for m in range(0, len(lista)):
    if lista[m][1] == maior:
        veio.append(lista[m][0])

print(f'A maior idade cadastrado foi de {veio} com {maior} anos.')
