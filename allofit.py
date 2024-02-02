import random

def main():
    #no arguments
    #call all functions to play the number of games specified
    first_roll()
    
def first_roll():
    #no arguments
    #uses roll_die() to generate list of 12 integers
    #returns a list of 12 random integers
    dice = []
    
    for x in range(12):
        
        dieroll = roll_die()
        dice.append(dieroll)
        
    return(dice)
    
def roll_die():
    #accepts no arguments
    #returns a random integer from 1 to 6

    return random.randint(1, 6)

def output_dice(dice):
    #accepts dice
    #outputs each die in the list
    
    print(dice)
    
def poop():
    pass
def apples():
    poop = 19
    for poooo in range(12):
        poop += 1
        
    print(poop)