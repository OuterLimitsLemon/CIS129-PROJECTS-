# Oscar E. Saenz
# Professor Troy Adams
# CIS129
# 19 October 2024

# Lab 7-3 The Dice Game
# This program simulates a dice game between two players, determining a winner based on the random dice rolls.

# add libraries needed
import random

# the main function
def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames()  # Removed arguments since the function does not take any.

    # while loop to run program again
    while endProgram.lower() == 'no':
        # populate variables
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo)

        # call to displayInfo
        displayInfo(winnerName)

        endProgram = input('Do you want to end program? (yes/no): ')

# this function gets the players' names
def inputNames():
    playerOne = input('Player one, please enter your name: ')
    playerTwo = input('Player two, please enter your name: ')
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    # determine the winner
    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = "TIE"

    return winnerName

# this function displays the winner
def displayInfo(winnerName):
    print(f"Winner: {winnerName}")

# calls main
main()
