'''
name = str(input('Qual é o seu nome? '))
if name == 'Mayan':
    print(f'Que nome lindo você tem {name}!')
print(f'Prazer em te conhecer {name}')
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'Sua média final é {m :.1f}')
print('Você foi APROVADO' if m >= 6 else 'Você foi REPROVADO') #Condição Simplificada


