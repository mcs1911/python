from datetime import date

sexo = str(input('Você é do sexo masculino? ')).lower()
if sexo == 'sim':
    ano = int(input('Digite o seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        tempo = (18 - idade)
        falta = date.today().year + tempo 
        print('Você ainda tem {} anos e faltam {} anos para seu alistamento'.format(idade, tempo))
        print(f'Seu alistamento será no ano de {falta}')
    elif idade == 18:
        print('Você já tem {} anos e deve se alistar'.format(idade))
    else: 
        tempo = (idade - 18)
        saldo = date.today().year - tempo 
        print('Você tem {} anos e já passou {} anos da idade de se alistar'.format(idade, tempo))
        print(f'Seu alistamento deveria ter sido em {saldo}')
else:
    print('O serviço militar não é obrigatório para mulheres no Brasil')