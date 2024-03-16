def Situ(media):
    
    if media < 3:
        s = "REPROVADO"
    elif media <= 6.9:
        s = "em RECUPERAÇÃO"
    else:
        s = "APROVADO"
    
    return s
    
def Media(a, b):
    media = (a + b) / 2
    return media

def Inicio():
    
    n1 = float(input('Primeira Nota: '))
    n2 = float(input('Segunda Nota: '))
    
    print(f'Com as notas {n1} e {n2} o aluno está {Situ(Media(n1, n2))}')

Inicio()