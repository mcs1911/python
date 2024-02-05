'''
5. Advanced Techniques:
* Check if a string is a palindrome (reads the same backward as forward).
* Count the frequency of each letter in a string.
* Convert a string to a list of numbers (e.g., "1234" to [1, 2, 3, 4]).
* Encrypt or decrypt a string using a simple substitution cipher.
'''
frase = str(input('Digite uma frase: '))
print(f'A letra \033[1;43m a \033[m aparece {frase.count('a')} vezes na frase que você digitou!')
