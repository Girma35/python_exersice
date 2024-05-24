import random
from art import logo 
from replit import clear

print(logo)
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def hint():
    global attempt
    global game_again
    attempt = 5 if difficulty == "hard" else 10

    while attempt > 0:
        guess = int(input("Make a guess: "))
        if 1 <= guess <= 100:
            if guess == number:
                print(f"You got it! The answer was {number}")
                return True
            elif guess > number:
                attempt -= 1
                print("Too high.")
            else:
                attempt -= 1
                print("Too low.")

            print(f"Guess again. You have {attempt} attempts remaining to guess the number.")
        else:
            print("Please choose a number between 1 and 100.")

    print("You've run out of guesses, you lose. 😔")
    print("Ohh!!🥺 You can play again")
    game_again = input("Would you like to play again? (yes/no): ").lower()
    return game_again == "yes"

while hint():
    clear()
