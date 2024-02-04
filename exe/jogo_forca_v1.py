import random
from os import system, name

#Função para limpar a tela após cada execução

def limpa_tela():
    #Comando para Winsdows
    if name == 'nt':
        _ = system('cls')
    #Comando para Mac e Linux
    else:
        _ = system('clear')