from datetime import date

def voto(idade):
    if idade >= 18 and idade <= 65:
        return "VOTO OBRIGATÓRIO"
    elif idade < 18:
        return "VOTO NEGADO"
    else:
        return "VOTO OPCIONAL"


ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

print(f'Com {idade} anos: {voto(idade)}')

