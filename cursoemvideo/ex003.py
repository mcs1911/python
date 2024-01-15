n = input('Digite algo: ')
print('O tipo privitivo desse valor é: ', type(n))
print('O que você digitou é Alfanumérico? ', n.isalnum())
print('O que você digitou é Alfabético? ', n.isalpha()) 
print('O que você digitou é um espaço? ', n.isspace()) 
print('O que você digitou é Decimal? ', n.isdecimal())
print('O que você digitou é Numérico? ', n.isnumeric())
print('O que você digitou está em letras Maiúsculas? ', n.isupper())
print('O que você digitou está em letras Minúsculas? ', n.islower())
print('O que você digitou está Capitalizado? ', n.istitle())


