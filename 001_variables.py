my_string_variable = 'Variável de String'
print(my_string_variable)

my_int_variable = 4
print(my_int_variable)

my_int_to_str = str(my_int_variable)
print(my_int_to_str)
print(type(my_int_to_str))

my_bool_variable = False
print(my_bool_variable)

# Concatenação de Variáveis num print

print(my_string_variable, my_int_to_str, my_bool_variable)
print("Concatenação de um texto com uma variável", my_int_variable)

# Algumas funções 

print(len(my_string_variable)) # Mostra a quantidade de caracteres - o lenght 

# Podemos declarar diversas variáveis numa mesma linha 

name, surname, horoscope, age = 'Mayan', "Cavalcanti", 'Escorpião', 35
print('Meu nome é:', name, surname, ". Tenho", age, 'anos.', "Sou do signo de:", horoscope)

first_name = input("What's your name? ")
age = input("How old are you? ")

print("Nice to meet you", first_name)
print(age)