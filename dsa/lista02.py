
#Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela \"Hoje é dia de descanso\", caso contrário imprima na tela \"Você precisa trabalhar!\"

dia = input('Que dia da semana é hoje? ').strip().lower()
if dia == 'sabado' or dia == 'domingo':
    print(f'Hoje é \033[33m{dia}\033[m, dia de descanso!!!')
else: 
    print(f'Hoje é \033[31m{dia}\033[m, vai trabalhar!!!')

print('---FIM---')

dia = input('Que dia da semana é hoje? ').strip().lower()
if dia in 'sabadosábadodomingo':
    print(f'Hoje é \033[33m{dia}\033[m, dia de descanso!!!')
else: 
    print(f'Hoje é \033[31m{dia}\033[m, vai trabalhar!!!')

print('---FIM---')

#Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista" 

frutas = ['maça', 'pera', 'uva', 'laranja', 'morango']
if 'morango' in frutas:
    print(f'Sim a lista tem \033[33mMorango\033[m na posição {frutas.index('morango')}')
    op = input('Deseja exclui-lo? [s/n] ').strip().upper()[0]
    if op in 'simSim':
        frutas.pop(4)
        print(frutas)
    else:
        print('Valeu falou!')
else:
    print('A lista não tem o morango do deserto')

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

lista = []
minha_tupla = (2, 4, 6, 8)
for i in (minha_tupla):
    i = i * 2
    lista.append(i)
print(lista)
print(minha_tupla)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela"

for i in range(100, 151, 2):
    print(f'{i} ', end='')

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, \n",
# imprima as temperaturas na tela"

temperatura = 40
controle = 36

while 35 < controle < 40:
    print(controle)
    controle += 1
    
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,\n",
# mas quando for encontrado o valor 23, interrompa a execução do programa"

contador = 0
while contador < 100:
    print(contador)
    contador += 1
    if contador == 23:
        break
print('---FIM---')

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, \n",
# adicione à lista, apenas os valores pares e imprima a lista"

lista_ex07 = []
n = 4
tot = 0
while n <= 20:
    n += 1
    if n % 2 == 0:
        lista_ex07.append(n)
        tot += 1
print(lista_ex07)
print(f'A lista é composta de {tot} números pares entre 4 e 20')
 
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)\n",
#nums = range(5, 45, 2)"

lista_ex08 = []
for nums in range(5, 45, 2):
    lista_ex08.append(nums)
print(lista_ex08)
    
# Exercício 9 - Faça a correção dos erros no código abaixo e#execute o programa. Dica: são 3 erros.\n",

temperatura = float(input('Qual a temperatura? '))

if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
 
# Exercício 10 - Faça um programa que conte quantas vezes a letra \"r\" aparece na frase abaixo. Use um placeholder na \n",
# sua instrução de impressão\n",
# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” \n",

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão."

resultado = frase.count('r')

print(f'Na frase fornecida foram encontrados {resultado} letras "r".')

  