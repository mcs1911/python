brasileirao_2018 = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo", "Atlético", "Athletico Paranaense", "Cruzeiro", "Botafogo", "Santos", "Bahia", "Fluminense", "Corinthians", "Chapecoense", "Ceará", "Vasco da Gama", "America Fc", "Sport", "Vitória", "Paraná")

print(f'Os 5 primeiros colocados foram {brasileirao_2018[:5]}')
print(len(brasileirao_2018))
print(f'Os 4 últimos colocados foram {brasileirao_2018[-4:]}')
print(sorted(brasileirao_2018))
posiçao = brasileirao_2018.index("Chapecoense") + 1
print(f'A posição do Chapecoense neste campeonato é {posiçao}ª posição')