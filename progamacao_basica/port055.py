primeiro_valor = 3

# Inicializando uma lista com o primeiro valor
valores = [primeiro_valor]

# Loop para calcular os próximos 9 valores
for _ in range(9):
    # Calculando o próximo valor como o dobro do valor anterior
    proximo_valor = valores[-1] * 2
    valores.append(proximo_valor)

# Imprimindo os valores
print("Os 10 valores são:")
for valor in valores:
    print(f'{valor} -> ', end=' ')
print('FIM')   