'''

Para usar e modificar o valor de a dentro da função emprega-se a palavra reservada 'global'

Sem o global cria-se duas variáveis, uma com escopo global outra com local

'''

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}') 
