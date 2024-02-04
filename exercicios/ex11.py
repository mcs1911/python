# EXERCÍCIO 11 (56)

''' 
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
'''

print('----INÍCIO---')

soma_idade = 0
mulheres_menores = 0
homem_velho = 0
idade_velho = 0

for pessoa in range (1,5):
    nome = input(f'Nome de {pessoa}ª pessoa: ')
    idade = int(input(f'Qual é {pessoa}ª idade: '))
    sexo = input('Sexo: [M/F]').upper()
    soma_idade += idade
    if sexo in 'Femininofeminino' and idade < 20:
        mulheres_menores += 1
    if sexo in 'Masculinomasculino':
        homem_velho = nome
        idade_velho = idade
        if idade_velho < idade:
            idade_velho = idade
            homem_velho = nome
        
        
media = soma_idade // 4
print(f'A média das idades do grupo fornecido é de {media} anos')
print(f'Foram detectadas {mulheres_menores} mulheres menores de 20 anos')
print(f'O homem mais velho do grupo tem {idade_velho} anos e se chama {homem_velho}')

print('---FIM---')
