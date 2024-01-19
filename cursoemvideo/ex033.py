n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o Terceiro número: '))

# Verificando qual é o menor valor
menor = n1
if n1 > n2 and n3 > n2:
    menor = n2
if n3 < n1 and n3 < n2 :
    menor = n3
    
# Verificando qual é o maior valor
maior = n3
if n2 > n3 and n2 > n1:
    maior = n2
if n1 > n2 and n1 > n3:
    maior = n1

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

'''      
n1 < n2 < n3
n1 > n2 > n3
n1 < n2 > n3
n1 > n2 < n3
'''