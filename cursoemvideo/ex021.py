import pygame
print("Initializing Pygame")
pygame.init()
print("Loading music")
pygame.mixer.music.load('pon.ogg')
pygame.mixer.music.load('pon.mp3')
print("Playing music...")
pygame.mixer.music.play()
input() # Sem essa caralha não funciona!
pygame.event.wait()
pygame.quit()