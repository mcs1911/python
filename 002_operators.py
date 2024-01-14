### OPERADORES ARITMÉTICOS###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 4) # Módulo
print(10 // 3) # Floor division - divisão aprox até um número inteiro
print(2 ** 3) # Exponencial

print(2 + 6 / 4 * 3 // 3 -5)

# Concatenação

print("Hello " + "Python")

# print("Hello" + 4) #ERROR

print("Hello " + str(4))

print("Hello " * 5)
print("Hello " * (2 ** 3))

my_float = 2.5 * 2 
print("Hello " * int(my_float))

### OPERADORES COMPARATIVOS ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hello" > "Python")
print("Hello" < "Python")
print("Hello" >= "Python")
print("Hello" <= "Hollo") # Ordem alfabética
print(len("Hello") <= len("Hollo")) # Contando caracteres
print("Hello" == "Hello")
print("Hello" != "Python")

### OPERADORES LÓGICOS ###

print(3 > 4 and "Hello" > "Python")
print(3 > 4 or "Hello" > "Python")
print(3 < 4 and "Hello" < "Python")
print(3 < 4 or "Hello" < "Python")
print(3 < 4 or ("Hello" < "Python" and 4 == 4))
print(not(3 > 4))