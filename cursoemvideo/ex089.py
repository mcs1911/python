#  EXERCÍCIO 89
"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""

n = int(input('Quantos alunos você quer cadastrar? '))

for i in range(n):
    lista =[]
    for alu in range(n):
        aluno = input('Nome: ')   
        n1 = float(input('Primeira Nota: ')) 
        n2 = float(input('Segunda Nota: ')) 
        media = (n1 + n2) / 2
        
print(lista)