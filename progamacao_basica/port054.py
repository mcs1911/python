cont = maior = menor = velho = novo =  0
op = 'S'
while True:
    print('----------------------------')
    print(f'Cadastro da {cont + 1}ª pessoa')
    print('----------------------------')
    nome = input('Nome: ')
    if len(nome) < 3:
        print('Nome inválido. Tente novamente')
    else:
        cont += 1
        try:
            idade = int(input('Idade: '))
            while idade > 120 or idade < 0:
                print('Idade inválida')
                idade = int(input('Idade: '))
            if cont == 1:
                maior = idade
                menor = idade
            else:
                if idade > maior:
                    maior = idade
                    velho = nome
                if idade < menor:
                    menor = idade
                    novo = nome
   
        except:
            print('Valor inválido. Tente novamente')
            idade = int(input('Idade: '))
        op = input('Deseja continuar? ').upper()
        while op not in 'SN':
            op = input('Deseja continuar? ').upper()
    if op == 'N':
        break
    
print(f'Foram cadastradas {cont} pessoas')
print(f'A pessoa mais nova é {novo} com {menor} anos')
print(f'A pessoa mais velha é {velho} com {maior} anos')