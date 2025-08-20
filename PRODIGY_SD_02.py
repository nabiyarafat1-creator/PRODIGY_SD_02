import random

def number_guess():
    print("Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 100")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)

        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} tries.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guess()