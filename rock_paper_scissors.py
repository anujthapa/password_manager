import random

game_outcoms = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_input = input("Enter your choice Rock/Paper/Scissors or Q to quit ").lower()
    if user_input == "q":
        break
    if user_input not in game_outcoms:
        continue
    rand_gen_num = random.randint(0,2)
    computer_choice = game_outcoms[rand_gen_num]
    if user_input == "rock" and computer_choice =="scissors":
        print("You Won :)")
        user_wins += 1
    elif user_input == "paper" and computer_choice =="rock":
        print("You Won :)")
        user_wins += 1
    elif user_input == "scissors" and computer_choice =="paper":
        print("You Won :)")
        user_wins += 1
    else:
        print("Computer wins")
        computer_wins += 1

print(f"You won {user_wins} times out of {int(user_wins) + int(computer_wins) }")
print("Good bye!")
