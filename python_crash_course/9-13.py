from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

print("6-sided die: ")
die = Die(6)
for i in range(10):
    die.roll_die()

print("10-sided die: ")
die_10 = Die(10)
for i in range(10):
    die_10.roll_die()   

print("20-sided die: ")
die_20 = Die(20)
for i in range(10):
    die_20.roll_die()   

