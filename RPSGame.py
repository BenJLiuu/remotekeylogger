import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/sci or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Win!")
        user_wins += 1

    else:
        print("Loss!")
        computer_wins += 1

print("Win Count:", user_wins)
print("The computer won", computer_wins)




