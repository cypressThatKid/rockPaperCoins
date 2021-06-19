import random, os
from colorama import Fore, Style

global coins
coins = 1000
computerCoins = 1000

def bet(numOfCoins, winOrLoose):
    global coins
    if winOrLoose == 'won':
        coins += int(numOfCoins) * 2
    else:
        coins -= int(numOfCoins) 


while True:

    os.system("cls")

    if coins == 0:
        print(Fore.RED + "GAME OVER, YOU HAVE NO MORE COINS!" + Fore.RESET)
        break
    elif coins < 0:
        print(Fore.RED + "GAME OVER, YOU HAVE NO MORE COINS!" + Fore.RESET)
        break

    possible_actions = ['r', 'p', 's']
    computer_action = random.choice(possible_actions)

    print(Fore.BLUE + """
    ___  ___  _____
  / _ \/ _ \/ ___/
 / , _/ ___/ /__  
/_/|_/_/   \___/ 

Rock, Paper, Coins (and scissors)

{}CURRENT-COINS: {}{}
OPERATIONS: {}
AGAINST-COMPUTER: True

Have fun!

    """.format(Fore.GREEN, Fore.RESET, coins, possible_actions) + Fore.RESET)

    user_action = input(Fore.CYAN + "CHOOSE rOCK, pAPER, sCISSORS (r, p, s): " + Fore.RESET)

    coinsToBet = input(Fore.GREEN + "COINS TO BET (YOU HAVE {} COINS): ".format(coins) + Fore.RESET)
    print(f"\nYOU CHOSE {user_action}, OPPONENT CHOSE {computer_action}.\n")

    if int(coinsToBet) > int(coins):
        print(Fore.RED + "YOU CAN NOT BET THAT MUCH, EXITING!" + Fore.RESET)
        break

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        print(Fore.BLUE + "[INFO] YOUR COINS HAVE NOT BEEN AFFECTED" + Fore.RESET)
    elif user_action == "r":
        if computer_action == "s":
            print(Fore.GREEN + "Rock smashes scissors! You win!" + Fore.RESET)
            bet(coinsToBet, 'won') #changes coins based on "won" or "lose" in the second argument
            print(Fore.GREEN + "GAINED {} COINS!".format(int(coinsToBet) + int(coinsToBet)) + Fore.RESET) #tells you how many coins you gained/lost
        else:
            print(Fore.RED + "Paper covers rock! You lose.")
            bet(coinsToBet, 'lose') #changes coins based on "won" or "lose" in the second argument
            print("LOST {} COINS!".format(coinsToBet) + Fore.RESET) #tells you how many coins you gained/lost
    elif user_action == "p":
        if computer_action == "r":
            print(Fore.GREEN + "Paper covers rock! You win!")
            bet(coinsToBet, 'won') #changes coins based on "won" or "lose" in the second argument
            print("GAINED {} COINS!".format(int(coinsToBet) + int(coinsToBet)) + Fore.RESET) #tells you how many coins you gained/lost
        else:
            print(Fore.RED + "Scissors cuts paper! You lose.")
            bet(coinsToBet, 'lose') #changes coins based on "won" or "lose" in the second argument
            print("LOST {} COINS!".format(coinsToBet) + Fore.RESET) #tells you how many coins you gained/lost
    elif user_action == "s":
        if computer_action == "p":
            print(Fore.GREEN + "Scissors cuts paper! You win!")
            bet(coinsToBet, 'won') #changes coins based on "won" or "lose" in the second argument
            print("GAINED {} COINS!".format(int(coinsToBet) + int(coinsToBet)) + Fore.RESET) #tells you how many coins you gained/lost
        else:
            print(Fore.RED + "Rock smashes scissors! You lose.")
            bet(coinsToBet, 'lose') #changes coins based on "won" or "lose" in the second argument
            print("LOST {} COINS!".format(coinsToBet) + Fore.RESET) #tells you how many coins you gained/lost

    play_again = input(Fore.BLUE + "Play again? (y/n): " + Fore.RESET)
    if play_again.lower() != "y":
        break
