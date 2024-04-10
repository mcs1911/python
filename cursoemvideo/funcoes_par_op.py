# Parâmetro opcional

# se colocar a=0, b=0, c=0 pode chamar a função sem nenhum parâmetro que não vai quebrar o programa

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma dos valores vale {s}')


somar(3, 2, 5)
somar(2, 1)
    