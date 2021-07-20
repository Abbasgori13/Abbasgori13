import random

colors = ["red", "blue", "green", "yellow", "black", "white"]

while True:
    pick = random.choice(colors)
    guess = input("Can you guess the colour? ")
    while True:
        if guess == pick:
            break
        else:
            guess = input("Your guess is wrong try again: ")
    print("You guessed it right!")

    play_again = input("Do you want to play again? Type 'no' to quit: ")

    if play_again.lower() == "no":
        break
print("Thanks for playing")