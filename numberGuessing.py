import random

def number_guessing_game():
    print("Welcome to Number Guessing Game")
    target_number = random.randint(1, 100)
    attempt = 0

    try:
        while True:
            user_guess = int(input("Guess the number (1 - 100):"))
            attempt += 1

            if user_guess == target_number:
                print(f"Congrstualtion , you guessed the correct number {target_number} in {attempt} attempts.")
                break
            elif user_guess < target_number:
                print("Too low , try again")
            else:
                print("Too  high , try again")

    except ValueError:
        print("Error: Please enter a valid number")

number_guessing_game()