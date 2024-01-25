from datetime import date
cont_maior = 0
cont_menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = date.today(). year - ano 
    if idade >= 21:
        cont_maior = cont_maior + 1
    else:
        cont_menor += 1
print(f'Dos anos de nascimento fornecidos {cont_maior} pessoas são maiores de idade e {cont_menor} são menores de 21 anos.')
  
    