vezes = int(input('Quantos numeros da sequência? '))
n1 = 0
n2 = 1

print(f'{n1} -> {n2} -> ', end=' ')
for i in range(vezes):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(f'{n3} ->',end=' ')
print('FIM')   