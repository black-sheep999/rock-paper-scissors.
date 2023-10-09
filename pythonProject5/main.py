import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, or scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        stop = ("You won a total number of " + str(+user_points) + "and computer total score is " + str(computer_points))
        print("stop")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("your input is rock")
            print("computer input is rock")
            print("it is a tie")
        if computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer wins ")
            computer_points += 1
        if computer_input == "scissors":
            print("your input is rock")
            print("computer input is scissors")
            print("you win!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("your input is paper")
            print("computer input is rock")
            print("you win! ")
            user_points += 1
        if computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("it is a tie")
        if computer_input == "scissors":
            print("your input is paper")
            print("computer input is scissors")
            print("computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("your input is scissors")
            print("computer input is rock")
            print("computer wins")
            computer_points += 1
        if computer_input == "paper":
            print("your input is scissors")
            print("computer input is paper")
            print("you win")
            user_points += 1
        if computer_input == "scissors":
            print("your input is scissors")
            print("computer input is scissors")
            print("it is a tie")

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "stop":
        print("Invalid Input")
