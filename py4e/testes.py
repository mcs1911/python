'''
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

NameError: name 'repeat_lyrics' is not defined


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

'''
x = 'Sergio'
index = 5
while index >= 0:
    letter = x[index]
    print(letter)
    index -= 1 
    