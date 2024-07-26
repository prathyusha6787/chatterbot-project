import random

def number_game():
    print("Welcome to the Number Game!")
    
    play_again = True
    
    while play_again:
        # Step 1: Generate a random number within the specified range
        lower_bound = 1
        upper_bound = 100
        secret_number = random.randint(lower_bound, upper_bound)
        
        # Additional details
        attempts_limit = 10
        attempts = 0

        print(f"I have generated a number between {lower_bound} and {upper_bound}. Can you guess it?")

        while attempts < attempts_limit:
            # Step 2: Prompt the user to enter their guess
            user_guess = int(input("Enter your guess: "))

            # Step 3: Compare the user's guess and provide feedback
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            attempts += 1

        # Display the user's score
        if attempts == attempts_limit:
            print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

    print("Thanks for playing the Number Game!")

# Start the game
number_game()
