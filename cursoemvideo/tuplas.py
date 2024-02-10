frutas = ('Pessêgo', 'Uva', 'Laranja', 'Mamão', 'Maça')

# 3 formas de iterar a tupla

for fruta in frutas:
    print(f'{fruta}')
    
for fruta in range(0, len(frutas)):
    print(f'Vou comer {frutas[fruta]}')

for position, fruta in enumerate(frutas):
    print(f'{fruta} está no INDEX {position}')