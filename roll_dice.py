import random

def roll_die():
    #accepts no arguments
    #returns a random integer from 1 to 6
    for x in range(12):
        dice = random.randint(1, 6)
        print(dice)
    
    return dice