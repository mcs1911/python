
def mensagem(txt):
    linha(txt)
    print(f'\n{txt}')
    linha(txt)
    print()


def linha(tam):
    for i in range(0, len(tam)):
        print('-', end=' ')


def Inicio():
    
    mensagem("Olá, tudo bem?")
    mensagem("Estou aprendendo a programar...")
    mensagem("Eu gosto bastante!")


Inicio()