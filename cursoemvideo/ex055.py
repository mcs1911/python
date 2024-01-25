maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual é o {c}º peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é igual a {maior}kg e o menor peso digitado foi igual a {menor}kg')