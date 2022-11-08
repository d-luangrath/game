"""A number-guessing game."""
import random

def guessing_game():

    user_score = 0
    too_low = 0
    too_high = 101
    
    num = int(input("Choose a number between 1 and 100 \n> "))
    if num not in range(1, 100):
        print("Error. Please enter a valid number.")
   
    secret_num = random.randint(1, 100)
    print(f"High: {too_high}, Low: {too_low}, Secret Number: {secret_num}.")
    

    while secret_num != num:

        try:
            num = int(input("Choose a number between 1 and 100 \n> "))
        except:
            print("Invalid input.")
            continue

        if num not in range(1, 100):
            print("Error. Please enter a valid number.")
            continue
       
        print(f"High: {too_high}, Low: {too_low}, Secret Number: {secret_num}.")
    
        if num < secret_num:
            print("Too low!")
        if num > secret_num:
            print("Too high")
    if num == secret_num:
        print("Congratulations! You guessed the correct number!")
        user_score += 1
        print(f"Your score is {user_score}.")

name = input("What is your name? \n> ").title()
print(f"Hello, {name}! Let's play a guessing game.")

guessing_game()

while True:
    play_again = input("Would you like to play again? Y/N? \n> ").lower()
    if play_again == "y":
        guessing_game()
    elif play_again == "n":
        print("Bye, thanks for playing.")
        break
    else:
        print("Invalid input, enter Y or N (case insensitive)")
        continue
    