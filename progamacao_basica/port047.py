print('Contagem personalizada!')
inicio = int(input('INÍCIO: '))
final = int(input('FINAL: '))
passo = int(input('PASSO: '))

if inicio > final:
        passo = (-1) * passo
for c in range(inicio, final, passo):
    print(f'{c}...', end='')
print('ACABOU!')