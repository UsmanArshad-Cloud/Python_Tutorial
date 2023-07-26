import random
class Dice:
    def Roll(self):
        return (random.randint(1,6),random.randint(1,6))
dice=Dice()
print(dice.Roll())