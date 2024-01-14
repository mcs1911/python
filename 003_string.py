### STRINGS ###

my_string = "Minha String"
my_other_string = "Minha outra String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Esta é uma String\ncom salto de linha"
print(my_new_line_string)

my_tab_string = "\tEsta é uma String com Tabulação"
print(my_tab_string)

my_scape_string = "\\tEsta é uma String\\n escapada"
print(my_scape_string) # A barra extra ignora o comando 

# Formatando 

name, surname, age = "Mayan", "Cavalcanti", 35

print("Meu nome é {} {} e tenho {} anos.".format(name, surname, age))
print("Meu nome é %s %s e tenho %d anos." %(name, surname, age))
print(f"Meu nome é {name} {surname} e tenho {age} anos.")

# Muito mais fácil do que fazer a concatenação
print("Meu nome é " + name + " " + surname + " e minha idade é " + str(age))

# Desempacotando caractéres

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)

# Divisão

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_language = language[:: -1]
print(reversed_language)

# Funções

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("11".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))