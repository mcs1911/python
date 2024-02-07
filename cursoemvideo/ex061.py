print('Gerador de Progressões Aritméticas')
print('-=' * 20)

pri = int(input('Digite o primeiro termo: '))
raz = int(input('Qual é a razão dessa PA? '))
termo = pri
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += raz
    cont += 1
print('\n---FIM---')