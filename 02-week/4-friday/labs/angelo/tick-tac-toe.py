from time import sleep
import os
# ready = input('''Please select your character.
# 1. X     2. O ''')

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

ready = input('''Please select your character.
1. X     2. O ''')

while True:
        os.system('clear')
        print('''Board Guide:  1 | 2 | 3
             -----------
              4 | 5 | 6
             -----------
              7 | 8 | 9 ''')
        print()     
        print(print_board())
        player_1 = int(input('Please choose an empty space for X '))
        if board[player_1] == ' ':
            board[player_1] = 'X'
        else:
            print()
            print('Please choose another square.')
            sleep(1)
        board[player_1] = "X"
        print()
        if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
            print("X wins!!")
            print()
            break
        elif board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
            print("X wins!!")
            print()
            break
        elif board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
            print("X wins!!")
            print()
            break
        elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            print("X wins!!")
            print()
            break
        elif board[2] == 'X' and board[5] == 'X' and board[9] == 'X':
            print("X wins!!")
            print()
            break
        elif board[3] == 'X' and board[6] == 'X' and board[9] == 'X':
            print("X wins!!")
            print()
            break
        elif board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
            print("X wins!!")
            print()
            break
        elif board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
            print("X wins!!")
            print()
            break

    
#Tick-Tac-Toe Rules
# Within the game there is a 1 large square made up of 9 tiny other squares in a 3x3 format
# You choose one of two characters, X or O, to play the game, players can only use X and O
# Must decide on a method for which player of the two goes first 
# When the game starts you may place your character in any of the 9 squares 
# The turn switches to the next player and that player can place their character on any of the 8 remaining squares
# You cannot place your character in a space that is already occupied
# You cannot place your character in any section outside of the 1 large square.
# The play switches between each of the players until each 1 player gets 3 of their characters in a row in any direction
# If a player wins the program must inform the player with that specific character that they have one
# If all of the spaces on the "board" are taken up and their is no winner the program must inform the match was a draw





# player = 'x'
# while True:
#     print(f'it is player {player} turn')
#     # all the player's actions
#     # check for if game as been won
#     player = switch_player()
    


# def switch_player(player):
#     if player == 'x':
#         player = 'o'
#     elif player == 'o':
#         player = 'x'






# board - a 2-dimensional array that represents a 3x3 tic-tac-toe board
# location - a 2-item tuple that specifies an cell on the board
# player - a String, either "X" or "Y
# Return a copy of the board with the player String placed at the location.


# Throw an error if:

# The board is the wrong size
# The location is already occupied by a player
# The location is invalid
# The player String is something other than "X" or "Y"