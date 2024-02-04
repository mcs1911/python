import random

   
class Dice:
    def roll(self):
        primeira = random.randint(1,6)
        segunda = random.randint(1,6)
        return primeira, segunda
    
# no Return não precisa colocar () para indicar que é uma tupla... pq o python faz isso automaticamente

rolar = Dice()
print(rolar.roll())