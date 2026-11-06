import random


def show_menu():
    print("\n" + "=" * 35)
    print(" NUMBER GUESSING GAME")
    print("=" * 35)
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 200)")
    print("0. Exit")
    print("=" * 35)
def play_game():
    while True:
        show_menu()
        choice = input("Choose difficulty: ").strip()
        if choice == "0":
            print("Thanks for playing!")
            break
        elif choice == "1":
            max_number = 50
            attempts_limit = 10
        elif choice == "2":
            max_number = 100
            attempts_limit = 7
        elif choice == "3":
            max_number = 200
            attempts_limit = 6
        else:
            print("Invalid choice! Please try again.")
            continue
        secret_number = random.randint(1, max_number)
        attempts = 0
        won = False
        print(f"\nI have selected a number between 1 and {max_number}.")
        print(f"You have {attempts_limit} attempts to guess it.")
        print("Type 'q' to quit the current game.")
        while attempts < attempts_limit:
            guess = input("\nEnter your guess: ").strip()
            if guess.lower() == "q":
                print("You left the current game.")
                break
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input! Please enter an integer.")
                continue
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue
            attempts += 1
            if guess == secret_number:
                won = True
                print("\nCongratulations! You guessed the number!")
                print(f"The secret number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            remaining = attempts_limit - attempts
            print(f"Attempts remaining: {remaining}")
        if not won and attempts == attempts_limit:
            print("\nGame Over!")
            print(f"The correct number was {secret_number}.")
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye.")
            break
if __name__ == "__main__":
    play_game()

