import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Choose: 1. Rock | 2. Paper | 3. Scissors | 4. Quit")

        user_input = input("Enter your choice (1-4): ")

        if user_input == '4':
            print("\nThanks for playing!")
            break
        elif user_input not in ['1', '2', '3']:
            print("Invalid choice! Please choose again.")
            continue

        user_choice = choices[int(user_input) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\nResult: {result}")

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Your score: {user_score} | Computer's score: {computer_score}")

play_game()
