import random


def show_menu():
    print("\n" + "=" * 40)
    print(" ROCK PAPER SCISSORS")
    print("=" * 40)
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Exit")
    print("=" * 40)
def show_score(player_score, computer_score, draws):
    print("\n---------- SCORE ----------")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws: {draws}")
    print("---------------------------")
def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    draws = 0
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("\nThanks for playing!")
            show_score(player_score, computer_score, draws)
            break
        elif choice == "1":
            player = "rock"
        elif choice == "2":
            player = "paper"
        elif choice == "3":
            player = "scissors"
        else:
            print("Invalid choice! Please try again.")
            continue
        computer = random.choice(choices)
        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")
        if player == computer:
            print("It's a draw!")
            draws += 1
        elif (
                (player == "rock" and computer == "scissors")
                or (player == "paper" and computer == "rock")
                or (player == "scissors" and computer == "paper")
        ):
            print("Congratulations! You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        show_score(player_score, computer_score, draws)
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing!")
            show_score(player_score, computer_score, draws)
            break
if __name__ == "__main__":
    play_game()

