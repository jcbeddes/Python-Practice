import random

print("Welcome to number guesser!")

def get_guess():
    number = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                print("Out of range. Please guess between 1 and 10.")
                continue

            if guess > number:
                print("Too high! Try again!")
            elif guess < number:
                print("Too low! Try again!")
            else:
                print("Congrats! You win!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

def play_again():
    while True:
        play = input("Do you want to play again? (y/n): ").strip().lower()
        if play == "y":
            get_guess()
        elif play == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please type 'y' or 'n.'")

def main():
    get_guess()
    play_again()
    
main()