import random

def roll_die():
    #accepts no arguments
    #returns a random integer from 1 to 6

    return random.randint(1, 6)

def first_roll():
    #no arguments
    #uses roll_die() to generate list of 12 integers
    #returns a list of 12 random integers
    dice = []
    
    for x in range(12):
        
        dieroll = roll_die()
        dice.append(dieroll)
        
    return(dice)

def output_dice(dice):
    pass