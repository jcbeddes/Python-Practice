import random

def get_guess():
    number = random.randint(1, 1000)
    counter = 0
    print(f"Guess counter: {counter}")
    while True:
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
            if guess < 1 or guess > 1000:
                counter += 1
                print(f"Out of range. Guess counter: [{counter}] Please guess between 1 and 10.")
                continue

            if guess > number:
                counter += 1
                print(f"Too high! Try again! Guess counter: {counter}")
            elif guess < number:
                counter += 1
                print(f"Too low! Try again! Guess counter: {counter}")
            else:
                counter += 1
                print(f"Congrats! You won in {counter} guess!")
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
    print("Welcome to number guesser!")
    get_guess()
    play_again()
    
main()