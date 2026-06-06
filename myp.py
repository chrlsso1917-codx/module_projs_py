import random
# Accept lower and upper bounds from the user.
# Generate a random number in the selected range.
# Calculate the maximum allowed guesses using the binary search formula.
# Run a loop to take user guesses:
# If the guess is too high, print: "Try Again! You guessed too high."
# If the guess is too low, print: "Try Again! You guessed too small."
# If the guess is correct, print: "Congratulations!" and exit the loop.
# If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 5 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
ch = 5                        # Total allowed chances
gc = 0                        # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
       print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
       break

    # If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"

    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better Luck Next Time!')

    elif guess > num:
        print(f'Too high! Try a lower number.')

    elif guess < num:
        print(f'Too low! Try a higher number.')