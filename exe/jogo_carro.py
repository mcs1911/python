comando = ''
started = False

while True:
    comando = input('>>> Digite um comando: ').lower()
    if comando == 'start':
        if started:
            print('O carro já está em movimento')
        else:
            started = True
            print('O carro começou a andar')
    elif comando == 'stop':
        if not started:
            print('O carro já está parado')
        else:
            started = False
            print('O carro parou')
    elif comando == 'help':
        print('''
start - iniciar o carro
stop  - parar o carro
help  - mostrar as opções
quit  - sair do jogo''')
    elif comando == 'quit':
        break
    else:
        print('O camando digitado não é válido. Tente novamente')
print('---FIM DO JOGO---')
