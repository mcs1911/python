# Para retornar valores

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 6)
r2 = somar(4, 3)
r3 = somar(3)

print(f'Os cálculos deram: {r1}, {r2} e {r3}')