# import
import random
import time

# win/lose/tie counters
wins = 0
loses = 0
ties = 0

# print welcome statement
print("\nHello! Welcome to the RPS game!\n")
time.sleep(2)
print("You and the computer will pick between rock, paper, and scissors to see who wins!\n")
time.sleep(3.5)

# the "while True" code here will allow the program to run until the play_again == "n"
while True:

# game code  
 
    # choices
    action_list = ["rock", "paper", "scissors"]

    # computer randomlly selects one choice
    computer_action = random.choice(action_list)

    # user selects their choice
    print("Please make your selection!\n")
    user_action = input("rock, paper, or scissors?: ")

    # added delay/sleep for "counting off"
    time.sleep(.5)
    print("\nrock...")
    time.sleep(.5)
    print("paper...")
    time.sleep(.5)
    print("scissors...")
    time.sleep(.5)
    print("SHOOT!\n")
    time.sleep(.5)

    # print choices for user to see
    print(f"You picked {user_action} and the computer picked {computer_action}\n")

    # determine winner!
    # start with tie conditions to remove extra conditions
    # the wins/loses/ties +=1 added to the counters
    if computer_action == user_action: 
        print("It's a tie!\n")
        ties += 1
    elif user_action == "rock":
        if computer_action == "paper":
            print("Paper covers rock! You lose.\n")
            loses += 1
        else:
            print("Rock crushes scissors! You win!\n")
            wins += 1
    elif user_action == "paper":
        if computer_action == "scissors":
            print("Scissors cuts paper! You lose.\n")
            loses += 1
        else:
            print("Paper covers rock! You win!\n")
            wins += 1
    elif user_action == "scissors":
        if computer_action == "rock":
            print("Rock crushes scissors! You lose.\n")
            loses += 1
        else:
            print("Scissors cuts paper! You win!\n")
            wins += 1

    # show score counter
    print(f"You have {wins} wins, {loses} loses, and {ties} ties.\n")

    # rerun code to play again
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        print("Thanks for playing!\n")
        time.sleep(1)
        break