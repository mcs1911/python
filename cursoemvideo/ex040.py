n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Sua média final foi de \033[1;31m {m :.1f} \033[m e você está \033[1;31mREPROVADO!')
elif 5 <= m <= 6.9:
    print(f'Sua média é de \033[1;33m {m :.1f} \033[m e você está de \033[1;33mRECUPERAÇÃO!')
else:
    print(f'Sua média é de \033[1;32m {m :.1f} \033[m e você está \033[1;32mAPROVADO!')
