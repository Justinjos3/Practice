import random
options = ["Rock", "Paper", "Scissors"]
opposing_weapon = ""
my_weapon = ""
my_score = 0
computer_score = 0


while my_score != 10 and computer_score != 10:
    opposing_weapon = random.choice(options)
    my_weapon = input("Enter your weapon: ")
    if my_weapon == "Rock" and opposing_weapon == "Scissors":
        print("You score")
        my_score += 1
        print(my_score)
        print(computer_score)
    elif my_weapon == "Rock" and opposing_weapon == "Rock":
        print("Tie game")
    elif my_weapon == "Rock" and opposing_weapon == "Paper":
        print("Computer scores")
        computer_score += 1
        print(my_score)
        print(computer_score)
    elif my_weapon == "Paper" and opposing_weapon == "Rock":
        print("You score")
        my_score += 1
        print(my_score)
        print(computer_score)
    elif my_weapon == "Paper" and opposing_weapon == "Paper":
        print("Tie game")
    elif my_weapon == "Paper" and opposing_weapon == "Scissors":
        print("Computer scores")
        computer_score += 1
        print(my_score)
        print(computer_score)
    elif my_weapon == "Scissors" and opposing_weapon == "Paper":
        print("You score")
        my_score += 1
        print(my_score)
        print(computer_score)
    elif my_weapon == "Scissors" and opposing_weapon == "Scissors":
        print("Tie game")
    elif my_weapon == "Scissors" and opposing_weapon == "Rock":
        print("Computer scores")
        computer_score += 1
        print(my_score)
        print(computer_score)
    else:
        print("Error")

if my_score == 5:
    print("YOU WIN!!")
if computer_score == 5:
    print("YOU LOSE!!")
