print('----INICIO----')

while True:
    num = int(input('A tabuada de qual número você deseja ver? '))
    print('-' * 20)
    if num < 0:
        print(f'Você digitou um \033[01;31mNÚMERO INVÁLIDO ({num})\033[m e a tabuada foi interrompida!')
        break
    for mult in range(1, 11):
        print(f'{num} * {mult} = {num * mult}')
    print('-' * 20)
    

print('\n----FIM----')