print('Gerador de Progressões Aritméticas')
print('-=' * 20)

pri = int(input('Digite o primeiro termo: '))
raz = int(input('Qual é a razão dessa PA? '))
termo = pri
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos mais você gostaria de ver? '))

print(f'Progressão finalizada com {total} termos.')