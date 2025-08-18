import random

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess it?")

attempts = 0
guess = None

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    except ValueError:
        print("Please enter a valid number!")

print(f" You got it! The secret number was {secret_number}.")
print(f"It took you {attempts} attempts.")
