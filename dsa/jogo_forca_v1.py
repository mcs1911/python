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
        
# Função
def game():
    
    limpa_tela()
    
    print('\nJogo da Forca!')
    print('Advinhe a palavra abaixo:\n')
    
    # Lista de palavras secretas
    palavras = ['naja', 'potro', 'ema', 'jacare', 'cascavel', 'jabuti', 'siri']
    
    # Escolher randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # List Comprehension
    letras_descobertas = ['_' for letra in palavra]
    
    chances = 6
    
    letras_erradas = []
    