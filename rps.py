# import
import random
import time

# win/lose/tie counters
wins = 0
loses = 0
ties = 0

# print welcome statement
print("\nHello! Welcome to the RPS game!")
time.sleep(2)
print("\nYou and the computer will pick between rock, paper, and scissors to see who wins!")
time.sleep(3.5)

# the "while True" code here will allow the program to run until the play_again == "n"
while True:

# game code  
 
    # choices
    action_list = ["rock", "paper", "scissors"]

    # computer randomlly selects one choice
    computer_action = random.choice(action_list)

    # user selects their choice
    print("\nPlease make your selection!")
    user_action = input("rock, paper, or scissors?: ")

    # added delay/sleep for "counting off"
    time.sleep(.5)
    print("\nrock...")
    time.sleep(.5)
    print("paper...")
    time.sleep(.5)
    print("scissors...")
    time.sleep(.5)
    print("SHOOT!")
    time.sleep(.5)

    # print choices for user to see
    print(f"\nYou picked {user_action} and the computer picked {computer_action}")

    # determine winner!
    # start with tie conditions to remove extra conditions
    # the wins/loses/ties +=1 added to the counters
    if computer_action == user_action: 
        print("\nIt's a tie!")
        ties += 1
    elif user_action == "rock":
        if computer_action == "paper":
            print("\nPaper covers rock! You lose.")
            loses += 1
        else:
            print("\nRock crushes scissors! You win!")
            wins += 1
    elif user_action == "paper":
        if computer_action == "scissors":
            print("\nScissors cuts paper! You lose.")
            loses += 1
        else:
            print("\nPaper covers rock! You win!")
            wins += 1
    elif user_action == "scissors":
        if computer_action == "rock":
            print("\nRock crushes scissors! You lose.")
            loses += 1
        else:
            print("\nScissors cuts paper! You win!")
            wins += 1

    # show score counter
    print(f"\nYou currently have {wins} wins, {loses} loses, and {ties} ties.")

    # rerun code to play again
    play_again = input("\nPlay again? (y/n): ")
    if play_again != "y":
        print("\nThanks for playing!")
        time.sleep(1)
        break