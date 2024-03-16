
def Meu_Escreva(txt, quant, x):
    
    def borda(n):
        if n == 0:
            print(" ")
        elif n == 1:
            print('=-=' * 12)
        elif n == 2:
            print('--:::--' * 5)
        elif n == 3:
            print('<<<<<<<<<<<<----------->>>>>>>>>>>>>')
    
    borda(x)
    for i in range(0, quant):
        print(txt)
    borda(x)

def Inicio():
    Meu_Escreva("Oi", 1, 1)
    Meu_Escreva("Estou aprendendo a programar", 3, 2)
    Meu_Escreva("É bem desafiador...", 2, 3)
    Meu_Escreva("Sucesso total!", 5, 0)

Inicio()