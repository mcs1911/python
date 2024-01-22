for c in range(0, 6):
    print('Hello')
print('FIM')

for c in range(0, 6):
    print('Hello')
    print('FIM')

for c in range(0, 6):
    print('c')
print('FIM')

for c in range(0, 6, 2):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3): # O comando de abaixo vai ser executado as vezes que estiverem descritas no range
    n = int(input('Digite um número: '))
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n # s = s + n
print(f'O somatório de todos os valores é {s}')