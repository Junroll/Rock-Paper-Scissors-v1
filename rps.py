#player selects mode
mode = input("Rock Paper Scissors -> Random Response?     Yes/No\n").lower()

#player choice
player_input = input("rock, paper, or scissors?").lower()

#check if player select is valid
def check_mode(true):
    if true == "yes":
        random_response()
    else:
        if true == "no":
            roll(player_input)
        else:
            print("Please enter a yes or no response")


#check if input is one of the three options
def check(valid):
    if valid == "rock" or valid == "paper" or valid == "scissors":
        check_mode(mode)
    else:
        print("Please enter one of the three options only.")

#function to always beat the user
def roll(option):
    if option == "paper":
        print("Your Input:",player_input)
        print ("Computer Response:","Scissors")
        print()
        print("YOU LOSE!!!!")
    else:
        if option == "scissors":
            print("Your Input:",player_input)
            print("Computer Reponse:","Rock")
            print()
            print("YOU LOSE!!!!")
        else:
            if option == "rock":
                print("Your Input:",player_input)
                print("Computer Response:","Paper")
                print()
                print("YOU LOSE!!!!")

#function to generate random response
def random_response():
    import random
    list1 = ["rock","paper","scissors"]
    computer_response = random.choice(list1)
    print("Your Input:",player_input)
    print("Computer Response:",computer_response)
    print()
    decision(player_input,computer_response)

#Decision of the round
def decision(user, computer):
    if user == computer:
        print("It's a draw. Try Again!")
    elif user == "rock":
        if computer == "paper":
            print("YOU LOSE!!!!")
        else:
            print("Congratulations!! You WIN!!")
    elif user == "scissors":
        if computer == "rock":
            print("YOU LOSE!!!!")
        else:
            print("Congratulations!! You WIN!!")
    elif user == "paper":
        if computer == "scissors":
            print("YOU LOSE!!!!")
        else:
            print("Congratulations!! You WIN!!")

check(player_input)