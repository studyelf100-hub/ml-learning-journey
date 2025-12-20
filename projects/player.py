# Simple Player Score Tracker
def main():
    # Get player names
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")

    scores = {player1_name: 0, player2_name: 0}
# Start the score tracking loop
    while True:
        print(
            f"\n{player1_name}: {scores[player1_name]} | {player2_name}: {scores[player2_name]}")
        print("\n1. Add points to " + player1_name)
        print("2. Add points to " + player2_name)
        print("3. Show scores")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            points = int(input(f"Points to add to {player1_name}: "))
            scores[player1_name] += points
        elif choice == "2":
            points = int(input(f"Points to add to {player2_name}: "))
            scores[player2_name] += points
        elif choice == "3":
            print(f"\n{player1_name}: {scores[player1_name]}")
            print(f"{player2_name}: {scores[player2_name]}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


# Run the main function
if __name__ == "__main__":
    main()
