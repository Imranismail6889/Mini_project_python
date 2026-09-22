import random

choices = ["rock", "paper", "scissors"]
print("🎮 Rock Paper Scissors")
print("Type rock, paper, or scissors")
while True:
    user = input("Your choice: ").lower()
    if user not in choices:
        print("Invalid choice. Try again.")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins!")
