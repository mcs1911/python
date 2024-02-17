
controle = []

ex = input('Digite uma expressão matemática: ')

for char in ex:
    if char == '(':
        controle.append(char)
    elif char == ')':
        if len(controle) > 0:
            controle.pop()
        else:
            controle.append(char)
#print(controle)       
if len(controle) == 0:
    print('Sua expressão esta correta')
else:
    print('Tem algo errado na sua expressão!')
       