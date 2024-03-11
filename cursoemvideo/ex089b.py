"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""

alunos = []
dados = list()
op = ' '

while True:
    nome = input('Nome: ')
    dados.append(nome)
    n1 = float(input('Nota 1: '))
    dados.append(n1)
    n2 = float(input('Nota 2: '))
    dados.append(n2)
    media = (n1 + n2)/ 2
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    op = input('Deseja continuar? [N/S] ')
    if op in 'Nn':
        break
print('-------------------------------')
print('\tBoletim Escolar')
print('-------------------------------')
print('Nome \t\t\tMédia')
for i in range(0, len(alunos)):
    print(f'{i} - {alunos[i][0]}\t\t{alunos[i][3]}')

aluno = int(input('Digite o número do aluno que você deseja ver as notas: '))

for j in range(0, len(alunos)):
    if j == aluno:
        print(f'{alunos[j][0]} -  Nota 1: {alunos[j][1]}, Nota 2: {alunos[j][2]}')
          
#print(alunos[0][0], end=' ')
#print(f'\t\t\t{alunos[0][3]}')
#print(f'{alunos[0]}', end=' ')
#print(f'{alunos[]}')