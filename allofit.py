import random

def main():
    #no arguments
    #call all functions to play the number of games specified
    dice = first_roll()
    output_dice(dice)
    
def first_roll():
    #no arguments
    #uses roll_die() to generate list of 12 integers
    #returns a list of 12 random integers
    dice = []
    
    for x in range(12):
        
        dieroll = roll_die()
        dice.append(dieroll)
        
    return dice
    
def roll_die():
    #accepts no arguments
    #makes a random integer from 1 to 6
    #returns a random integer from 1 to 6

    return random.randint(1, 6)

def output_dice(dice):
    #accepts dice
    #outputs each die in the list
    #returns
    
    
    roll_number = 1
    print("----Roll # ", roll_number, "----", sep='')
    
    die_number = 1
    index = 0
    
    for x in range(len(dice)):
        print("Die	", format(die_number, '2'), ": ", dice[index], sep='')
        die_number += 1
        index += 1
    
def count_frequency(dice, number):
    