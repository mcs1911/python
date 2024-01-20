r1 = float(input('O primeiro segmento de reta vale: '))
r2 = float(input('O segundo segmento de reta vale: '))
r3 = float(input('O terceiro segmento de reta vale: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} \033[32mPODEM\033[m formar um triângulo')
    if r1 == r1 == r3:
        print('Com essas retas é possível formar um triângulo \033[1;33mEQUILÁTERO')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Com essas retas é possível formar um triângulo \033[1;35mISÓSCELES')
    else:
        print('Com essas retas é possível formar um triângulo \033[1;36mESCALENO')
else:
    print(f'As retas {r1}, {r2} e {r3} \033[31mNÃO PODEM\033[m formar um triângulo')