import random
user_score = 0
computer_score = 0

def get_user_choice():
    ch = input("Choose rock, paper, or scissors: ").lower()
    while ch not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please choose rock, paper, or scissors.")
        ch = input("Choose rock, paper, or scissors: ").lower()
    return ch

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "draw":
        print("draw")
    elif winner == "user":
        print("user wins")
    else:
        print("Computer wins!")

def play_game():
    global user_score, computer_score
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    
    display_result(user_choice, computer_choice, winner)
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
