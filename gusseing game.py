import random

def guessing_game():
    print("Welcome to Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0


    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break


guessing_game()