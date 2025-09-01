try:
    number = int(input("Number: "))
    if number %  2 == 0:
        print(f"{number} is an even number")
    else:
        print("That's odd.")
except ValueError:
    print("Type a whole number idiot")