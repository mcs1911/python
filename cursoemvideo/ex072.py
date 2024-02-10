tupla_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

num = -1
while num not in range(0, 21):
    num = int(input('Digite um número de 0 a 20: '))
    num_extenso = tupla_extenso[num]
print(f'Você digitou \033[01;33m{num_extenso}')
    
