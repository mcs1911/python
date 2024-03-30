from datetime import date 

trabalhador = {}

while True:
    trabalhador['nome'] = input('Digite o nome: ')
    ano_nasc = int(input('Ano de nascimento: '))
    trabalhador['idade'] = date.today().year - ano_nasc
    trabalhador['num_carteira'] = int(input('Carteira de Trabalho (0 se não houver): '))
    if trabalhador['num_carteira'] == 0:
        break
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['sal'] = float(input('Salário: R$'))    
    
    trabalhador['aposentadoria'] = (35 - (date.today().year - trabalhador['contratacao'])) + trabalhador['idade']
    break 

print('-=-' * 30)
print(trabalhador)


for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
    

