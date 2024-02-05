'''
3. Formatting and Trimming:
* Ensure a user's input has only lowercase letters.
* Remove any extra whitespace from the beginning and end of a string.

* Format a string to align text to the left, right, or center.
* Pad a string with a specific character to make it a certain length.
'''

name = str(input('Digite seu nome completo: ')).lower().strip()
print(f'{name}')


