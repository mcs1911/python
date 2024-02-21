
num = cont = soma = maior = 0
while num != 9999:
    num = int(input(f'Digite o {cont + 1}º valor: '))
    if num != 9999:
        cont += 1
        soma += num
        if cont == 1:
            maior = num 
        else:
            if num > maior:
                maior = num

print(f'Você digitou {cont} números')
print(f'O maior número digitado foi {maior}')
if cont != 0:
    print(f'A média dos valores digitados é {soma/cont :.2f}')  
else:
    print('Nenhum número digitado')   

print(f'A somatória de todos os valores digitados é {soma}')
    
    