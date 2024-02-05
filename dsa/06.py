'''
Guessing Game: Write a program that generates a random number between 1 and 100 and then asks the user to guess it. Use a while loop to keep asking the user for guesses until they get it right.
Word Reverser: Write a program that asks the user for a word and then uses a while loop to print the word backwards.
Palindrome Checker: Write a program that asks the user for a word and then uses a while loop to check if the word is a palindrome (reads the same backwards and forwards).
Multiplication Table: Write a program that asks the user for a number and then uses a nested while loop to print the multiplication table for that number (all the products from 1 x 1 to that number x that number).
Fibonacci Sequence: Write a program that generates the first 10 numbers of the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, 34, 55).
Rock, Paper, Scissors: Write a program that simulates a game of Rock, Paper, Scissors against the computer. Use a while loop to keep playing until the user wants to stop.

print('Count Up: Write a program that uses a while loop to print the numbers from 1 to 10.')

cont = 1
while cont <= 10:
    print(cont)
    cont += 1

for i in range(1,11):
    print(i)

print('Count Down: Modify the previous program to count down from 10 to 1.')

cont = 10
while cont >= 1:
    print(cont)
    cont -= 1

for i in range(10,0, -1):
    print(i)

print('Sum of Numbers: Write a program that asks the user for a number and then uses a while loop to sum up all the numbers from 1 to that number.')

n = int(input('Digite um número: '))

soma = 0
c = 0
while c != n: 
    soma = soma + c
    c += 1
print(f'A soma de todos os numeros até {n} é igual a {soma}')

n = int(input('Digite um número: '))
soma = 0 
c = 1
while c < n:
    soma += c
    c += 1
print(f'A soma de todos os numeros até {n} é igual a {soma}')
'''

#Factorial: Write a program that asks the user for a number and then uses a while loop to calculate the factorial of that number (the product of all positive integers less than or equal to that number).

n = int(input('Digite um número: '))
soma = 0
c = n  
while c != 1:
    multi = (n * c)
    c -= 1
    soma += multi
    print(f'{n}! = {n}*{c}')
print(f'{n}! = {soma}')