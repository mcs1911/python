dicionario = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five'}

phone = (input('Phone: '))

output = ''
for i in phone:
    output += dicionario.get(i, '!') + ' '

print(output)