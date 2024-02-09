from random import randint



print('----JOGO DO PAR OU ÍMPAR----')

ganhar = 0
perder = 1

while True:
    if perder == 0:
        break
    jog_num = int(input('Número: '))
    jog_escolha = ' '
    comp_num = randint(0, 11)
    soma = jog_num + comp_num
    print('-' * 30)
    while jog_escolha not in 'PpIi':
        jog_escolha = input('Você quer Par ou Ímpar [P/I]: ').strip().upper()[0]
    if jog_escolha in 'Pp':
        if soma % 2 == 0:
            print(f'Você escolheu {jog_num} e o computador escolheu {comp_num}. A soma = \033[01;32m{soma} é PAR!!!!\033[m VOCÊ GANHOU!')
            ganhar += 1
        else:
            print(f'Você escolheu {jog_num} e o computador escolheu {comp_num}. A soma = \033[01;31m{soma} é ÍMPAR!!!!\033[m Você PERDEU!')
            perder -= 1
    if jog_escolha in 'IiÍí':
        if soma % 2 != 0:
            print(f'Você escolheu {jog_num} e o computador escolheu {comp_num}. A soma = \033[01;32m{soma} é ÍMPAR!!!!\033[m VOCÊ GANHOU!')
            ganhar += 1
        else:
            print(f'Você escolheu {jog_num} e o computador escolheu {comp_num}. A soma = \033[01;31m{soma} é PAR!!!!\033[m Você PERDEU!')
            perder -= 1
        print('-' * 30)

print('-' * 30)
print(f'\nVocê ganhou \033[01;32m{ganhar}\033[m vezes!!!')  

print('\n----FIM----')