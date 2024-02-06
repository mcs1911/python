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
    
    while chances > 0:
        print(' '.join(letras_descobertas))
        print('\nChances restantes:', chances)
        print('Letras erradas:', ' '.join(letras_erradas))
        
        tentativa = input('\nDigite uma letra: ').lower()
        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        if '_' not in letras_descobertas:
            print('\n\033[01;32mParabéns você venceu! A palavra era: ', palavra)
            break
        
    if '_'in letras_descobertas:
        print('\n\033[01;31mVocê perdeu... a palavra era: ', palavra)

# Bloco main
if __name__ == '__main__':
    game()
    
        
    