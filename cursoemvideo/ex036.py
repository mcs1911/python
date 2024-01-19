print('-=- * 20')
print('Bem vindo ao sistema de \033[31m Empréstimos \033[m do Banco Mayan]')
print('-=- * 20')
valor = float(input('Digite o valor do Imóvel: R$ '))
sal = float(input('Digite o seu salário: R$ '))
anos = float(input('Em quantos anos você deseja pagar? '))
prest = valor / anos 

if prest > sal * 0.3:
    print(f'Sua prestação {prest :.2f} é muito alta com relação ao seu salário {sal :.2f}')
    print('Seu empréstimo foi \033[1;31m NEGADO!')
else:
    print('Seu empréstimo foi \033[1;32m ACEITO!')