n = int(input('Digite um número: '))

fat = 1
while n > 0:
    fat *= n
    n -= 1

print(fat)

'''

soma = 1
for i in range(n, 0, -1):
    r = n * i
    print(f'{n}x{i}')
    soma *= r
print(soma)

'''