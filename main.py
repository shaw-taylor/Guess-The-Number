#Number Guessing Game Objectives:

# Import random
from random import randint

# Include an ASCII art logo.
from art import logo
print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns number of turns remaining"""   
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL
    elif difficulty == 'hard':
        return HARD_LEVEL
    else:
        print("Invalid difficulty choice. Please choose 'easy' or 'hard.")

   
def game():
#Choosing a random number between 1 anf 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The answer is {answer}.")
    
# Reveal the number of remaining attempts.
    turns = set_difficulty()
    
# Repeat the question if the guess was wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")
# Track number of turns and reduce by 1 if they are wrong.

game()


