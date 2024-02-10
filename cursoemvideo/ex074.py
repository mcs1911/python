from random import randint

lista = []

for i in range(5):
    numero = randint(0, 10)
    lista.append(numero)
#print(lista)

tupla_aleatoria = tuple(lista)
print(tupla_aleatoria)
menor = sorted(tupla_aleatoria)[0]
maior = sorted(tupla_aleatoria)[-1]

print(f'O Menor número gerado foi {menor}')
print(f'O Maior número gerado foi {maior}')

# Poderia ter usado max(tupla_aleatoria) e o mesmo com mim