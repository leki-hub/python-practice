import random
print("\nI'm thinking of a number between 1 and 100. Can you guess it?")

def guess_number():
    secret_number = random.randint(1, 100)
    tries = 0

    while tries < 7:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("\nCongratulations! You've guessed the secret number in", tries, "tries.")
            break

    if tries ==7:
        print("\nSorry, you've run out of tries. The secret number was", secret_number + ".")

guess_number()
"""or below """ #wow-self taught example on exception handling
import random
print("\nI'm thinking of a number between 1 and 100. Can you guess it?\n")

def guess_number():
    secret_number = random.randint(1, 100)
    tries = 0

    while tries < 7:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("\nCongratulations! You've guessed the secret number in", tries, "tries.")
            break
guess_number()
try:
  while True:
    print("\nSorry, you've run out of tries. The secret number was", "secret_number" + ".")
except Exception as n:
    print("The error has accured" , n)
finally:
    print("An error has been found ")