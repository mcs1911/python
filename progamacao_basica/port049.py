print('Sequência de Fibonacci')

x1 = 0
x2 = 1

num = int(input('Digite quantos valores você quer mostrar: '))

for i in range(num):
    if i == 0:
        print(x1, end=' ')
    elif i == 1:
        print(x2, end= ' ')
    else:
        x3 = x1 + x2
        print(x3, end=' ')
        x1, x2 = x2, x3
            
   
    
 