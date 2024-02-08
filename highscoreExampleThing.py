high_score = 0
high_player = ''
another = 'y'

while another != 'n':
    #get input from the user
    score = int(input("Enter a new high score: "))
    player = input("Enter a player name: ")
    
    #check if there is a new high score
    if score > high_score:
        print("New high score!")
        high_score = score
        high_player = player

    print(f"Current high score: {high_score} by {high_player}")
    
