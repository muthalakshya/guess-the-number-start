#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random 
print(logo)
def level(correct_no,range_no):
    for position in range(0,range_no[0]):
        print(f"You have {range_no[position]} attempts remaining to guess the no.")
        guess_number = int( input("Make a guess. "))
        if guess_number>correct_no:
            print("Too high.")
        elif guess_number<correct_no:
            print("Too low.")
        else:
            print(f"You got it! answer was {correct_no}.")
            break
    

def compare(difficult_level):    
    correct_no = random.randint(1,101)
    if difficult_level=='easy':
        range_no = [10,9,8,7,6,5,4,3,2,1]
        level(correct_no,range_no)
    else:
        range_no = [5,4,3,2,1]
        level(correct_no,range_no)

print("Welcome to the number Guessing game!")
print("I am thinking of the number between 1 to 100")
difficult_level = input("Choose a difficulty. Type 'easy' or 'hard' :- ")
compare(difficult_level)