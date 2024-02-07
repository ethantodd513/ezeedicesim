import random

def main():
    #no arguments
    #call all functions to play the number of games specified
    dice = first_roll()
    number = output_dice(dice)
    count_frequency(dice, number)
    
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
    number = 1
    
    for x in range(len(dice)):
        print("Die	", format(die_number, '2'), ": ", dice[index], sep='')
        die_number += 1
        index += 1
    
    return number

def find_mode(dice):
    #accepts a list of dice
    #uses count_frequency(dice, number) to determine how often each number occurs
    #returns mode
    pass
    
def count_frequency(dice, number):
    dice.sort()
    print(dice)
    print(number)
    index = 0
    
    #searches for ones
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    #searches for 11 digits same
    number = 1
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
        
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
        
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
        
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
        
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
        
    #ssearch for 10 digits same
    
    
    
    
    
    
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number:
        print("The mode is ", number)
        
    elif dice[index] == number:
        print("The mode is ", number)
    
    #searches for twos
    
    number += 1
    print(number)
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number:
        print("The mode is ", number)
        
    elif dice[index] == number:
        print("The mode is ", number)
    
    #searches for threes
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number:
        print("The mode is ", number)
        
    elif dice[index] == number:
        print("The mode is ", number)
    
    #searches for fours
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number:
        print("The mode is ", number)
        
    elif dice[index] == number:
        print("The mode is ", number)
    
    #searches for fives
    
    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number:
        print("The mode is ", number)
        
    elif dice[index] == number:
        print("The mode is ", number)
    
    #searches for sixes

    number += 1
    
    if dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number and dice[index+11] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number and dice[index+10] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number and dice[index+9] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number and dice[index+8] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number and dice[index+7] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number and dice[index+6] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number and dice[index+5] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number and dice[index+4] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number and dice[index+3] == number:
        print("The mode is ", number)
        
    elif dice[index] == number and dice[index+1] == number and dice[index+2] == number:
        print("The mode is ", number)
    
    elif dice[index] == number and dice[index+1] == number:
        print("The mode is ", number)
        
    elif dice[index] == number:
        print("The mode is ", number)
        
def fqm():
    amount = 0
    current = 0
    word = 120
    for die in dice:
        if die == number:
            amount = amount + 1
    return amount

def fart(dice):
    pass