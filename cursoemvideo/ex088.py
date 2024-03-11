#  EXERCÍCIO 88
'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cada
'''
from random import randint

n_cartelas = int(input('Quantas cartelas você deseja preencher? '))

for i in range(n_cartelas):
    cartela = []
    while len(cartela) < 6:
        num = randint(1, 60)
        if num not in cartela:
            cartela.append(num)
    cartela = sorted(cartela)
    print(cartela)