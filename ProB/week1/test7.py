import random
print("***Welcome to the Number Guessing Game***")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

target_number = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target_number:
        print("Too Low! Try again")
    elif guess > target_number:
        print("Too high! Try again")

    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break