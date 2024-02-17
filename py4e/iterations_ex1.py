'''
soma = cont = 0 

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    try:
        num = int(num)
        soma += num
        cont += 1
    except ValueError:
        print('Invalid input')
        continue
    
    
print(f'Sum: {soma}')
print(f'Count: {cont}')
print(f'Average: {soma / cont :.2f}')



soma = cont = 0 

while True:
    num = input('Enter a number: ')
    if num.lower() == 'done':
        break
    try:
        n = int(num)
        soma += n
        cont += 1
    except ValueError:
        print('Invalid input')
        continue
    
if cont != 0:
    print(f'Sum: {soma}')
    print(f'Count: {cont}')
    print(f'Average: {soma / cont :.2f}')
else:
    print('No numbers were entered.')
 

  
import sys

soma = cont = 0 

while True:
    num = input('Enter a number: ')
    if num.lower() == 'done':
        sys.exit()
    try:
        n = int(num)
        soma += n
        cont += 1
    except ValueError:
        print('Invalid input')
        continue
    
print(f'Sum: {soma}')
print(f'Count: {cont}')
if cont != 0:
    print(f'Average: {soma / cont:.2f}')
else:
    print('No numbers were entered.')

'''

soma = cont = 0 

while True:
    num = input("Enter a number: ")
    
    if num == 'done':
        break
    try:
        num = int(num)
        soma += num
        cont += 1
    except:
        print('Invalid input')
       
print(f'Sum: {soma}')
print(f'Count: {cont}')

if cont > 0 :
    print(f'Average: {soma / cont :.2f}')
else: 
    print('Não foi adicionado nenhum valor')