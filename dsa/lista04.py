
   # Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
    
from math import sqrt

class Rocket():

    def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
            
    def move_rocket(self, x_increment=0, y_increment=1):
            self.x += x_increment
            self.y += y_increment
            
    def print_rocket(self):
            print(self.x, self.y)
 

roc1 = Rocket(2, 3)
roc1.x
roc1.y
roc1.print_rocket()

# Não funciona, nem chamando a função diretamente no print

roc2 = roc1.move_rocket(3, 5)
print(roc2)


    # Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2 métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos especiais.


class Pessoa():
    
    def __init__(self, nome, cidade, telefone, email): 
            self.nome = nome
            self.cidade = cidade
            self.telefone = telefone
            self.email = email 
    
    def print_nome(self):
            print(f'Nome: {self.nome}')
    
    def nome_cidade(self):
            cid = input('Digite a cidade: ')
            print(cid)

x = Pessoa('Mayan', 'La Paz', '32', 'may@gmail')
print(x.nome)
print(x.cidade)

print(x.nome_cidade())
# O que fazer para transformar em dado? 
#<__main__.Pessoa object at 0x100dee9f0>
        
'''
    # Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.
    
 '''