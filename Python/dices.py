'''
/------------------------------------\
|       |                    |      *|
|   1   | DICE GUESSING GAME |   3   |
|       |                    |*      |
\------------------------------------/
/-----------------\
| BY ROMAN LUKAVA |
\-----------------/
'''

### IMPORT MODULE RANDOM ###
import random

### PLAYER VARIABLES ###
player_coins = 500
player_bet = 0
player_guess = 0

### DICE ASCII ###
dice_1 = ("""
/-------\\
|       |
|   1   |
|       |
\-------\\
""")

dice_2 = ("""
/-------\\
|      *|
|   2   |
|*      |
\-------\\
""")

dice_3 = ("""
/-------\\
|      *|
|   3   |
|*      |
\-------\\
""")

dice_4 = ("""
/-------\\
|*     *|
|   4   |
|*     *|
/-------/
""")

dice_5 = ("""
/-------\\
|*     *|
|   5   |
|*     *|
/-------/
""")

dice_6 = ("""
/-------\\
|*     *|
|*  6  *|
|*     *|
/-------/
""")

### GAMELOOP ###
while (player_coins > 0):
    print("\nYour Coins:", int(player_coins))  # PRINT PLAYERS COINS

    dice1 = random.randint(1, 6)  # ROLL FIRST DICE
    dice2 = random.randint(1, 6)  # ROLL SECOND DICE
    total_roll = (int(dice1) + int(dice2))

    player_bet = input("\nPlace your bet: ")  # PLAYER BETS COINS

    player_guess = input("\nGuess dice roll: ")  # PLAYER GUESSES ROLL

    print("\nDice 1:")  # Print Dice 1

    if dice1 == 1:  # Draw dice 1
        print(dice_1)
    elif dice1 == 2:
        print(dice_2)
    elif dice1 == 3:
        print(dice_3)
    elif dice1 == 4:
        print(dice_4)
    elif dice1 == 5:
        print(dice_5)
    elif dice1 == 6:
        print(dice_6)
    pass

    print("\nDice 2:")  # Print Dice 2

    if dice2 == 1:  # Draw dice 2
        print(dice_1)
    elif dice2 == 2:
        print(dice_2)
    elif dice2 == 3:
        print(dice_3)
    elif dice2 == 4:
        print(dice_4)
    elif dice2 == 5:
        print(dice_5)
    elif dice2 == 6:
        print(dice_6)

    if (int(total_roll) == int(player_guess)):
        print("Rolled", int(total_roll), " you won!")
        player_coins = (int(player_coins) + int(player_bet))
    else:
        print("Rolled", int(total_roll))
        player_coins = (int(player_coins) - int(player_bet))
else:
    print("\nGame Over")
    print("\nDice guessing game","by Roman Lukava")
