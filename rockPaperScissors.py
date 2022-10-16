# --------------------------------------
# Name: Daniel Barbosa and John Pham
# Date: 10/13/2022
# Project One: Rock, Paper, Scissors game
# --------------------------------------

# Declare variable that tells user what to type
print("Let's play Rock, Paper, Scissors.")
print()
char1 = 'RPS' # 'RPS' declared to use 

# Loop that takes in players' inputs, in addition print error message if not 'RPS'
while True:
    player1 = input("Player 1, Enter your choice: ")
    
    if player1.upper() not in "RPS":
        print("[ERROR:",player1 ,"not a valid move.]")

    else:
    
        userInput1 = input("Player 2, Enter your choice: ")
        player2 = userInput1
     
        # Processing steps that prints the outcomes of the games    
        if player1.upper() == 'S' :
            if player2.upper() == 'P' :
                print("Scissors v. Paper") 
                print("Player 1 wins")
            elif player2.upper() == 'S':
                print("Scissors v. Scissors")
                print("It's a TIE")
            elif player2.upper() == 'R':
                print("Rock v. Scissors")
                print("Player 2 wins")
            else:
                print("Scissors v. [Error",player2,"not a valid move.]" )
        elif player1.upper() == 'R' :
            if player2.upper() == 'S' :
                print("Rock v. Scissors")
                print("Player 1 wins")
            elif player2.upper() == 'R':
                print("Rock v. Rock")
                print("It's a TIE")
            elif player2.upper() == 'P':
                print("Rock v. Paper")
                print("Player 2 wins")
            else:
                print("Rock v. [Error",player2,"not a valid move.]")
        elif player1.upper() == 'P':
            if player2.upper() == 'R':
                print("Paper v. Rock")
                print("Player 1 wins")
            elif player2.upper() == 'P':
                print("Paper v. Paper")
                print("It's a TIE")
            elif player2.upper() == 'S':
                print("Paper v. Scissors")
                print("Player 2 wins")
        else:
            print("Paper v. [ERROR: ", player2 ,"not a valid move.]")
    # Asks player to input y or n for a rematch (y = rematch, n = game ends)
    rematch = input("\nagain? \n")
    
    # Continue game if 'Y', if not 'Y' end the game.
    if rematch.upper() != "Y":
        break

print("Nice Game!")