n1 = int(input('Digite um número: '))
n2 = int(input('Agora digite outro: '))
s = n1 + n2
m = n1 * n2
sub = n1 - n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'O resultado da soma entre {n1} e {n2} é {s}, a multiplicação é {m}, a subtração é {sub} e a divisão dá {d :.2f}.')
print(f'Já a divisão inteira é igual a: {di} e a exponenciação é: {e}.')

# Se mesmo tendo duas linhas de comando de print, eu quisesse que aparecesse tudo numa mesma linha era só colocar end = ' ' no final do primeiro print.

# Para quebrar a linha dentro de um print \n