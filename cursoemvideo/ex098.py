def contador(ini, fim, passo):
    if ini > fim:
        if passo < 0:
            passo *= (-1)
            for j in range(ini, fim + passo, passo):
                print(j, end=' ')
            print('FIM')
        elif passo == 0:
            for i in range(ini, fim - 1, -1):
                print(i, end=' ')
            print('FIM')
        else:
            passo *= (-1)
            for l in range(ini, fim + passo, passo):
                print(l, end=' ')
            print('FIM')
    else:
        if passo < 0:
            passo *= (-1)
            for j in range(ini, fim + passo, passo):
                print(j, end=' ')
            print('FIM')
        elif passo == 0:
            for i in range(ini, fim - 1, 1):
                print(i, end=' ')
            print('FIM')
        else:
            for k in range(ini, fim + 1, passo):
                print(k, end=' ')
            print('FIM')

    print('-=-' * 10)


i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))

contador(1, 10, 1)
contador(10, 0, 2)
contador(1, 10, 0)
contador(-10, 10, 0)
contador(i, f, p)