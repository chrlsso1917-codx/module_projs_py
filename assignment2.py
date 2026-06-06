import random

# In this assignment, you will create a simple number guessing game. The program will randomly select a number between 1 and 100, and the user will have to guess it. The program will provide feedback on whether the user's guess is too low, too high, or correct. The game will also keep track of the number of attempts it takes for the user to guess the number correctly. This assignment will help you practice using loops, conditionals, and handling user input in Python.
# You can enhance the game by adding features such as a scoring system, a timer, or different difficulty levels. Have fun coding and enjoy the game!

num = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < num:
            print("Too low! Try again.")
        elif guess > num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {num} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")