# EXERCÍCIO 57
'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

print('----INÍCIO---')

sexo = 'P'

while sexo != 'M' and sexo != 'F':
    sexo = input('Qual o sexo?[M/F]: ').strip().upper()[0]
    if sexo == 'M':
        print('Sexo Masculino')
    elif sexo == 'F':
        print('Sexo Feminino')
    else: 
        print('Por favor digite um sexo válido!')
print('Obrigada pelo cadastro!')
    
print('---FIM---') 