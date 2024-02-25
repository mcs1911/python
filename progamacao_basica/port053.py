soma = cont = num = 0 
num = int(input('Digite um valor entre 0 e 10: '))

while True:
    op = input('Deseja continuar? [S/N] ')
    if op.upper() in 'N':
        break
    if op.upper() in 'S':
        num = int(input('Digite um valor entre 0 e 10: '))
    while op.upper() not in 'SN':
        op = input('Deseja continuar? [S/N] ')
        
'''  
while num <= 0 and num >=10:
    num = int(input('Digite um valor entre 0 e 10: '))
    if 0 <= num <=10:
        soma += num
        cont += 1
    
 '''     
print(f'Foram digitados {cont} valores')
print(f'A soma dos valores é {soma}')

'''
soma = cont = num = 0 
while True:
    try:
        num = input('Digite um valor entre 0 e 10: ')
        if 0 <= num and num <= 10:
            soma += num
            cont += 1
            op = input('Deseja continuar? [S/N] ').upper()
            if op in 'N':
                break
            while op not in 'SN':
                op = input('Deseja continuar? [S/N] ').upper()
        elif 0 >= num:
            num = int(input('Digite um valor entre 0 e 10: ')) 
        elif num > 10:
           num = int(input('Digite um valor entre 0 e 10: ')) 
    except:
        print('Digitação inválida!')
        num = int(input('Digite um valor entre 0 e 10: '))
'''        
    
 