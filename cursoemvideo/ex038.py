n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
if n1 > n2:
    print(f' \033[1;32m {n1} \033[m é maior que \033[1;36m {n2}')
elif n1 < n2:
    print(f' \033[1;32m {n2} \033[m é maior que \033[1;36m {n1}')
else:
    print(f'O primeiro e o segundo valor são \033[1;31m IGUAIS \033[m e valem: \033[1;31m {n1}')
