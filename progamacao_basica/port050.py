print('--------Tabuadas--------')

inicial = int(input('Tabuada INICIAL: '))
final = int(input('Tabuada FINAL: '))
for e in range(inicial, final + 1):
    print('------------------------------')
    print('----------CALCULANDO----------')
    print('------------------------------')
    for i in range(1, 11):
        print(f'{e} x {i} = {e * i}')
        
print('\n------FIM------')