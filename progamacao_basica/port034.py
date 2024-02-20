cont_par = cont_impar = soma_par = soma_impar   = 0

cont = 1

while cont <= 5:
    val = int(input(f'Digite o {cont}º  valor: '))
    if val % 2 == 0:
        cont_par += 1
        soma_par += val
    else:
        cont_impar += 1
        soma_impar += val
    cont += 1
if cont_impar != 0:
    media_impar = soma_impar / cont_impar
else:
    print('Não foram adicionados valores ímpares')
    
if cont_par != 0:
    media_par = soma_par / cont_par
else:
    print('Não foram adicionados valores pares')

print(f'Você digitou {cont_par} números pares. A média desses valores é: {media_par :.2f}')
print(f'Você digitou {cont_impar} números ímpares. A média desses valores é: {media_impar :.2f}')