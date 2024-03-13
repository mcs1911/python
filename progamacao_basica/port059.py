print('---------------------------------')
print('\tEscola da Maynha')
print('---------------------------------')

lista = list()
soma = 0
for i in range(6):
    nota = float(input(f'Nota do Aluno {i}: '))
    lista.append(nota)
    
for j in range(0, len(lista)):
    soma += lista[j]
    
media = soma / len(lista)

print(f'A média da turma foi: {media:.2f}')

print('---------------------------------')

print(f'Alunos que ficaram acima da média: ')
for notas in range(0,len(lista)):
    if lista[notas] >= media:
        print(notas, end=' ')
        