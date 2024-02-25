'''
for i in range(3):
    print(i)
    for e in range(2):
        print(f'{e} - ')
        
for row in range(0, 3):
    for col in range(0, 3):
        print(f'{row} {col}')
        

n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('\n')
n = 5
for i in range(n):
    for j in range(i, n):
        print('*', end=' ')
    print()

print('\n')
n = 5
for i in range(n - 1):
    for j in range(i + 1):
        print('*', end=' ')
    print()

n = 5
for i in range(n):
    for j in range(i, n):
        print('*', end=' ')
    print()

print('\n')

'''

n = 5
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
   
    for j in range(i, n):
        print('*', end=' ')
    
    for j in range(i, n -1):
        print('*', end=' ')  
    print()

print('\n')

n = 5
for i in range(n):
    for j in range(i, n - 1):
        print(' ', end=' ') 
    for t in range(i + 1):
        print('*', end=' ')
    for p in range(i):
        print('*', end=' ')
    
    print()

print('\n')    
n = 5
for i in range(n -1):
    for j in range(i, n - 1):
        print(' ', end=' ') 
        
    for t in range(i + 1):
        print('*', end=' ')
        
    for p in range(i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
   
    for j in range(i, n):
        print('*', end=' ')
    
    for j in range(i, n -1):
        print('*', end=' ')  
    print()
    
