import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])



def get_user_choice():
    choice=input("Enter your choice:")
    return choice




def determine_winner(user, computer):
    print(f"comp selected {computer}")
    if user==computer:
        print("Draw")
    elif user=="rock"  and computer=="scissors":
        print("User wins")
    elif user=="scissors" and computer=="paper":
        print("User wins")
    elif user=="paper" and computer=="rock":
        print("user wins")
    else:
        print("Computer wins")
        return


def play(user_choice, comp_choice):
    user_choice=get_user_choice()
    comp_choice=get_computer_choice()
    result=determine_winner(user_choice, comp_choice)
    
    return(result)
play(get_user_choice, get_computer_choice)





